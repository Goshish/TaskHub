from django.urls import path
from . import views
from .views import LoginUser
from .views import RegisterFormView

urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('reg', RegisterFormView.as_view(), name='reg'),
    path('log_in', LoginUser.as_view(), name='log_in'),
]



