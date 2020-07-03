"""ask URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin

#from qa.views import test

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#]
urlpatterns = [
    url(r'^$', qa.views.test, name='index'),				        #/
    url(r'^login/', qa.views.test, name='login'),			        #/login/
    url(r'^signup/', qa.views.test, name='signup'),	           	#/signup/
#    url(r'^question/<([0-9]{3})>/', qa.views.test, name='question'), #/question/<255>/
    url(r'^question/<int:id>/', qa.views.test, name='question'), #/question/<255>/
    url(r'^ask/', qa.views.test, name='ask'),			           	#/ask/
    url(r'^popular/', qa.views.test, name='popular'),	         	#/popular/
    url(r'^view/', qa.views.test, name='view'),		          	#/view/
]