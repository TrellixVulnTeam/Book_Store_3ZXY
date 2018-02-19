from django.conf.urls import url,include
from . import views
#from bookstore.views import login_view

urlpatterns = [
    url(r'^$', views.home),
    url(r'^register/', views.register),
    url(r'^login/$', views.auth_view.login, {'template_name': 'Login.html'}),
    url(r'^logout/$', views.auth_view.logout, {'template_name': 'Logout.html'})
]
