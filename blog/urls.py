from django.conf.urls import patterns, include, url
from blog import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index,name = 'index'),
    url(r'^news/', views.news,name = 'news'),
    url(r'^article/', views.article,name = 'article'),

)
