# Generated by Django 3.0.2 on 2020-07-19 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_remove_itemlink_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemlink',
            name='item',
            field=models.ForeignKey(default='1538900e-97b7-4567-83f3-7565c0b8f604', on_delete=django.db.models.deletion.CASCADE, related_name='itemlink', to='project.Item'),
            preserve_default=False,
        ),
    ]