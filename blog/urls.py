from django.urls import path
from blog.views import (
    create_blog_view,
    detail_blog_view,
    edit_blog_view,
    like,
)
from personal.views import (
    home_screen_view,
)

app_name = 'blog'

urlpatterns = [
    # path('create/', create_blog_view, name="create"),
    # path('like/', like, name='like'),
    # path('<category>/<year>/<month>/', detail_blog_view, name="detail"),
    path('trending', home_screen_view, name="home"),
    path('<category>/<year>/<month>/<day>/<time>/<identity>/<title>/', detail_blog_view, name="detail"),
    # path('<category>/edit/', edit_blog_view, name="edit"),
]
