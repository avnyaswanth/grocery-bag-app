# Generated by Django 3.2.7 on 2021-09-22 18:49

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
            name='GroceryItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemName', models.CharField(max_length=100)),
                ('itemQuantity', models.IntegerField()),
                ('flag', models.CharField(choices=[('PENDING', 'PENDING'), ('BOUGHT', 'BOUGHT'), ('NOTAVAILABLE', 'NOT AVAILABLE')], default='PENDING', max_length=20)),
                ('dateAdded', models.DateField()),
                ('owner', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
