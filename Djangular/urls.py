"""
Definition of urls for Djangular.
"""


# Uncomment the next lines to enable the admin:

from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

# from rest_framework_jwt.views import obtain_jwt_token
#from django.views.decorators.csrf import ensure_csrf_cookie  #use this on the login page later to protect it from csrf attacks

 #admin.autodiscover()

urlpatterns = [
    # Examples:

    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="scrumboard/home.html")),

    url(r'^scrumboard/', include('scrumboard.urls')),
    url(r'^profile/', include('profiles.urls')),
    url(r'^lesson/', include('lessons.urls')),
    url(r'^docs/', include('rest_framework_docs.urls')),
    # url(r'^user/', include('authentication.urls')),
    url(r'^auth/', include('rest_auth.urls')),
    url(r'^auth/registration', include('registration.urls')),
    # url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    # url(r'^auth/', include('rest_framework_social_oauth2.urls', namespace='social')),

#    url(r'^api/', include('api.urls')),
  #  url(r'^docs/', include('rest_framework_docs.urls')),
 


  #  url(r'^auth_api/', include('auth_api.urls')),
  #  url(r'^admin/', admin.site.urls),

   # url(r'^scrum$', scrumboard.)

    #url(r'^$', app.views.home, name='home'),
    #url(r'^contact$', app.views.contact, name='contact'),
    #url(r'^about', app.views.about, name='about'),
    #url(r'^login/$',
    #    django.contrib.auth.views.login,
    #    {
    #        'template_name': 'app/login.html',
    #        'authentication_form': app.forms.BootstrapAuthenticationForm,
    #        'extra_context':
    #        {
    #            'title': 'Log in',
    #            'year': datetime.now().year,
    #        }
    #    },
    #    name='login'),
    #url(r'^logout$',
    #    django.contrib.auth.views.logout,
    #    {
    #        'next_page': '/',
    #    },
    #    name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   #  url(r'^admin/', include(admin.site.urls)),
]
