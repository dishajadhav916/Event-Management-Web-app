# Generated by Django 4.1.7 on 2023-05-28 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.FileField(default=None, max_length=250, null=True, upload_to='wed/')),
                ('pro_name', models.CharField(default='True', max_length=60)),
                ('price', models.CharField(default='True', max_length=600)),
            ],
        ),
    ]
