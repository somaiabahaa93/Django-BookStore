# Generated by Django 3.2 on 2021-04-22 13:00

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20210422_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='Isbn',
            fields=[
                ('autherTitle', models.CharField(max_length=256)),
                ('bookTitle', models.CharField(max_length=256)),
                ('isbnNumber', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AddField(
            model_name='book',
            name='isbn',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='books.isbn'),
        ),
    ]
