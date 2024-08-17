from django.urls import path, include
from . import views

urlpatterns=[
    path('', views.index, name='home'),

    #registration
    path('customer_registration',views.customer_registration,name='customer_registration'),
    path('plantshop_registration',views.plantshop_registration,name='plantshop_registration'),

    #login/logout
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),

    #profil view
    path('customer_profile',views.customer_profile,name='customer_profile'),
    path('plantshop_profile',views.plantshop_profile,name='plantshop_profile'),

    #customer
    path('edit_customer_view',views.edit_customer_view,name='edit_customer_view'),
    path('edit_customer/<int:id>',views.edit_customer,name='edit_customer'),
    path('edit_customer/update_customer/<int:id>',views.update_customer,name='update_customer'),
    path('delete_customer/<int:id>',views.delete_customer,name='delete_customer'),

    #plantshop
    path('edit_plantshop_view',views.edit_plantshop_view,name='edit_plantshop_view'),
    path('edit_plantshop/<int:id>',views.edit_plantshop,name='edit_plantshop'),
    path('edit_plantshop_view/update_plantshop/<int:id>/',views.update_plantshop,name='update_plantshop'),
    path('delete_plantshop/<int:id>',views.delete_plantshop,name='delete_plantshop'),

    #product
    path('add_product',views.add_product,name='add_product'),
    path('add_product_save',views.add_product_save,name='add_product_save'),
    path('delete_product/<int:id>',views.delete_product,name='delete_product'),
    path('added_successfully',views.added_successfully,name='added_successfully'),

    path('product_list_view_for_customer/',views.product_list_view_for_customer,name='product_list_view_for_customer'),

    path('product_profile/<int:id>/',views.product_profile,name='product_profile'),
    path('product_profile/add_product_to_cart/<int:id>',views.add_product_to_cart,name='add_product_to_cart'),
    path('cart_view/', views.cart_view, name='cart_view'),
    path('my_products',views.my_products,name='my_products'),
    path('cart_view/proceed/<int:id>', views.proceed, name='proceed'),
    path('delete_cartitem/<int:id>',views.delete_cartitem,name='delete_cartitem'),
    
    path('order_summary/<int:id>',views.order_summary,name='order_summary'),
    path('order_summary_new/buy_now/<int:id>',views.buy_now,name='buy_now'),
    path('my_orders/',views.my_orders,name='my_orders'),
    # path('payment_success/',views.payment_success,name='payment_success'),
    path('orders_got/',views.orders_got,name='orders_got'),
    path('product_list_cacti/',views.product_list_cacti,name='product_list_cacti'),
    path('product_list_indoor/',views.product_list_indoor,name='product_list_indoor'),
    path('product_list_flowering/',views.product_list_flowering,name='product_list_flowering'),
    path('product_list_fruit/',views.product_list_fruit,name='product_list_fruit'),
    path('product_list_hanging/',views.product_list_hanging,name='product_list_hanging'),
    path('product_list_all',views.product_list_all,name='product_list_all'),
    path('search/', views.search_products, name='search_products'),

]