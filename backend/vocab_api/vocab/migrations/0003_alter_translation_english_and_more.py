# Generated by Django 5.1.5 on 2025-02-01 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vocab', '0002_translation_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translation',
            name='english',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='maguindanaon',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
