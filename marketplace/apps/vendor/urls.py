from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('become-vendor/',views.become_vendor,name='become_vendor'),
    path('vendor-admin/',views.vendor_admin,name='vendor_admin'),
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('login/',auth_views.LoginView.as_view(template_name='vendor/login.html'),name='login'),
    path('add-product',views.add_product,name='add_product'),
    path('edit-vendor/',views.edit_vendor,name='edit_vendor'),
    path('',views.vendors,name='vendors'),
    path('<int:vendor_id>/',views.vendor,name='vendor'),
    path('edit_product/<int:pk>/',views.edit_product,name='edit_product'),
]
