# Generated by Django 3.0.8 on 2021-11-30 14:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Create Date')),
                ('modify_date', models.DateTimeField(auto_now=True, null=True, verbose_name='Modify Date')),
                ('question', models.CharField(blank=True, help_text='Question', max_length=1000, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='attachments')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_user', to=settings.AUTH_USER_MODEL)),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mentor', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modified_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
