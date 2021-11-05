# Generated by Django 3.2.8 on 2021-11-02 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blockstore_apps_bundles', '0002_create_drafts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bundle',
            name='description',
            field=models.TextField(blank=True, db_collation='utf8mb4_general_ci', max_length=10000),
        ),
        migrations.AlterField(
            model_name='bundle',
            name='slug',
            field=models.SlugField(allow_unicode=True, db_collation='utf8mb4_general_ci'),
        ),
        migrations.AlterField(
            model_name='bundle',
            name='title',
            field=models.CharField(db_collation='utf8mb4_general_ci', db_index=True, max_length=180),
        ),
        migrations.AlterField(
            model_name='bundleversion',
            name='change_description',
            field=models.TextField(blank=True, db_collation='utf8mb4_general_ci', max_length=1000),
        ),
        migrations.AlterField(
            model_name='collection',
            name='title',
            field=models.CharField(db_collation='utf8mb4_general_ci', db_index=True, max_length=180),
        ),
        migrations.AlterField(
            model_name='draft',
            name='name',
            field=models.CharField(db_collation='utf8mb4_general_ci', max_length=180),
        ),
    ]
