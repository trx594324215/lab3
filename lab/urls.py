from django.conf.urls import patterns, include, url
from django.contrib import admin
from lab import views
from lab import my_homepage_view
#import my_homepage_view.home
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lab.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    ('^$',my_homepage_view.home),
    (r'^search/$',my_homepage_view.home),
    (r'^more',views.more),
    (r'^delete',views.delete),
    (r'^edit',views.edit),
    (r'^after',views.after),
    url(r'^admin/', include(admin.site.urls)),
)
