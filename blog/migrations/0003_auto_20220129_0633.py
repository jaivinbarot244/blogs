# Generated by Django 3.2.8 on 2022-01-29 01:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='sno',
            new_name='post_id',
        ),
        migrations.RemoveField(
            model_name='post',
            name='Author',
        ),
        migrations.RemoveField(
            model_name='post',
            name='content',
        ),
        migrations.RemoveField(
            model_name='post',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='post',
            name='timestemp',
        ),
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
        migrations.AddField(
            model_name='post',
            name='chead0',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='post',
            name='chead1',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='post',
            name='chead2',
            field=models.CharField(default='', max_length=5000),
        ),
        migrations.AddField(
            model_name='post',
            name='head0',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='head1',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='head2',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='shop/images'),
        ),
        migrations.AddField(
            model_name='post',
            name='tilte',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]