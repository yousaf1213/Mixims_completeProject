# Generated by Django 4.1.6 on 2023-02-07 13:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restful_api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('Product_name', models.CharField(max_length=30)),
                ('Product_desc', models.CharField(blank=True, max_length=300, null=True)),
                ('Price', models.IntegerField(max_length=4)),
                ('Id', models.UUIDField(default=uuid.UUID('f43e2dda-a734-436f-9e00-355c9a2d975d'), editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
