# Generated by Django 5.2.1 on 2025-05-14 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_skill_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('tech_stack', models.CharField(max_length=200)),
                ('github_link', models.URLField(blank=True, null=True)),
                ('live_link', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
