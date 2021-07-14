from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.http import HttpResponse, JsonResponse

from operator import attrgetter

from blog.models import BlogPost, Like, Dislike, Comment, Reply, CommentReport, ReplyReport
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm, CommentForm, ReplyForm
from account.models import Account


# from personal.views import (
#     home_screen_view,
# )

def create_blog_view(request):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect('must_authenticate')

    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()

    context['form'] = form

    return render(request, "blog/create_blog.html", context)


def like(request):
    if request.method == 'GET':
        post_id = request.GET['post_id']
        # likedpost = Post.objects.get(id=post_id)
        m = Like(post=likedpost)
        m.save()
        return HttpResponse('success')
    else:
        return HttpResponse("unsuccesful")


def detail_blog_view(request, category, year, month, day, time, identity, title):
    context = {}
    blog_post = get_object_or_404(BlogPost, category=category, id=identity)
    context['blog_post'] = blog_post
    user = request.user

    comments = blog_post.comments.all()
    context['comments'] = comments

    new_comment = None
    new_reply = None
    context['new_comment'] = new_comment
    context['new_reply'] = new_comment
    
    total_comments = Comment.objects.all().count() + Reply.objects.all().count()
    context['total_comments'] = total_comments
    total_replies = Reply.objects.all().count()
    context['total_replies'] = total_replies

    if user in blog_post.liked.all():
        like_color = "success"
        dislike_color = "primary"
    elif user in blog_post.disliked.all():
        like_color = "primary"
        dislike_color = "success"
    else:
        like_color = "primary"
        dislike_color = "primary"

    context['like_color'] = like_color
    context['dislike_color'] = dislike_color

    action = request.POST.get('action')
    print(action)
    context['CommentModel'] = Comment.objects

    if request.method == 'POST':
        if action == 'to_comment':
            if user.is_authenticated:
                comment_form = CommentForm(data=request.POST)
                context['comment_form'] = comment_form
                if comment_form.is_valid():

                    # Create Comment object but don't save to database yet
                    new_comment = comment_form.save(commit=False)
                    # Assign the current post to the comment
                    new_comment.post = blog_post
                    new_comment.commenter = request.user
                    # Save the comment to the database
                    new_comment.save()
                    print('saved')
                    context['new_comment'] = new_comment
                    return HttpResponse('success')
                else:
                    print('failed')
                    print(comment_form.errors)
                    return HttpResponse('error')
            else:
                login_message = "Sorry, you have to be logged in to like or dislike posts"
                return HttpResponse("Sorry, you have to be logged in to comment on posts")

        elif action == 'to_reply':
            if user.is_authenticated:
                reply_form = ReplyForm(data=request.POST)
                context['reply_form'] = reply_form

                TBR_id = int(request.POST.get('parent_id'))
                TBR_comment = get_object_or_404(Comment, id=TBR_id)
                print(TBR_comment)

                if reply_form.is_valid():
                    new_reply = reply_form.save(commit=False)
                    new_reply.comment = TBR_comment
                    new_reply.replier = request.user
                    new_reply.save()
                    print('saved')
                    context['new_reply'] = new_reply
                    return HttpResponse('success')
                else:
                    print('failed')
                    print(reply_form.errors)
                    return HttpResponse('error')
            else:
                login_message = "Sorry, you have to be logged in to like or dislike posts"
                return HttpResponse("Sorry, you have to be logged in to reply to comments")


        elif action == "to_report":
            if user.is_authenticated:
                target = request.POST.get('target')
                report_title = request.POST.get('title')
                if target == "comment":
                    comment_id = int(request.POST.get('target_id'))
                    comment = get_object_or_404(Comment, id=comment_id)
                    print(comment)
                    CommentReport.objects.create(title=report_title, comment=comment, reporter=user)
                    print(CommentReport.objects.last())
                    return HttpResponse('success')
                elif target == "reply":
                    reply_id = int(request.POST.get('target_id'))
                    reply = get_object_or_404(Reply, id=reply_id)
                    print(reply)
                    ReplyReport.objects.create(title=report_title, reply=reply, reporter=user)
                    print(ReplyReport.objects.last())
                    return HttpResponse('success')
            else:
                return HttpResponse("Sorry, you have to be logged in to report comments or replies")
                
        else:
            post_id = request.POST.get('post_id')
            post_obj = BlogPost.objects.get(id=post_id)
            post_obj = BlogPost.objects.get(id=post_id)

            if action == 'to_like':
                if user in post_obj.liked.all():
                    post_obj.liked.remove(user)

                elif user in post_obj.disliked.all():
                    post_obj.disliked.remove(user)
                    post_obj.liked.add(user)

                else:
                    if user.is_authenticated:
                        post_obj.liked.add(user)
                        like, like_created = Like.objects.get_or_create(post_id=post_id)

                        if not like_created:
                            if like.value == 'Like':
                                like.value = 'Unlike'
                            else:
                                like.value = 'Like'
                        like.save()
                        return HttpResponse('success')
                    else:
                        login_message = "Sorry, you have to be logged in to like or dislike posts"
                        context['login_message'] = login_message
                        return render(request, 'blog/detail_blog.html', context)



            elif action == 'to_dislike':
                if user in post_obj.disliked.all():
                    post_obj.disliked.remove(user)

                elif user in post_obj.liked.all():
                    post_obj.liked.remove(user)
                    post_obj.disliked.add(user)

                else:
                    if user.is_authenticated:
                        post_obj.disliked.add(user)
                        dislike, dislike_created = Dislike.objects.get_or_create(post_id=post_id)

                        if not dislike_created:
                            if dislike.value == 'Like':
                                dislike.value = 'Unlike'
                            else:
                                dislike.value = 'Like'
                        dislike.save()
                        return HttpResponse('success')
                    else:
                        login_message = "Sorry, you have to be logged in to like or dislike posts"
                        context['login_message'] = login_message
                        return render(request, 'blog/detail_blog.html', context)


    # post = get_object_or_404(Post, slug=Post.slug)
    # if post.slug != slug:
    # return redirect('blog:post-detail', slug=Post.slug)
    else:
        pass
    # return HttpResponse("unsuccesful")

    query = ""

    # if request.method == "GET":
    # 	query = request.GET.get('cat', '')
    # 	context['query'] = str(query)

    # 	home_screen_view()

    # print(blog_post.date_updated)

    # GET TRENDING POSTS
    trending_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)[:6]
    context['trending_posts'] = trending_posts

    # GET RELATED POSTS
    post_title = blog_post.title
    related_posts = sorted(get_blog_queryset(post_title), key=attrgetter('date_updated'), reverse=True)[:6]
    context['related_posts'] = related_posts

    # GET MORE POSTS FROM THE SAME AUTHOR
    author_posts = get_author_posts(blog_post.author, blog_post.id, 6)
    context['author_posts'] = author_posts

    comment_form = CommentForm()
    context['comment_form'] = comment_form

    reply_form = ReplyForm()
    context['reply_form'] = reply_form
    return render(request, 'blog/detail_blog.html', context)


def edit_blog_view(request, category):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    blog_post = get_object_or_404(BlogPost, category=category)

    if blog_post.author != user:
        return HttpResponse('You are not the author of that post.')

    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance=blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            context['success_message'] = "Updated!"
            blog_post = obj

    form = UpdateBlogPostForm(
        initial={
            "category": blog_post.category,
            "title": blog_post.title,
            "body": blog_post.body,
            "image": blog_post.image,
        }
    )

    context['form'] = form
    return render(request, 'blog/edit_blog.html', context)


def get_blog_queryset(query=None):
    queryset = []
    # query = "and"
    queries = query.split(" ")  # python install 2019 = [python, install, 2019]

    # print(queries)

    for q in queries:
        posts = BlogPost.objects.filter(
            Q(title__icontains=q) |
            Q(body__icontains=q)
        ).distinct()

        for post in posts:
            queryset.append(post)

    return list(set(queryset))


def get_author_posts(post_author, post_id=None, limit=None):
    post_author_id = Account.objects.get(username=post_author).id
    if post_id:
        author_posts = BlogPost.objects.filter(author=post_author_id).exclude(id=post_id)[:limit]
    else:
        author_posts = BlogPost.objects.filter(author=post_author_id)[:limit]
    md = {}

    for post in author_posts:
        md[post.date_updated] = post.id

    ml = sorted(md, reverse=True)
    sorted_posts = []

    for element in ml:
        post = BlogPost.objects.get(id=md[element])
        sorted_posts.append(post)

    return sorted_posts

# def get_related_posts(query=None):
#     queryset = []
# 	# query = "and"
#     queries = query.split(" ") # python install 2019 = [python, install, 2019]

# 	# print(queries)

# 	for q in queries:
# 		posts = BlogPost.objects.filter(
# 				Q(title__icontains=q) | 
# 				Q(body__icontains=q) |
# 				Q(author__notcontain=q)
# 			).distinct()

# 		for post in posts:
# 			queryset.append(post)

# 	return list(set(queryset))


# def get_trending_posts(query=None):
# 	queryset = []
# 	# query = "and"
# 	queries = query.split(" ") # python install 2019 = [python, install, 2019]

# 	# print(queries)

# 	for q in queries:
# 		posts = BlogPost.objects.filter(
# 				Q(title__icontains=q) | 
# 				Q(body__icontains=q) |
# 				Q(author__notcontain=q)
# 			).distinct()

# 		for post in posts:
# 			queryset.append(post)

# 	return list(set(queryset))
