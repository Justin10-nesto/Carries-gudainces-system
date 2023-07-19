from datetime import datetime
from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.core.validators import FileExtensionValidator
class Role(Group):
	class Meta:
		proxy = True
		app_label = 'auth'
		verbose_name = ('Role')

class Task_Given(Permission):
	class Meta:
		proxy = True
		app_label = 'auth'
		verbose_name = ('Task_Given')

	def __str__(self):
			return self.name

class Other_info(models.Model):
	id = models.AutoField(primary_key = True)
	username =models.CharField(max_length=255)
	User = models.OneToOneField(User, on_delete=models.CASCADE)
	bod = models.CharField(max_length=255)
	gender = models.BigIntegerField()
	location  = models.CharField(max_length=255)
	phon_no =models.BigIntegerField()

	def  __str__(self):
		return self.user

class Image(models.Model):
	id = models.AutoField(primary_key = True)
	User = models.OneToOneField(User, on_delete=models.CASCADE)
	photo= models.FileField(upload_to='images/',validators =[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])

	def __str__(self):
		return self.name + ": " + str(self.imagefile)


class Field(models.Model):
	field_id = models.AutoField(primary_key = True)
	field_name = models.CharField(max_length=255)

	def  __str__(self):
		return self.field_name

class Material(models.Model):
	id = models.AutoField(primary_key=True)
	book_tittle = models.CharField(max_length=255)
	book_author = models.CharField(max_length=255)
	book_edition = models.CharField(max_length=255)
	book_year = models.CharField(max_length=255)
	url = models.CharField(max_length=255)

class Learning(models.Model):
	id = models.AutoField(primary_key=True)
	topic =models.CharField(max_length = 255)
	Material= models.ForeignKey(Material, on_delete=models.CASCADE)

class Technology(models.Model):
	tchnology_id = models.AutoField(primary_key=True)
	tchnology_name = models.CharField(max_length=255)
	learning= models.ForeignKey(Learning, on_delete=models.CASCADE)
	def  __str__(self):
    		return self.tchnology_name

class Field_technology(models.Model):
	id =models.AutoField(primary_key = True)
	Technology= models.ForeignKey(Technology, on_delete=models.CASCADE)
	Field= models.ForeignKey(Field, on_delete=models.CASCADE)

class Catgory(models.Model):
	catgory_id = models.AutoField(primary_key =True)
	category_nam = models.CharField(max_length=255, unique= True)

class Level(models.Model):
	id = models.AutoField(primary_key =True)
	name = models.CharField(max_length=255)

class Subject(models.Model):
	sub_id = models.AutoField(primary_key =True)
	subject_name = models.CharField(max_length=255)
	class_lvl = models.ForeignKey(Level, on_delete=models.CASCADE)

	def __str__(self):
		return self.subject_name

class Admission(models.Model):
	admission_id = models.AutoField(primary_key= True)
	marks = models.CharField(max_length=255)
	subject = models.ForeignKey(Subject, on_delete=models.CASCADE)


class Univerisity(models.Model):
		university_id = models.AutoField(primary_key=True)
		university_name = models.CharField(max_length=255)
		total_coursers = models.BigIntegerField()
		no_lectures = models.BigIntegerField()


		def  __str__(self):
			return self.university_name

class Course(models.Model):
	course_id = models.AutoField(primary_key=True)
	cours_name = models.CharField(max_length=255)
	year = models.IntegerField()
	catgory = models.ForeignKey(Catgory, on_delete=models.CASCADE)
	field = models.ForeignKey(Field, on_delete=models.CASCADE)
	admission = models.ForeignKey(Admission, on_delete=models.CASCADE)
	def  __str__(self):
		return self.cours_name


class Univ_cours(models.Model):
	univ_course_id = models.AutoField(primary_key=True)
	course_id = models.IntegerField()
	university_id= models.IntegerField()
	uni_cours = models.ForeignKey(Univerisity, on_delete=models.CASCADE)
	uni_cours = models.ForeignKey(Course, on_delete=models.CASCADE)

	def __str__(self):
		return self.univ_course_id

class Post_message(models.Model):
	post_id=models.AutoField(primary_key=True)
	tittle = models.CharField(max_length=255)
	description =  models.TextField()
	category = models.CharField(max_length=255)
	User = models.ForeignKey(User, on_delete=models.CASCADE)
	time_post = models.CharField(max_length=255, default=datetime.now())


# model for designing chat group
class Ugroup_learder(models.Model):
	id =models.AutoField(primary_key=True)
	position = models.CharField(max_length=255)
	User = models.ManyToManyField(User)
	permission= models.ManyToManyField(Permission)


class UGroup(models.Model):
	group_id=models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	description =  models.CharField(max_length=255)
	category = models.CharField(max_length=255)
	leader = models.CharField(max_length=255, default = "1")

class UserGroup(models.Model):
	us_group_id =models.AutoField(primary_key=True)
	User = models.ForeignKey(User, on_delete=models.CASCADE)
	group = models.ForeignKey(UGroup, on_delete=models.CASCADE)
	msg = models.TextField()

class Ugr_usr(models.Model):
	id =models.AutoField(primary_key= True)
	User = models.ManyToManyField(User)
	group_nam = models.ManyToManyField(UGroup)
