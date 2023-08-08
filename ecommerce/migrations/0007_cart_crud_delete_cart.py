# Generated by Django 4.1.7 on 2023-06-02 02:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ecommerce', '0006_rename_product_image_product_crud_pro_img_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart_crud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prod_name', models.CharField(default='true', max_length=60)),
                ('price', models.IntegerField(default=0)),
                ('description', models.CharField(max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
    ]
