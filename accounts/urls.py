from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('users/my-courses', views.EnrolledCoursesListView.as_view(), name='enrolled-courses'),
    path('users/my-courses/<slug:slug>/view', views.StartLessonView.as_view(), name='course-lessons'),
    path('users/my-courses/<slug:slug>/lessons/<int:id>', views.LessonView.as_view(), name='course-lessons-single'),
]
