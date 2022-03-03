from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from Student.models import Other_info,  Course, Ugroup_learder, UGroup,  Univ_cours, Field, Material, Learning, Technology, Field_technology, Catgory, Subject, Admission, Univerisity, Post_message
from Student.decorators import un_lect

@un_lect
def lindex(request):
    return render(request, 'lecture/index.html')

def lsetting(request):
    id = request.user.id
    data = User.objects.filter(id = id).first()
    dat = Other_info.objects.filter(usrnam= data.username).first()
    print(dat)
    context = {'data':data, 'dat':dat}
    return render(request, 'lecture/setting.html', context)

def editsetting(request):
    id = request.user.id
    data = User.objects.filter(id = id).first()
    dat= Other_info.objects.filter( id= id).first()
    context = {'data':data, 'dat':dat}
    return render(request, 'lecture/Editsetting.html', context)

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
            Other_info.objects.create(User = data, usrnam =data.username,  bod = bod, gender = gender, location = location, phon_no = phon_no)
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
def eco_cours(request):
    cat = Catgory.objects.filter(category_nam = 'economice').first()
    data = Course.objects.filter(catgory=cat)
    context = {'data':data}
    return render(request, 'lecture/course.html', context)

def art_cours(request):
    cat = Catgory.objects.filter(category_nam='arts').first()
    data = Course.objects.filter(catgory=cat)
    context = {'data':data}
    return render(request, 'lecture/course.html', context)

def courses(request):
    data = Course.objects.all()
    context = {'data':data}
    return render(request, 'lecture/course.html', context)

def sci_cours(request):
    cat = Catgory.objects.filter(category_nam = 'science').first()
    data = Course.objects.filter(catgory=cat)
    context = {'data':data}
    return render(request, 'lecture/course.html', context)

def addcourse(request):
    data = Subject.objects.all()
    context = {'data':data}
    return render(request, 'lecture/addcoures.html', context)

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

        try:
            cat = Catgory.objects.create(category_nam=category)
        finally:
            AD =Admission.objects.filter(subject_id = sub.sub_id).first()
            ca = Catgory.objects.filter(category_nam=category).first()
            fi = Field.objects.filter(field_name=aplications1 ).first()
            ad = Admission.objects.filter(subject=sub).first()
            Course.objects.create(cours_name = name, year = year, catgory=ca, field =fi, admission =ad)
        return redirect('./courses')

def laddcourse(request):
    data = Subject.objects.all()
    context = {'data':data}
    return render(request, 'lecture/addcoures.html', context)

def lTechnology(request):
    return render(request, 'lecture/Technology.html')

def laddgroup(request):
    return render(request, 'lecture/addgroup.html')

def ladduser(request):
    return render(request, 'lecture/adduser.html')

def lcourses(request):
    return render(request, 'lecture/course.html')

def lgroupmessage(request):
    return render(request, 'lecture/groupmessage.html')

def lgroups(request):
    data = UGroup.objects.all()
    context = {'data':data}
    return render(request, 'lecture/groups.html', context)


def setting(request):
    data = User.objects.all()
    context = {'data':data}
    return render(request, 'lecture/user.html', context)

def announcemnt(request):
    data = Post_message.objects.all()
    context = {'data':data}
    return render(request, 'lecture/announcemnt.html', context)

def groupmessage(request, id):
    data = UGroup.objects.all()
    context = {'data':data}
    return render(request, 'lecture/groupmessage.html', context)

def addpost(request):
    return render(request, 'lecture/addpost.html')

def process_post(request):
    if request.method =="POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        category = request.POST.get('category')
        us = request.user.id
        user = User.objects.filter(id = us).first()
        data_f = Post_message.objects.create(tittle= name, description =description, category= category, User= user)
    return redirect('./announcemnt')


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
    return render(request, 'lecture/editgroup.html', context)

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


def block_group(request, group_id):
    UGroup.objects.get(group_id= group_id).delete()
    return redirect('./groups')
