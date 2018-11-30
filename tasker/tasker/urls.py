from django.conf.urls import url
from django.contrib import admin
from taskerapp import views
from django.contrib.auth import views as auth_views
from django.conf.urls import include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^task/sign-in/$', auth_views.login, {
        'template_name': 'task/sign_in.html',
        },
       
      
        name='task-sign-in'),
    url(r'^task/sign-out/$', auth_views.logout, {
        'next_page': '/'},
        name='task-sign-out'),
    url(r'^task/$', views.task_home, name="task-home"),
    url(r'^task/sign-up-learner/$', views.task_sign_up_learner, 
        name='task-sign-up-learner'),
     url(r'^task/sign-up-teacher/$', views.task_sign_up_teacher, 
        name='task-sign-up-teacher'),
    url(r'^task/account/$', views.task_account, 
        name='task-account'),
    url(r'^task/gigs/(?P<id>[0-9]+)/$', views.gig_detail, 
        name='gig-detail'),
    url(r'^task/my-gigs/$', views.my_gigs, 
        name='my-gigs'),
    url(r'^task/create-gig/$', views.create_gig, 
        name='create-gig'),
        url(r'^task/profile/(?P<username>\w+)/$', views.profile, 
        name='profile'),
    url(r'^task/search/$', views.search, 
        name='search'),    
    url(r'^task/lending-page/$', views.lending_page, 
        name='lending-page'), 
    url(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

