# Generated by Django 4.0.3 on 2023-03-17 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greet', '0003_remove_greet_dohui_remove_greet_gyeongjun_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='greet',
            name='win',
            field=models.TextField(blank=True, null=True, verbose_name='최승호'),
        ),
    ]
