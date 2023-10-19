from django.urls import path
from .views import ProductListView
from .views import ProductDetailView
from .views import CartListView
from .views import CartDetailView
from api.views import OrderDetailView, OrderListView
from .views import CompanyLocationAPI
from .views import UserLoginView, UserLogoutView, UserRegistrationView,UserListView
from .views import DeliveryList, DeliveryDetail




urlpatterns=[
    path("product/" ,ProductListView.as_view(),name="product_list_view"),
    path("product/<int:id>/",ProductDetailView.as_view(),name="product_detail_view"),
    path("cart/" ,CartListView.as_view(),name="product_list_view"),
    path("cart/<int:id>/",CartDetailView.as_view(),name="product_detail_view"),
    path("orders/", OrderListView.as_view(), name="order_list"),
    path("orders/<int:id>/", OrderDetailView.as_view(), name="order_detail"),
    path('location/', CompanyLocationAPI.as_view(), name='company_location_view'),
    path('location/<int:user_id>/', CompanyLocationAPI.as_view(), name='company_location_view'),
    path('deliveries/', DeliveryList.as_view(), name='delivery_list'),
    path('deliveries/<int:id>/', DeliveryDetail.as_view(), name='delivery_detail'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('user/', UserListView.as_view(), name='user'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
  

]



