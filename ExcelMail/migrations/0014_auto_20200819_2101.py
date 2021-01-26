# Generated by Django 2.2.5 on 2020-08-19 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ExcelMail', '0013_auto_20200614_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_feedback',
            name='Communication_LD',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('VeryGood', 'VeryGood'), ('Good', 'Good'), ('Average', 'Average'), ('Poor', 'Poor')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='teacher_feedback',
            name='Laboratory_LD',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('VeryGood', 'VeryGood'), ('Good', 'Good'), ('Average', 'Average'), ('Poor', 'Poor')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='teacher_feedback',
            name='Online_Class_LD',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('VeryGood', 'VeryGood'), ('Good', 'Good'), ('Average', 'Average'), ('Poor', 'Poor')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='teacher_feedback',
            name='Study_Material_LD',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('VeryGood', 'VeryGood'), ('Good', 'Good'), ('Average', 'Average'), ('Poor', 'Poor')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='teacher_feedback',
            name='Teaching_LD',
            field=models.CharField(choices=[('Excellent', 'Excellent'), ('VeryGood', 'VeryGood'), ('Good', 'Good'), ('Average', 'Average'), ('Poor', 'Poor')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='teacher_feedback',
            name='interaction',
            field=models.CharField(choices=[('Affectionate', 'Affectionate'), ('Friendly', 'Friendly'), ('Formal', 'Formal'), ('Less concerned', 'Less concerned')], max_length=20, null=True),
        ),
    ]