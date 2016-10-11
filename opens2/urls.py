"""opens2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add opens2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))

"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from lms.views import (ListProjects, ProjectDetail, ListAllProjects, ListLessons, LessonDetail, ListAllLessons,
		ListTests, TestDetail, ListAllTests)
from django.views.generic import DetailView, View

urlpatterns = [
	# Auth
    url(r'^logout/$', auth_views.logout, {'next_page': 'projects'}, name='logout'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    
    # Admin
    url(r'^admin/', admin.site.urls),
    
    #Custom
    url(r'^$', ListProjects.as_view(), name='projects'),
    url(r'^projects/$', ListProjects.as_view(), name='project-list'),
    url(r'^projects/(?P<pk>[-\w]+)/$', ProjectDetail.as_view(), name='project-detail'),
 	url(r'^lessons/$', ListLessons.as_view(), name='lesson-list'),
    url(r'^lessons/(?P<pk>[-\w]+)/$', LessonDetail.as_view(), name='lesson-detail'),
    url(r'^tests/$', ListTests.as_view(), name='test-list'),
    url(r'^tests/(?P<pk>[-\w]+)/$', TestDetail.as_view(), name='test-detail'),
]
