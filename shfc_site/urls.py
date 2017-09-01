# from django.conf.urls.defaults import patterns, include, url

# # Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

# urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'shfc_site.views.home', name='home'),
#     # url(r'^shfc_site/', include('shfc_site.foo.urls')),

#     # Uncomment the admin/doc line below to enable admin documentation:
#     # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

#     # Uncomment the next line to enable the admin:
#     url(r'^admin/', include(admin.site.urls)),


# )

from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib import admin, auth
from django.contrib.auth import views as auth_views

admin.autodiscover()

urlpatterns = patterns('',
    url(r"^$", "home.views.index"),
    url(r"^fishing/home/$", 'boats.views.home_index'),
    url(r"^fishing/boats/$", 'boats.views.index'),
    url(r"^boats/data/$", 'boats.views.schedule'),
    url(r"^membership/$", 'membership.views.index'),

    url(r"^ranges/home/$", 'range.views.home_index'),
    url(r"^ranges/archery/", 'archery.views.index'),
    url(r"^ranges/range/$", 'range.views.index'),
    url(r"^ranges/home/rso/calender/data/$", 'range.views.rso_calendar_data'),


    url(r'^polls/$', 'polls.views.index'),
    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),
    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),
    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
    url(r'^admin/', include(admin.site.urls)),

    # url(r'^login$', auth_views.login, name='login'),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout'),
)
