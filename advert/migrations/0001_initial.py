# Generated by Django 2.1.8 on 2019-05-10 08:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_title', models.CharField(max_length=250)),
                ('ISBN', models.CharField(blank=True, default='', max_length=100)),
                ('price', models.PositiveSmallIntegerField()),
                ('authors', models.CharField(blank=True, default='', max_length=250)),
                ('edition', models.CharField(blank=True, default='', max_length=100)),
                ('condition', models.CharField(choices=[('1', 'Nyskick'), ('2', 'Mycket gott skick'), ('3', 'Gott skick'), ('4', 'Hyggligt skick'), ('5', 'Dåligt skick'), ('6', 'Ej angett')], default='6', max_length=1)),
                ('state', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], default='A', max_length=1)),
                ('transaction_type', models.CharField(choices=[('S', 'Selling'), ('B', 'Buying')], default='S', max_length=1)),
                ('contact_info', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='adverts', to=settings.AUTH_USER_MODEL)),
                ('responder', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accepted_adverts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AdvertImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='ad_images')),
                ('advert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='image', to='advert.Advert')),
            ],
        ),
    ]
