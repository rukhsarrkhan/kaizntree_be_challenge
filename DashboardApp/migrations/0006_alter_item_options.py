# Generated by Django 5.0.1 on 2024-02-11 21:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("DashboardApp", "0005_alter_category_name_alter_tag_name"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="item",
            options={"ordering": ["id"]},
        ),
    ]
