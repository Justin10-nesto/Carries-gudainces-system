from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.loginm, name='loginm'),
path('admin/logout/', views.logout_data, name='logout'),

    path('logout_data', views.logout_data, name='logout_data'),
    path('loginauth', views.loginauth, name='loginauth'),
    path('register', views.register, name='register'),
    path('register_user', views.register_user, name='register_user'),
    path('student', views.student_index, name='sindex'),
    path('student/courses', views.courses, name='student_courses'),
    path('student/sci_cours', views.sci_cours, name = 'student_sci_cours'),
    path('student/eco_cours', views.eco_cours, name = 'student_eco_cours'),
    path('student/art_cours', views.art_cours, name = 'student_art_cours'),

    path('student/courses_messages', views.courses_messages, name='courses_messages'),
    path('student/courses_update', views.courses_update, name='courses_update'),
    path('student/setting', views.setting, name = 'student_setting'),
    path('student/editsetting', views.editsetting, name = 'student_editsetting'),
    path('student/process_user_photo', views.process_user_photo, name = 'student_process_user_photo'),
    path('student/process_user_info', views.process_user_info, name = 'student_process_user_info'),

]