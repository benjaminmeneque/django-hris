# Generated by Django 4.1.7 on 2023-02-17 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employee", "0002_rename_lasstname_employee_lastname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], default="male", max_length=1
            ),
        ),
    ]
