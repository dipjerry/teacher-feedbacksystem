# Generated by Django 2.2.5 on 2020-08-19 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelMail', '0014_auto_20200819_2101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher_feedback',
            name='Branch',
            field=models.CharField(max_length=35, null=True),
        ),
        migrations.AlterField(
            model_name='teacher_feedback',
            name='Subject_Title',
            field=models.CharField(max_length=75, null=True),
        ),
    ]