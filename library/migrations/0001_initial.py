# Generated by Django 4.0.2 on 2022-08-15 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('descr', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='complete title of the book', max_length=100)),
                ('copies', models.IntegerField(blank=True, default=1)),
                ('edition', models.IntegerField(blank=True, null=True)),
                ('cover_image', models.ImageField(default='/default_cover.png', upload_to='book_covers/')),
                ('author', models.ManyToManyField(to='library.Author')),
                ('dept', models.ManyToManyField(to='library.Department')),
            ],
        ),
    ]
