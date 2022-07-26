from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)


urlpatterns = [
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('horses/', views.horses_index, name='index'),
path('horses/<int:horse_id>/', views.horses_detail, name='detail'),
path('horses/create/', views.HorseCreate.as_view(), name='horses_create'),
path('horses/<int:pk>/update/', views.HorseUpdate.as_view(), name='horses_update'),
path('horses/<int:pk>/delete/', views.HorseDelete.as_view(), name='horses_delete'),
path('horses/<int:horse_id>/add_feeding/', views.add_feeding, name='add_feeding'),
path('toys/', views.ToyList.as_view(), name='toys_index'),
path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toys_detail'),
path('toys/create/', views.ToyCreate.as_view(), name='toys_create'),
path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toys_update'),
path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toys_delete'),
path('horses/<int:horse_id>/assoc_toy/<int:toy_id>/', views.assoc_toy, name='assoc_toy'),
path('horses/<int:horse_id>/add_photo/', views.add_photo, name='add_photo'),
path('accounts/signup/', views.signup, name='signup'),
path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
path('register/', views.RegisterView.as_view(), name='auth_register'),
path('', views.getRoutes)
]