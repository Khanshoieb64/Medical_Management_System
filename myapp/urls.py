from django.urls import path
from myapp import views



urlpatterns = [
    path('',views.Login.as_view(),name='login'),
    path('signup',views.Signup.as_view(),name='signup'),
    path('logout',views.logout,name='logout'),
    path('home',views.home,name='home'),
    path('addmd',views.AddMedicineDetail.as_view(),name='addmd'),
    path('updatepage',views.updatepage,name='updatepage'),
    path('deletepage',views.deletepage,name='deletepage'),
    path('deletemd/<int:mid>',views.deletemd,name='deletemd'),
    path('deletemd2/<int:mid>',views.deletemd2,name='deletemd2'),
    path('updatemd/<int:pk>',views.updatemd,name='updatemd'),
]
