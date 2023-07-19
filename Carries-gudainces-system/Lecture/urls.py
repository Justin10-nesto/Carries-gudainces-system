from django.urls import path, include
from . import views
urlpatterns = [
path('lecture/index', views.lindex, name = 'lindex'),
 path('lecture/setting', views.lsetting, name = 'lecture_setting'),
 path('lecture/editsetting', views.editsetting, name = 'lecture_editsetting'),
 path('lecture/process_user_photo', views.process_user_photo, name = 'lecture_process_user_photo'),
 path('lecture/process_user_info', views.process_user_info, name = 'lecture_process_user_info'),

 path('lecture/addcourse', views.laddcourse, name = 'lecture_addcourse'),
 path('lecture/addgroup', views.laddgroup, name = 'lecture_addgroup'),
 path('lecture/Technology', views.lTechnology, name = 'lecture_Technology'),
 path('lecture/adduser', views.ladduser, name = 'lecture_adduser'),
 path('lecture/groupmessage', views.lgroupmessage, name = 'lecture_groupmessage'),

 path('lecture/courses', views.lcourses, name = 'lecture_courses'),
 path('lecture/addcourse', views.addcourse, name = 'lecture_addcourse'),
 path('lecture/sci_cours', views.sci_cours, name = 'lecture_sci_cours'),
 path('lecture/eco_cours', views.eco_cours, name = 'lecture_eco_cours'),
 path('lecture/art_cours', views.art_cours, name = 'lecture_art_cours'),
 path('lecture/process_cours', views.process_cours, name = 'lecture_process_cours'),

 path('lecture/announcemnt', views. announcemnt, name = 'lecture_aannouncemnt'),
 path('lecture/addpost', views. addpost, name = 'lecture_addpost'),
path('lecture/process_post', views. process_post, name = 'lecture_process_post'),
path('lecture/setting', views.setting, name = 'lecture_setting'),

 path('lecture/groups', views.lgroups, name = 'lecture_groups'),
path('lecture/edittinggroup/<slug:id>', views.edittinggroup, name = 'lecture_edittinggroup'),
 path('lecture/update_groups/<slug:id>', views.update_groups, name = 'lecture_update_groups'),
path('lecture/groupmessage/<slug:id>', views.groupmessage, name = 'lecture_groupmessage'),
 path('lecture/process_groups', views.process_groups, name = 'lecture_process_groups'),

 ]
