# Generated by Django 3.0.2 on 2020-07-19 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_itemlink_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemlink',
            name='item',
            field=models.ForeignKey(default='1538900e-97b7-4567-83f3-7565c0b8f604', on_delete=django.db.models.deletion.CASCADE, related_name='itemlinks', to='project.Item'),
        ),
    ]