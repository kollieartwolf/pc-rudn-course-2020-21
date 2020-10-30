# Generated by Django 3.1.2 on 2020-10-08 11:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0008_auto_20201006_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='status',
            field=models.CharField(choices=[('writing', 'В процессе'), ('to_review', 'Требует проверки'), ('opened', 'Открыта')], default='writing', max_length=9),
        ),
        migrations.AlterField(
            model_name='section',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
