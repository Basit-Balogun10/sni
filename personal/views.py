from django.db.models import Q
from django.shortcuts import render
from django.utils import timezone
from operator import attrgetter
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from blog.views import get_blog_queryset, get_author_posts
from blog.models import BlogPost

from datetime import timedelta, datetime

BLOG_POSTS_PER_PAGE = 18


def home_screen_view(request, *args, **kwargs):
    context = {}

    # Search
    query = ""

    if request.method == "GET":
        if request.GET.get('posted-since'):
            print(request.GET.get('posted-since'))


        elif request.GET.get('related-to'):
            print(request.GET.get('related-to'))
            post_title = request.GET.get('related-to')
            related_posts = sorted(get_blog_queryset(post_title), key=attrgetter('date_updated'), reverse=True)
            blog_posts = related_posts

        elif request.GET.get('posts-from'):
            print(request.GET.get('posts-from'))
            author = request.GET.get('posts-from')
            blog_posts = get_author_posts(author)

        elif request.GET.get('time-filter') and not request.GET.get('category-filter'):
            print('time only')
            time_filter = request.GET.get('time-filter')
            context['time_filter'] = time_filter
            category_filter = request.GET.get('category-filter')
            context['category_filter'] = category_filter
            now = timezone.now()
            time_frame = {"all": None, "today": 0, "yesterday": 1, "last week": 7, "2 weeks ago": 14, "3 weeks ago": 21,
                          "last month": 28, "this year": 365}
            no_of_days = time_frame[time_filter.lower()]
            if no_of_days == 0:
                time_delta = timedelta(hours=24)
            else:
                time_delta = timedelta(days=no_of_days)

            query = request.GET.get('q', '')
            print("TIME-QUERY: ", query)
            context['query'] = str(query)
            queryset = []
            # query = "and"
            queries = query.split(" ")  # python install 2019 = [python, install, 2019]

            # print(queries)

            if (now - time_delta) <= now:
                for q in queries:
                    posts = BlogPost.objects.filter(
                        Q(title__icontains=q) |
                        Q(body__icontains=q)
                    ).filter(Q(date_updated__gte=now - time_delta) & Q(date_updated__lte=now)).distinct()

                    for post in posts:
                        queryset.append(post)

            raw_blog_posts = list(set(queryset))

            blog_posts = sorted(raw_blog_posts, key=attrgetter('date_updated'), reverse=True)

        elif request.GET.get('category-filter') and not request.GET.get('time-filter'):
            print('category only')
            time_filter = request.GET.get('time-filter')
            context['time_filter'] = time_filter
            category_filter = request.GET.get('category-filter')
            context['category_filter'] = category_filter

            query = request.GET.get('q', '')
            print("CAT-QUERY: ", query)
            context['query'] = str(query)
            queryset = []
            # query = "and"
            queries = query.split(" ")  # python install 2019 = [python, install, 2019]

            # print(queries)

            for q in queries:
                posts = BlogPost.objects.filter(
                    Q(title__icontains=q) |
                    Q(body__icontains=q)
                ).filter(category=category_filter).distinct()

                for post in posts:
                    queryset.append(post)

            raw_blog_posts = list(set(queryset))

            blog_posts = sorted(raw_blog_posts, key=attrgetter('date_updated'), reverse=True)

        elif request.GET.get('time-filter') and request.GET.get('category-filter'):
            print('time and category')
            time_filter = request.GET.get('time-filter')
            context['time_filter'] = time_filter.lower()
            category_filter = request.GET.get('category-filter')
            context['category_filter'] = category_filter
            now = timezone.now()
            time_frame = {"all": None, "today": 0, "yesterday": 1, "last week": 7, "2 weeks ago": 14, "3 weeks ago": 21,
                          "last month": 28, "this year": 365}
            no_of_days = time_frame[time_filter.lower()]
            time_delta = timedelta(days=no_of_days)

            query = request.GET.get('q', '')
            print("BOTH-QUERY: ", query)
            context['query'] = str(query)
            queryset = []
            # query = "and"
            queries = query.split(" ")  # python install 2019 = [python, install, 2019]

            # print(queries)

            if (now - time_delta) <= now:
                for q in queries:
                    posts = BlogPost.objects.filter(
                        Q(title__icontains=q) |
                        Q(body__icontains=q)
                    ).filter(Q(date_updated__gte=now - time_delta) & Q(date_updated__lte=now) & Q(
                        category__iexact=category_filter)).distinct()

                    for post in posts:
                        queryset.append(post)
            raw_blog_posts = list(set(queryset))

            blog_posts = sorted(raw_blog_posts, key=attrgetter('date_updated'), reverse=True)

        else:
            query = request.GET.get('q', '')
            print("QUERY ", query)
            print(request.GET.get('test'))
            context['query'] = str(query)
            blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)
    else:
        pass
    # Pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts

    return render(request, "personal/home.html", context)
