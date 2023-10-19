from django.contrib import admin
from django.urls import path
from . import views
from .views import DarajaApiView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accesstoken/', views.get_access_token, name='get_access_token'),
    path('stkpush/', DarajaApiView.as_view(), name='initiate_stk_push'),
    path('query/', views.query_stk_status, name='query_stk_status'),
    path('callback/', views.process_stk_callback)


]