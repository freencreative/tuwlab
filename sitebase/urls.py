from django.conf.urls import include, url
from django.contrib import admin
from myapp import views as MyAppView

urlpatterns = [
    # Examples:
    # url(r'^$', 'sitebase.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mypage/', MyAppView.DisplayMyPage),
    url(r'^mypage_param/(?P<my_parameter>.+)', MyAppView.DisplayMyPageWithParameter),
    url(r'^insert/(?P<isbn>.+);(?P<title>.+);(?P<memo>.*)', MyAppView.InsertBook),
    url(r'^show/(?P<isbn>.+)', MyAppView.DisplayBook),
]
