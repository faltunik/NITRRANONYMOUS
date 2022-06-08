"""chauraha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from posts import views as post_views
from polls import views as poll_views
from users import views as user_views
from django.contrib.auth import views as auth_views
# from reset_password.views import ResetPasswordView
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register("reset-password", ResetPasswordView, basename="reset_password")




post_router = DefaultRouter()
comment_router = DefaultRouter()
reply_router = DefaultRouter()
poll_router = DefaultRouter()
profile_router = DefaultRouter()
# register our viewset with router
post_router.register('post', post_views.PostView, basename = 'post')
comment_router.register('comment', post_views.CommentView, basename= 'comments')
reply_router.register('reply', post_views.ReplyView, basename= 'reply')
poll_router.register('poll', poll_views.PollViewSet, basename= 'poll')
profile_router.register('profile', user_views.ProfileViewSets, basename= 'profile')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('users.urls')),
    path('like/', include('posts.urls')),
    path('pollaction/', include('polls.urls')),
    path('post/', include(post_router.urls)),
    path('comments/', include(comment_router.urls)),
    path('reply/', include(reply_router.urls)),
    path('poll/', include(poll_router.urls)),
    path('profile/', include(profile_router.urls)),
    path('reset_password/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset_password/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    # path('reset/',include(router.urls)),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
