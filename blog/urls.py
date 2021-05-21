from django.urls import path
from blog.views import (
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
    like,
)

app_name = 'blog'

urlpatterns = [
    path('create/', create_blog_view, name="create"),
    path('like/', like, name='like'),
    # path('<category>/<year>/<month>/', detail_blog_view, name="detail"),
    path('<category>/<year>/<month>/<day>/<time>/<identity>/<title>/', detail_blog_view, name="detail"),
    path('<category>/edit/', edit_blog_view, name="edit"),
]
