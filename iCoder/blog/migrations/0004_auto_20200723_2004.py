# Generated by Django 3.0.5 on 2020-07-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200723_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
