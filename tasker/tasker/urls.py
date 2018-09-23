from django.conf.urls import url
from django.contrib import admin
from taskerapp import views
from django.contrib.auth import views as auth_views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
    url(r'^task/sign-in/$', auth_views.login, {
        'template_name': 'task/sign_in.html'},
        name='task-sign-in'),
    url(r'^task/sign-out/$', auth_views.logout, {
        'next_page': '/'},
        name='task-sign-out'),
    url(r'^task/$', views.task_home, name="task-home"),
    url(r'^task/sign-up/$', views.task_sign_up, 
        name='task-sign-up'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

