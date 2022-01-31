from django.urls import path
from school import views

urlpatterns=[
    path('login/',views.user_login,name='login'),
    path('signup/',views.user_signup,name='signup'),
    path('logout/',views.user_logout,name='logout'),
    path('details/',views.student_details,name='details'),
    path('create/',views.student_create,name='create'),
    path('update/<int:id>',views.student_update,name='update'),
    path('delete/<int:id>',views.student_delete,name='delete'),
]