from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    #path('payment/',views.PaymentNet.as_view()),
    url(r'^$',views.CreateNetwork.as_view(),name='home'),
    path('product/',views.product)
    
]
