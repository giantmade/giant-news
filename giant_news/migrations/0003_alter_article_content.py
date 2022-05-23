# Generated by Django 3.2.13 on 2022-05-23 09:00

import cms.models.fields
from django.db import migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0022_auto_20180620_1551'),
        ('giant_news', '0002_relatedarticlecardplugin_relatedarticleplugin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='content',
            field=cms.models.fields.PlaceholderField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='giant_news_articles', slotname='article_content', to='cms.placeholder'),
        ),
    ]
