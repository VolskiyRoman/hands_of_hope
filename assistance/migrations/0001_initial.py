# Generated by Django 5.1.7 on 2025-05-10 06:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('shelter', 'Shelter'), ('evacuation', 'Evacuation'), ('medicine', 'Medicine'), ('food', 'Food'), ('psychological', 'Psychological'), ('clothes', 'Clothes'), ('transport', 'Transport'), ('info_support', 'Info Support'), ('legal', 'Legal'), ('repair', 'Repair'), ('volunteer', 'Volunteer'), ('other', 'Other')], max_length=32)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('contact_phone', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('open', 'Open'), ('in_progress', 'In Progress'), ('resolved', 'Resolved'), ('rejected', 'Rejected')], default='open', max_length=32)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='help_requests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HelpReply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('responder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='assistance.helprequest')),
            ],
        ),
    ]
