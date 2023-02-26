from django.contrib import admin
from django.urls import path
from admin_black import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', views.dashboard, name='dashboard'),
     path('icons/', views.icons, name='icons'),
     path('map/', views.map, name='map'),
     path('notifications/', views.notifications, name='notifications'),
     path('user-profile/', views.user_profile, name='user_profile'),
     path('tables/', views.tables, name='tables'),
     path('typography/', views.typography, name='typography'),
     path('rtl/', views.rtl, name='rtl'),
     path('upgrade/', views.upgrade, name='upgrade'),

     path('accounts/auth-signup/', views.auth_signup, name = 'auth_signup'),
     path('accounts/auth-signin/', views.AuthSignin.as_view(), name='auth_signin'),
     path('accounts/forgot-password/', views.UserPasswordResetView.as_view(), name='forgot_password'),

     path('accounts/password-reset-confirm/<uidb64>/<token>/', 
        views.UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
     path('accounts/password-change/', views.UserPasswordChangeView.as_view(), name='password_change'),
     path('accounts/password-change-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='accounts/password_change_done.html'
    ), name="password_change_done" ),
    path('accounts/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='accounts/password_reset_complete.html'
    ), name='password_reset_complete'),
    path('accounts/password-reset-done/', auth_views.PasswordResetDoneView.as_view(
        template_name='accounts/password_reset_done.html'
    ), name='password_reset_done'),
    path('accounts/logout/', views.user_logout_view, name='logout'),

]