# Generated by Django 4.2.4 on 2023-09-08 18:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pereval', '0003_alter_users_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perevaladded',
            name='images',
        ),
        migrations.AddField(
            model_name='images',
            name='pereval',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='pereval.perevaladded'),
        ),
    ]
