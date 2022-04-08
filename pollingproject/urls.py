"""pollingproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from polling.views import signuppage, loginpage, firstpage, page, loginpage_d, create_poll, poll, poll_result

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', firstpage),
    path('loginpage', loginpage),
    path('signuppage', signuppage),
    path('signuppage_data', page),
    path('loginpage_data', loginpage_d),
    path('create_poll', create_poll),
    path('poll', poll),
    path('poll_result', poll_result),
]
