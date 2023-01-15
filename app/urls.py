from django.urls import include, path
from.import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('login_page',views.login_page,name='login_page'),
    path('registration',views.registration,name='registration'),
    path('super_admin',views.super_admin,name='super_admin'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('add_desigination',views.add_desigination,name='add_desigination'),
    path('add_vehicle',views.add_vehicle,name='add_vehicle'),
    path('update_vehicle/<int:pk>/',views.update_vehicle,name='update_vehicle'),
    path('delete/<int:pk>/',views.delete_vehicle,name='delete_vehicle'),
    path('update_vehicle_admin/<int:pk>/',views.update_vehicle_admin,name='update_vehicle_admin'),
    path('user_admin_list',views.user_admin_list,name='user_admin_list'),
    path('delete_user_admin/<int:pk>/',views.delete_user_admin,name='delete_user_admin'),
    path('userhome/',views.userhome,name='userhome'),
    path('user_logout',views.user_logout,name='user_logout'),
    
   
    
    
    ]