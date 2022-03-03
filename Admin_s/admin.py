from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, Group, Permission
from Student.models import Other_info,  Course, Ugroup_learder, UGroup, Level,  Univ_cours, Field, Material, Learning, Technology, Field_technology, Catgory, Subject, Admission, Univerisity, Post_message


admin.site.site_header = 'Carrier Guidance System admin'
admin.site.site_title = 'Carrier Guidance System admin'
admin.site.site_url = 'http://localhost:8000'
admin.site.index_title = 'Carrier Guidance System administration'

class Other_infoAdmin(admin.ModelAdmin):
    list_display = ['id','username','phon_no', 'location', 'gender', 'bod']
    list_filter = ['id','username']
    list_per_page = 10

class FieldAdmin(admin.ModelAdmin):
    list_display = ['field_id','field_name']
  #  list_filter = ['field_name']
    search_fields = ['field_name']
    list_display_links = None
    actions_on_bottom = True
    actions_on_top = False
    list_per_page = 10

    fieldsets = [
        ['Field Information', {
            'fields': ['field_name']
            }],
    ]


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'list_of_names', 'username', 'email', 'groupsdata', 'is_active']
    def list_of_names(self, obj):
        return ("%s" % ' '.join([obj.first_name, obj.last_name ]))
    list_of_names.short_description = 'fully name'

    def groupsdata(self, obj):
        return ("%s" % ' '.join([ gr.name for gr in obj.groups.all() ]))
    groupsdata.short_description = 'Role'

    actions_on_bottom = True
    actions_on_top = False
    list_per_page = 10


class GroupAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class LvlAdmin(admin.ModelAdmin):
    list_display = ['id','name']

class AdmissionAdmin(admin.ModelAdmin):
    list_display = ['admission_id','marks', 'subjectdata']

    def subjectdata(self, obj):
        return ("%s" % ' '.join([ obj.subject.subject_name]))
    subjectdata.short_description = 'Subject'

    def subjectdata(self, obj):
        return ("%s" % ' '.join([ obj.subject.subject_name]))
    subjectdata.short_description = 'Subject'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Group, GroupAdmin)
admin.site.register(Other_info, Other_infoAdmin)
admin.site.register(Field, FieldAdmin)
admin.site.register(Technology)
admin.site.register(Subject)
admin.site.register(Post_message)
admin.site.register(Catgory)
admin.site.register(Learning)
admin.site.register(Univerisity)
admin.site.register(Admission, AdmissionAdmin)
admin.site.register(Field_technology)
admin.site.register(Material)
admin.site.register(Level, LvlAdmin)
