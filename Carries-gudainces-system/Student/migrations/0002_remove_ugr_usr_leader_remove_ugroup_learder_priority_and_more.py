# Generated by Django 4.0.1 on 2022-01-24 10:43

from django.conf import settings
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0013_role_task_given'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ugr_usr',
            name='leader',
        ),
        migrations.RemoveField(
            model_name='ugroup_learder',
            name='priority',
        ),
        migrations.AddField(
            model_name='ugr_usr',
            name='group_nam',
            field=models.ManyToManyField(to='Student.UGroup'),
        ),
        migrations.AddField(
            model_name='ugroup_learder',
            name='User',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ugroup_learder',
            name='permission',
            field=models.ManyToManyField(to='auth.Permission'),
        ),
        migrations.AlterField(
            model_name='image',
            name='photo',
            field=models.FileField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]),
        ),
        migrations.RemoveField(
            model_name='ugr_usr',
            name='User',
        ),
        migrations.AddField(
            model_name='ugr_usr',
            name='User',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
