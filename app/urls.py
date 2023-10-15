from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('registration/',views.registration,name='registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('student-information/', views.student_information, name='student_information'),
    path('student-marks/', views.student_marks, name='student_marks'),
    path('student-fees/', views.student_fees, name='student_fees'),
    path('student-attendance/', views.student_attendance, name='student_attendance'),
]