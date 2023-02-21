from django.urls import path
from frontend import views

urlpatterns = [
    path('webpage/',views.webpage, name='webpage'),
    path('cbillingpage/', views.cbillingpage, name='cbillingpage'),
    path('cart/<int:dataid>', views.cart, name='cart'),
    path('contactpage/',views.contactpage,name='contactpage'),
    path('aboutpage/',views.aboutpage,name='aboutpage'),
    path('discategory/<itemcatg>',views.discategory,name='discategory'),
    path('bookpage/',views.bookpage,name='bookpage'),
    path('signpage/',views.signpage,name='signpage'),
    path('savelogin/', views.savelogin, name='savelogin'),
    path('customerlogin/',views.customerlogin, name='customerlogin'),
    path('customerlogout/',views.customerlogout, name='customerlogout'),
    path('savedata5/', views.savedata5, name='savedata5'),
    path('savedata6/', views.savedata6, name='savedata6'),
    path('savebiling/', views.savebiling, name='savebiling'),


]