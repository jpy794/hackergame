# Generated by Django 2.1.12 on 2019-10-11 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('submission', '0003_submission_group'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='submission',
            options={'default_permissions': (), 'permissions': [('full', '管理提交记录'), ('view', '查看提交记录')]},
        ),
    ]
