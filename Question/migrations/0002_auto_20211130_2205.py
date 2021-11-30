# Generated by Django 3.0.8 on 2021-11-30 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Question', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='questions',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='modified_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
