# Generated by Django 2.2.10 on 2020-12-25 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catName', models.CharField(max_length=15, verbose_name='category name')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('status', models.BooleanField(default=True, verbose_name='Do you want to show it?')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='media')),
                ('abstract', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('writer', models.CharField(blank=True, max_length=25, null=True)),
                ('status', models.CharField(blank=True, choices=[('P', 'published'), ('D', 'draft')], max_length=1, null=True)),
                ('category', models.ManyToManyField(related_name='book', to='book.Category')),
                ('shop', models.ManyToManyField(blank=True, to='shop.Shop')),
            ],
        ),
    ]
