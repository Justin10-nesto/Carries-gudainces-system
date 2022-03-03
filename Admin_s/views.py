from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group, Permission
from Student.decorators import un_admin
from django.contrib import messages
from Student.models import Other_info, Image,  Course,UserGroup, UserGroup, Ugroup_learder, UGroup,  Univ_cours, Field, Material, Learning, Technology, Field_technology, Catgory, Subject, Admission, Univerisity, Post_message

def index(request):
    data = request.user.get_all_permissions()
    context= {'data':data}
    return render(request, 'Admin_s/index2.html', context)

def setting(request):
    id = request.user.id
    data = User.objects.filter(id = id).first()
    dat = Other_info.objects.filter(username = data.username).first()
    context = {'data':data, 'dat':dat, }
    return render(request, 'Admin_s/setting.html', context)

def editsetting(request):
    id = request.user.id
    data = User.objects.filter(id = id).first()
    dat= Other_info.objects.filter( id= id).first()
    context = {'data':data, 'dat':dat, }
    return render(request, 'Admin_s/Editsetting.html', context)

def process_user_photo(request):
    if request.method == "POST":
        photo = request.POST.get('photo')
        us = request.user.username
        data = User.objects.filter(username = us).first()
        Image.objects.create(User = data, photo=photo)
    return redirect('./setting')

def process_user_info(request):
    if request.method == "POST":
        Us = request.user.id
        data = User.objects.filter(id= Us).first()
        bod = request.POST.get('bod')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        phon_no = request.POST.get('phon_no')
        last_name =request.POST.get('lname')
        first_name = request.POST.get('fname')
        username =request.POST.get('uname')
        password =request.POST.get('password1')
        password2 =request.POST.get('password2')
        email = request.POST.get('email')
        try:
            Other_info.objects.create(User = data, username =data.username,  bod = bod, gender = gender, location = location, phon_no = phon_no)
        except:
            dat1 = Other_info.objects.filter(id = id).first()
            dat1.User = data
            dat1.bod = bod
            dat1.gender = gender
            dat1.location = location
            dat1.phon_no = phon_no
        finally:
            if password == password2:
                data = User.objects.filter(id = Us).first()
                data.username=username
                data.email = email
                data.set_password(password)
                data.last_name= last_name
                data.first_name= first_name
                data.save()
        return redirect('./setting')

def assignrol(request, id):
    user = User.objects.filter(id = id)
    group = Group.objects.all()
    cont ={'data':user, 'group':group, }
    return render(request, 'Admin_s/assignrol.html', cont)

def assign_role(request, id):
    if request.method == "POST":
        last_name =request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        username =request.POST.get('username')
        password =request.POST.get('password1')
        email = request.POST.get('email')
        Usergr = request.POST.get('Usergr')
        user = User.objects.filter(id = id)
        group = Group.objects.get(name =Usergr)
        user = User.objects.get(username =username)
        user.groups.add(group)
    return redirect('./viewuser')

def edituserinfo(request, user_id):
    user = User.objects.filter(id = user_id).first()
    group = Group.objects.all()
    context = {'user':user, 'group':group, }
    return render(request, 'Admin_s/edituser.html', context)

def updateuser(request, user_id):
    if request.method =='POST':
        last_name =request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        username =request.POST.get('username')
        password =request.POST.get('password1')
        email = request.POST.get('email')
        Usergr = request.POST.get('Usergr')
        userdata = User.objects.filter(id =user_id).first()
        userdata.username=username
        userdata.email = email
        userdata.set_password(password)
        userdata.last_name= last_name
        userdata.first_name= first_name
        userdata.save()
        group = Group.objects.get(name = Usergr)
        user = User.objects.get(username =username)
        user.groups.add(group)
    return redirect('./viewuser')


def blockuser(request, user_id):
    user = User.objects.filter(id = user_id).first()
    user.is_active =0
    user.save()
    return redirect('./viewuser')

def deleteuser(request, user_id):
    User.objects.filter(id = user_id).delete()
    return redirect('./viewuser')

def courses(request):
    data = Course.objects.all()
    context = {'data':data, }
    return render(request, 'Admin_s/course.html', context)

def sci_cours(request):
    cat = Catgory.objects.filter(category_nam = 'science').first()
    data = Course.objects.filter(catgory=cat)
    context = {'data':data, }
    return render(request, 'Admin_s/course.html', context)

def eco_cours(request):
    cat = Catgory.objects.filter(category_nam = 'economice').first()
    data = Course.objects.filter(catgory=cat)
    context = {'data':data, }
    return render(request, 'Admin_s/course.html', context)

def art_cours(request):
    cat = Catgory.objects.filter(category_nam='arts').first()
    data = Course.objects.filter(catgory=cat)
    context = {'data':data, }
    return render(request, 'Admin_s/course.html', context)

def addcourse(request):
    data = Subject.objects.all()
    context = {'data':data, }
    return render(request, 'Admin_s/addcoures.html', context)

def process_cours(request):
    if request.method =="POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        aplications1 = request.POST.get('aplications1')
        aplications2 = request.POST.get('aplications2')
        subjects = request.POST.get('subjects')
        marks = request.POST.get('marks')
        year = request.POST.get('years')
        sub =Subject.objects.filter(subject_name = subjects).first()
        data_f = Field.objects.create(field_name=aplications1)
        data_f1 = Field.objects.create(field_name=aplications2)
        adm = Admission.objects.create(subject=sub, marks=marks)

        AD =Admission.objects.filter(subject_id = sub.sub_id).first()
        ca = Catgory.objects.filter(category_nam=category).first()
        fi = Field.objects.filter(field_name=aplications1 ).first()
        ad = Admission.objects.filter(subject=sub).first()
        Course.objects.create(cours_name = name, year = year, catgory=ca, field =fi, admission =ad)
        return redirect('./courses')

def announcemnt(request):
    data = Post_message.objects.all()
    context = {'data':data, }
    return render(request, 'Admin_s/announcemnt.html', context)

def addpost(request):
    context = {}
    return render(request, 'Admin_s/addpost.html', context)

def process_post(request):
    if request.method =="POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        us = request.user.id
        print(name, description, category)
        user = User.objects.filter(id = us).first()
        Post_message.objects.create(tittle= name, description =description, category= category, User= user)
    return redirect('./announcemnt')


def editpost(request, id):
    data = Post_message.objects.filter(post_id = id)
    context = {'data':data}
    return render(request, 'Admin_s/editpost.html', context)

def change_editted_post(request, id):
    if request.method =="POST":
        name = request.POST.get('name ')
        description = request.POST.get('description')
        category = request.POST.get('category')
        us = request.user.id
        user = User.objects.filter(id = us).first()
        data = Post_message.objects.filter(post_id = id)
        data.tittle= name
        data.description =description
        data.category= category
        data.User= user
        data.save()

    return redirect('./announcemnt')

def delete_post(request, id):
    data = Post_message.objects.filter(post_id = id).delete()
    return redirect('../announcemnt')


def addgroup(request):
    context = {}
    return render(request, 'Admin_s/addgroup.html', context)

def adduser(request):
    group = UGroup.objects.all()
    us = User.objects.all()
    context = {'group':group, 'us':us}
    return render(request, 'Admin_s/adduser.html', context)

def process_adding_group(request):
    if request.method =="POST":
        group = request.POST.get('group')
        user = request.POST.get('user')
        group_chat = UGroup.objects.filter(group_id = group).first()
        user_group = User.objects.filter(id = user).first()
        try:
            Ugr_usr.User.add(user)
            Ugr_usr.group_nam.add(user_group)

        finally:
            return redirect('./groups')



def groupmessage(request, id):
    group = UGroup.objects.filter(group_id = id).first()
    messags = UserGroup.objects.all()
    user = request.user.username
    context = {'group':group, 'user':user, 'messags':messags, }
    return render(request, 'Admin_s/groupmessage.html', context)

def groups(request):
    data = UGroup.objects.all()
    context = {'data':data, }
    return render(request, 'Admin_s/groups.html', context)

def process_groups(request):
    if request.method =="POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        UGroup.objects.create(name=name, category= category, description=description, )
        return redirect('./groups')

def edittinggroup(request, id):
    data = UGroup.objects.get(group_id= id)
    context = {'data':data}
    return render(request, 'Admin_s/editgroup.html', context)

def update_groups(request, id):
    if request.method =="POST":
        name = request.POST.get('name')
        category = request.POST.get('category')
        description = request.POST.get('description')
        data = UGroup.objects.get(group_id= id)
        data.name = name
        data.description = description
        data.category = category
        data.save()
    return redirect('../groups')

def delete_group(request, group_id):
    UGroup.objects.filter(group_id= group_id).delete()
    return redirect('./groups')

def block_group(request, group_id):
    UGroup.objects.get(group_id= group_id).delete()
    return redirect('./groups')

def send_text_group(request, group_id):
    if request.method =="POST":
        msg = request.POST.get('message')
        user_id = request.user.id
        group = UGroup.objects.get(group_id= group_id)
        user = User.objects.filter(id = user_id).first()
        UserGroup.objects.create(User = user, group = group, msg= msg )
    return redirect('groupmessage', group.group_id)


def viewuser(request):
    data = User.objects.all()
    cont = {'data': data,}
    return render(request, 'Admin_s/user.html', cont)

def role(request):
    data = Group.objects.all()
    cont = {'data': data, }
    return render(request, 'Admin_s/role.html', cont)

def add_role(request):
    data = Permission.objects.all()
    cont = {'data': data, }
    return render(request, 'Admin_s/addrol.html', cont)

def Process_role(request):
    if request.method == "POST":
        name = request.POST.get('name')
        role = Group.objects.create(name =name)
    return redirect('./role')


def role_assign_form(request, rol_id):
    group = Group.objects.filter(id = rol_id).first()
    data = Permission.objects.all()
    cont = {'group': group, 'data':data, }
    return render(request, 'Admin_s/role_assign_form.html', cont)


def delete_role(request,role_id):
    data = Group.objects.filter(id =role_id).delete()
    return redirect('./role')

def view_role_Permission(request, role_id):
    group = Group.objects.filter(id = role_id).first()
    data = Permission.objects.all()
    cont = {'group': group, 'data':data, }
    return render(request, 'Admin_s/view_role_Permission.html', cont)

def updat_role_Permission(request, role_id):
    group = Group.objects.filter(id = role_id).first()
    data = Permission.objects.all()
    data_prm =[]
    for i in data:
        data_prm.append(i.name)
    for datpr in  data_prm:
        permission = request.POST.get(datpr)
        if permission != "":
            perm = Permission.objects.get(name = datpr )
            role = Group.objects.get(id = role_id)
            role.permissions.add(perm)
    return redirect('./role')

def remov_permision(request, role_id):
    group = Group.objects.filter(id = role_id).first()
    data = Permission.objects.all()
    cont = {'group': group, 'data':data, }
    return render(request, 'Admin_s/remove_role_Permission.html', cont)

def remove_role_Permission(request, role_id):
    group = Group.objects.filter(id = role_id).first()
    data = Permission.objects.all()
    data_prm =[]
    for i in data:
        data_prm.append(i.name)
    for datpr in  data_prm:
        permission = request.POST.get(datpr)
        if permission != "":
            perm = Permission.objects.get(name = datpr )
            role = Group.objects.get(id = role_id)
            role.permissions.remove(perm)
    return redirect('./role')

def assign_role_Permission(request, role_id):
    group = Group.objects.filter(id = role_id).first()
    data = Permission.objects.all()
    cont = {'group': group, 'data':data, }
    return render(request, 'Admin_s/assign_rol_prm.html', cont)

from django.views.generic.edit import CreateView

class AddMediaView(CreateView):
    model = Image
    fields ="__all__"
    template_name = 'admin/uploadimg.html'

    def get_success_url(self):
        return reverse('media_url')

