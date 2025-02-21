# Generated by Django 5.1.6 on 2025-02-21 06:15

import django.contrib.postgres.fields
import django.contrib.postgres.indexes
from django.conf import settings
from django.contrib.postgres.operations import BtreeGinExtension
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        BtreeGinExtension(),
        migrations.AlterField(
            model_name='review',
            name='content',
            field=models.TextField(db_index=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='product_name',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='review',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), blank=True, default=list, size=None),
        ),
        migrations.AddIndex(
            model_name='review',
            index=django.contrib.postgres.indexes.GinIndex(fields=['product_name'], name='review_product_name_trgm_idx', opclasses=['gin_trgm_ops']),
        ),
        migrations.AddIndex(
            model_name='review',
            index=django.contrib.postgres.indexes.GinIndex(fields=['product_name', 'content'], name='review_full_text_search_idx'),
        ),
    ]
