from django.urls import path
from Backend import views


urlpatterns = [
    path('indexpage/',views.indexpage, name='indexpage'),
    path('staffpage/',views.staffpage, name='staffpage'),
    path('savedata/',views.savedata, name='savedata'),
    path('displaystaffpage/',views.displaystaffpage,name='displaystaffpage'),
    path('editstaffpage/<int:dataid>/', views.editstaffpage, name='editstaffpage'),
    path('updatestaffdata/<int:dataid>/',views.updatestaffdata,name='updatestaffdata'),
    path('deletestaffdata/<int:dataid>/',views.deletestaffdata,name='deletestaffdata'),

                             #Category
    path('categorypage/',views.categorypage, name='categorypage'),
    path('savedata2/',views.savedata2, name='savedata2'),
    path('displaycategory/',views.displaycategory,name='displaycategory'),
    path('editcategory/<int:dataid>/', views.editcategory, name='editcategory'),
    path('updatecategory/<int:dataid>/',views.updatecategory,name='updatecategory'),
    path('deletecategory/<int:dataid>/',views.deletecategory,name='deletecategory'),
    path('productpage/',views.productpage, name='productpage'),
    path('datasave/',views.datasave, name='datasave'),
    path('displayproduct/',views.displayproduct,name='displayproduct'),
    path('editproduct/<int:dataid>/', views.editproduct, name='editproduct'),
    path('updateproduct/<int:dataid>/',views.updateproduct,name='updateproduct'),
    path('deleteproduct/<int:dataid>/',views.deleteproduct,name='deleteproduct'),
    path('adminloginpage/',views.adminloginpage, name='adminloginpage'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('adminlogout/',views.adminlogout,name='adminlogout'),
    path('acontactpage/',views.acontactpage, name='acontactpage'),
    path('deletecontactdata/<int:dataid>/',views.deletecontactdata,name='deletecontactdata'),
    path('abookpage/',views.abookpage, name='abookpage'),
    path('deletebookingdata/<int:dataid>/',views.deletebookingdata,name='deletebookingdata'),
    path('abillingpage/', views.abillingpage, name='abillingpage'),
    path('deletebillingdata/<int:dataid>/', views.deletebillingdata, name='deletebillingdata')

]