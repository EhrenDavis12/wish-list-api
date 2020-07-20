# Generated by Django 3.0.2 on 2020-07-19 03:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('is_purchased', models.BooleanField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wish_list_item', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='ItemLink',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('link', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_link', to=settings.AUTH_USER_MODEL)),
                ('wish_list_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project.Item')),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]