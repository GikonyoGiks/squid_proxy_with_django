from django.contrib.auth.views import LogoutView
from django.urls import include,path
from django.contrib import admin
import kratos.settings as settings
import auth.views as views
...

urlpatterns = [
        path('admin/', admin.site.urls, name='administrator'),
        path('', include('social_django.urls', namespace='social')),
        #path('', views_main.index, name='index'),
        path(
            'logout/',
            LogoutView.as_view(template_name=settings.LOGOUT_REDIRECT_URL),
            name='logout'
            ),
        path('manage/', views.manage, name='manage'),
        ]
