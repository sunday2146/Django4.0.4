# Generated by Django 3.1.7 on 2022-05-16 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='category',
            field=models.CharField(choices=[('artikel', 'Artikel'), ('blog', 'Blog'), ('berita', 'Jurnal')], default='-', max_length=20),
        ),
    ]
