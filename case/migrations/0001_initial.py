# Generated by Django 3.0.3 on 2020-02-25 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('hearing_date', models.DateTimeField()),
                ('case_status', models.CharField(choices=[('pending', 'Pending'), ('active', 'Active'), ('postphoned', 'PostPhoned'), ('closed', 'Closed')], default='p', max_length=100)),
                ('defendent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='defendent', to=settings.AUTH_USER_MODEL)),
                ('first_lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='first_lawyer', to=settings.AUTH_USER_MODEL)),
                ('registered_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appealer', to=settings.AUTH_USER_MODEL)),
                ('second_lawyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='second_lawyer', to=settings.AUTH_USER_MODEL)),
                ('witness', models.ManyToManyField(blank=True, null=True, related_name='witness', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
