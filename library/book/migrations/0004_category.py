# Generated by Django 2.2.10 on 2020-12-14 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_book_writer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=15)),
                ('status', models.BooleanField(default=True, verbose_name='Do you want to show it?')),
            ],
        ),
    ]
