
from django.urls import path, include
from . import views
urlpatterns = [
    path('adminr/index', views.index, name = 'index'),
    path('adminr/adduser', views.adduser, name = 'adduser'),

    path('adminr/courses', views.courses, name = 'acourses'),
    path('adminr/addcourse', views.addcourse, name = 'addcourse'),
    path('adminr/sci_cours', views.sci_cours, name = 'sci_cours'),
    path('adminr/eco_cours', views.eco_cours, name = 'eco_cours'),
    path('adminr/art_cours', views.art_cours, name = 'art_cours'),
    path('adminr/process_cours', views.process_cours, name = 'aprocess_cours'),

    path('adminr/announcemnt', views. announcemnt, name = 'aannouncemnt'),
    path('adminr/addpost', views. addpost, name = 'addpost'),
    path('adminr/process_post', views. process_post, name = 'process_post'),
    path('adminr/editpost/<slug:id>', views. editpost, name = 'editpost'),

path('adminr/change_editted_post/<slug:id>', views. change_editted_post, name = 'change_editted_post'),
    path('adminr/delete_post/<slug:id>', views. delete_post, name = 'delete_post'),

    path('adminr/assign_role/<slug:id>', views.assign_role, name = 'assign_role'),
    path('adminr/setting/', views.setting, name = 'setting'),
    path('adminr/editsetting', views.editsetting, name = 'editsetting'),
    path('adminr/process_user_photo', views.process_user_photo, name = 'process_user_photo'),
    path('adminr/process_user_info', views.process_user_info, name = 'process_user_info'),

    path('adminr/viewuser', views.viewuser, name = 'userreq'),
    path('adminr/assignrol/<slug:id>', views.assignrol, name = 'assignrol'),
    path('adminr/edituserinfo/<slug:user_id>', views.edituserinfo, name = 'edituserinfo'),
    path('adminr/updateuser/<slug:user_id>', views.updateuser, name = 'updateuser'),
    path('adminr/blockuser/<slug:user_id>', views.blockuser, name = 'blockuser'),
    path('adminr/deleteuser/<slug:user_id>', views.deleteuser, name = 'deleteuser'),

    path('adminr/role', views.role, name = 'role'),
    path('adminr/add_role', views.add_role, name = 'add_role'),
    path('adminr/role_assign_form/<slug:rol_id>', views.role_assign_form, name = 'role_assign_form'),
    path('adminr/Process_role', views.Process_role, name = 'Process_role'),
    path('adminr/delete_role/<slug:role_id>', views.delete_role, name = 'delete_role'),
    path('adminr/view_role_Permission/<slug:role_id>', views.view_role_Permission, name = 'view_role_Permission'),
    path('adminr/assign_role_Permission/<slug:role_id>', views.assign_role_Permission, name = 'assign_role_Permission'),
    path('adminr/updat_role_Permission/<slug:role_id>', views.updat_role_Permission, name = 'update_role_Permission'),
    path('adminr/remov_permision/<slug:role_id>', views.remov_permision, name = 'remov_permision'),
    path('adminr/remove_role_Permission/<slug:role_id>', views.remove_role_Permission, name = 'remove_role_Permission'),

    path('adminr/groups', views.groups, name = 'groups'),
    path('adminr/process_adding_group', views.process_adding_group, name = 'process_adding_group'),

    path('adminr/process_groups', views.process_groups, name = 'process_groups'),
    path('adminr/addgroup', views.addgroup, name = 'addgroup'),
    path('adminr/delete_group/<slug:group_id>', views.delete_group, name = 'delete_group'),
    path('adminr/edittinggroup/<slug:id>', views.edittinggroup, name = 'edittinggroup'),
    path('adminr/update_groups/<slug:id>', views.update_groups, name = 'update_groups'),

    path('adminr/send_text_group/<slug:group_id>', views.send_text_group, name = 'send_text_group'),
    path('adminr/groupmessage/<slug:id>', views.groupmessage, name = 'groupmessage'),
 path('uploadimage/', views.AddMediaView.as_view(), name='uploadimg_url'),

]