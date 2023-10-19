# from rest_framework.routers import DefaultRouter
# from .views import EwasteRequestViewSet
# from django.urls import path, include

# router = DefaultRouter()
# router.register(r'ewaste-requests', EwasteRequestViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),
# ]



from rest_framework.routers import DefaultRouter
from .views import EwasteRequestViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'ewaste-requests', EwasteRequestViewSet)

custom_routes = [
    path('ewaste-requests/<int:id>/update/', EwasteRequestViewSet.as_view({'put': 'put'}), name='ewaste-request-update'),
    path('ewaste-requests/<int:id>/delete/', EwasteRequestViewSet.as_view({'delete': 'delete'}), name='ewaste-request-delete')
]

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/', include(custom_routes))
]
