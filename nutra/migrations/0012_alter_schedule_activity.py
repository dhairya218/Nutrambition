# Generated by Django 4.2.6 on 2023-11-04 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nutra', '0011_schedule_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='activity',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nutra.excercies'),
        ),
    ]
