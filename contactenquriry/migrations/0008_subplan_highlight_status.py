# Generated by Django 5.0.1 on 2024-03-15 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactenquriry', '0007_subplan_subscriptionplan_remove_post_author_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='subplan',
            name='highlight_status',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
