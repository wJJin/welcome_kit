# Generated by Django 4.0.3 on 2023-02-27 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_student1_value1_user_student1_value2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='grade',
            field=models.CharField(choices=[('1학년', '1학년'), ('2학년', '2학년'), ('3학년', '3학년'), ('4학년', '4학년'), ('5학년', '5학년'), ('졸업생', '졸업생'), ('휴학', '휴학')], max_length=18, null=True, verbose_name='학년'),
        ),
        migrations.AlterField(
            model_name='user',
            name='leader',
            field=models.CharField(max_length=8, null=True, verbose_name='리더상'),
        ),
        migrations.AlterField(
            model_name='user',
            name='level',
            field=models.CharField(choices=[('2', 'LV2_아기사자'), ('1', 'LV1_운영진'), ('0', 'LV0_개발자')], default=2, max_length=5, verbose_name='등급'),
        ),
        migrations.AlterField(
            model_name='user',
            name='modifier',
            field=models.CharField(max_length=16, null=True, verbose_name='수식언'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student1',
            field=models.CharField(max_length=8, null=True, verbose_name='추천 동료1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student1_intro',
            field=models.TextField(max_length=256, null=True, verbose_name='추천 동료1 소개'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student1_value1',
            field=models.CharField(max_length=8, null=True, verbose_name='추천 키워드 1-1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student1_value2',
            field=models.CharField(max_length=8, null=True, verbose_name='추천 키워드 1-2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student1_value3',
            field=models.CharField(max_length=8, null=True, verbose_name='추천 키워드 1-3'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student2',
            field=models.CharField(max_length=8, null=True, verbose_name='추천 동료2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student2_intro',
            field=models.TextField(max_length=256, null=True, verbose_name='추천 동료2 소개'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student2_value1',
            field=models.CharField(max_length=8, null=True, verbose_name='추천 키워드 2-1'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student2_value2',
            field=models.CharField(max_length=8, null=True, verbose_name='추천 키워드 2-2'),
        ),
        migrations.AlterField(
            model_name='user',
            name='student2_value3',
            field=models.CharField(max_length=8, null=True, verbose_name='추천 키워드 2-3'),
        ),
        migrations.AlterField(
            model_name='user',
            name='track',
            field=models.CharField(choices=[('백엔드', '백엔드'), ('프론트엔드', '프론트엔드'), ('기획디자인', '기획디자인')], max_length=18, null=True, verbose_name='트랙'),
        ),
    ]
