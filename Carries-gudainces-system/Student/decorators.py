from django.shortcuts import redirect
from django.http import HttpResponse

def un_admin(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated and request.user.is_active:
			if request.user.is_superuser == 1:
				return redirect('/admin')
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group == 'Student':
				return redirect('student')
			elif group == 'Lecture':
				return redirect('lecture/index')
			elif group == 'Adminr':
				return view_func(request, *args, **kwargs)
		else:
			return redirect('/')
	return wrapper_func

def un_stud(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated and request.user.is_active:
			if request.user.is_superuser == 1:
				return redirect('/admin')
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group == 'Student':
				return view_func(request, *args, **kwargs)
			elif group == 'Lecture':
				return redirect('lecture/index')
			elif group == 'Adminr':
				return redirect('adminr/index')
		else:
			return redirect('/')
	return wrapper_func

def un_lect(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_authenticated and request.user.is_active:
			if request.user.is_superuser == 1:
				return redirect('/admin')
			if request.user.groups.exists():
				group = request.user.groups.all()[0].name
			if group == 'Student':
				return redirect('student')
			elif group == 'Lecture':
				return view_func(request, *args, **kwargs)
			elif group == 'Adminr':
				return redirect('adminr/index')
		else:
			return redirect('/')
	return wrapper_func


def allowed_roles(roles):
	def role(view_func):
		def wrapper_func(request, *args, **kwargs):
			group = None
			if request.user.is_authenticated and request.user.is_active:
				if request.user.groups.exists():
					group = request.user.groups.all()[0].name
				if group == 'Student':
					if group == roles[0]:
						return view_func(request, *args, **kwargs)
					elif group == 'Lecture':
						return redirect('lecture/index')
					elif group == 'Adminr':
						return redirect('adminr/index')

				if group == 'Lecture':
					if group == roles[0]:
						return view_func(request, *args, **kwargs)
					elif group == 'Adminr':
						return redirect('adminr/index')
					elif group == 'Student':
						return redirect('student')


				elif group == 'Adminr':
					if group == roles[0]:
						return view_func(request, *args, **kwargs)
					elif group == 'Lectre':
    						return redirect('lecture/index')
					elif group == 'Student':
						return redirect('student')

				else:
					return HttpResponse('you are not authorized')
			else:
				return redirect('/')
		return wrapper_func
	return role

