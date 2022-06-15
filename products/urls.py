from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='mainpage-url'),
    path('register/', views.registerPage, name='reg-url'),
    path('login/', views.loginPage, name='log-url'),
    path('logout/', views.logoutPage, name='logout-url'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process_item'),
    path('cart/', views.cart_page, name='cart-url'),
    path('<category_name>/', views.category_page, name='category-url'),

]
