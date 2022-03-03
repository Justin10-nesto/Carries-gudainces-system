from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib import messages
from Student.decorators import un_stud,allowed_roles
from Student.models import Other_info, Post_message,  Course, Ugroup_learder, UGroup,  Univ_cours, Field, Material, Learning, Technology, Field_technology, Catgory, Subject, Admission, Univerisity
import re

def register_user(request):
    if request.method =='POST':
        last_name =request.POST.get('last_name')
        first_name = request.POST.get('first_name')
        username =request.POST.get('username')
        password =request.POST.get('password')
        password1 =request.POST.get('password1')
        email = request.POST.get('email')
        Usergr = request.POST.get('Usergr')
        bod = request.POST.get('bod')
        gender = request.POST.get('gender')
        location = request.POST.get('location')
        phon_no = request.POST.get('phon_no')

        flag = 0
        special_sign_text1= [',. ~!@#$%^&*()_=+<>/[]{}']

        special_sign = [',', '.', ' ', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '=','+', '<', '>', '/', '[', ']', "{", '}']
        for  i in first_name:
            if i in range(-1,10):
                flag = -1
                messages.info(request, "first name must not contain a numerical")

        for  i in first_name:
            if i in special_sign:
                flag = -1
                messages.info(request, f"first name must not contain a {i}")

        for  i in last_name:
            if i in range(-1,10):
                flag = -1
                messages.info(request, "last name must not contain a numerical")

        for  i in last_name:
            if i in special_sign:
                flag = -1
                messages.info(request, f"last name must not contain a {i}")

        if len(phon_no) < 10:
            flag = -1
            messages.info(request, "phone number must be 10 numbers ")

        email_with_at = email.split('@')
        if len(email_with_at) < 2:
            flag = -1
            messages.info(request, "email must contain an @ sign")

        try:
            checking_dot= email_with_at[1].split('.')
            if len(checking_dot) < 2:
                flag = -1
                messages.info(request, "email must contain an . sign")
        except:
            flag = -1
            messages.info(request, "invalid email address")

        if password == password1:
            if len(password) < 7:
                    flag = -1
                    messages.info(request, "Weak password must contain a atleast 8 characters")

            else:
                flag = 0
        else:
            flag = -1
            messages.info(request, "two password doesn't match use corrct password")

        if flag == -1:
            return redirect('register')
        else:
            userdata = User.objects.create_user(
                username=username,
                email = email,
                password = password
                    )
            userdata.last_name= last_name
            userdata.first_name= first_name
            userdata.save()
            group = Group.objects.get(name =Usergr)
            user = User.objects.get(username =username)
            user.groups.add(group)
            Other_info.objects.create(User = user, username =username,  bod = bod, gender = gender, location = location, phon_no = phon_no)


        return redirect('/')

def loginauth(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password =request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request, user)
                if request.user.is_superuser:
                    return redirect('/admin')
                else:
                    return redirect('adminr/index')
            else:
                messages.info(request, "this account is blocked")
                return redirect('/')
        else:
            messages.info(request, "incorrect username or password")
            return redirect('/')

def logout_data(request):
    logout(request)
    return redirect('/')



def changepassform(request, id):
	data = User.objects.filter(id = int(id)).all()
	context = {'data':data}
	return render(request, 'password.html', context)

@un_stud
def student_index(request):
    return render(request, 'Student/index2.html')

def loginm(request):
    return render(request, 'Student/login.html')

def register(request):
    group = Group.objects.all()
    context = {'group':group}
    return render(request, 'Student/REG.html', context)

def courses(request):
	data = Course.objects.all()
	context = {'data':data}
	return render(request, 'Student/courses.html', context)


def sci_cours(request):
    cat = Catgory.objects.filter(category_nam = 'science').first()
    data = Course.objects.filter(catgory=cat)
    context = {'data':data}
    return render(request, 'Student/courses.html', context)

def eco_cours(request):
    cat = Catgory.objects.filter(category_nam = 'economice').first()
    data = Course.objects.filter(catgory=cat)
    context = {'data':data}
    return render(request, 'Student/courses.html', context)

def art_cours(request):
    cat = Catgory.objects.filter(category_nam='arts').first()
    data = Course.objects.filter(catgory=cat)
    context = {'data':data}
    return render(request, 'Student/courses.html', context)

def courses_messages(request):
    return render(request, 'Student/group_messages.html')

def courses_update(request):
	data = Post_message.objects.all()
	context = {'data':data}
	return render(request, 'Student/updates.html', context)


def setting(request):
    id = request.user.id
    data = User.objects.filter(id = id).first()
    dat = Other_info.objects.filter(usrnam= data.username).first()
    print(dat)
    context = {'data':data, 'dat':dat}
    return render(request, 'Student/setting.html', context)

def editsetting(request):
    id = request.user.id
    data = User.objects.filter(id = id).first()
    dat= Other_info.objects.filter( id= id).first()
    context = {'data':data, 'dat':dat}
    return render(request, 'Student/Editsetting.html', context)

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
