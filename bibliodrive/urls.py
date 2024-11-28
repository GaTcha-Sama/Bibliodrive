"""
URL configuration for bibliodrive project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from backoffice import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('', views.base, name='base'),

    path('titles/', views.title_list, name='title_list'),
    path('title/<str:isbn>/', views.title_detail, name='title_detail'),
    path('reserve/<str:isbn>/', views.reserve_title, name='reserve_title'),
    path('cancel-reserve/<str:isbn>/', views.cancel_reserve, name='cancel_reserve'),

    path('authors/', views.author_list, name='author_list'),
    path('author/<int:au_id>/', views.author_detail, name='author_detail'),
    
    path('publishers/', views.publishers_list, name='publisher_list'),
    path('publisher/<int:pubid>', views.publisher_detail, name='publisher_detail'),

    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__',
include(debug_toolbar.urls))
    ] + urlpatterns
