# Generated by Django 4.1.6 on 2023-02-09 11:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('restful_api', '0005_alter_product_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Id',
            field=models.UUIDField(default=uuid.UUID('64b96db9-5740-473a-ac09-2c8512a2d1af'), editable=False, primary_key=True, serialize=False),
        ),
    ]