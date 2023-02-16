# Generated by Django 4.1.5 on 2023-02-10 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_date_question_choice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='question',
        ),
        migrations.AddField(
            model_name='choice',
            name='choices',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='choices', to='albums.question'),
        ),
    ]
