#coding=utf-8

from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

#from account.forms import SignupFormExtra

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'yaayaa.views.home', name='home'),
    url(r'^blog/', include('blog.urls')),

    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Demo Override the signup form with our own, which includes a
    # first and last name.
    # (r'^accounts/signup/$',
    #  'userena.views.signup',
    #  {'signup_form': SignupFormExtra}),

    (r'^account/', include('userena.urls')),
    (r'^messages/', include('userena.contrib.umessages.urls')),
    url(r'^account/promo/$', 'account.views.promo', name='promo'),
    (r'^i18n/', include('django.conf.urls.i18n')),

    # 启用 django-ajax 框架
    (r'^ajax/', include('ajax.urls')),
)

# Add media and static files
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
