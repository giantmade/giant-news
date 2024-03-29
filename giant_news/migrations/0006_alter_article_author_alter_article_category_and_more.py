# Generated by Django 4.1.7 on 2023-03-20 09:16

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import filer.fields.image
import giant_news.models.article


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ("cms", "0022_auto_20180620_1551"),
        ("giant_news", "0005_auto_20220912_0459"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="author",
            field=models.ForeignKey(
                default=giant_news.models.article._default_author,
                null=True,
                on_delete=django.db.models.deletion.SET_DEFAULT,
                related_name="%(app_label)s_%(class)ss",
                to="giant_news.author",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)ss",
                to="giant_news.category",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="content",
            field=cms.models.fields.PlaceholderField(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="%(app_label)s_%(class)ss",
                slotname="content",
                to="cms.placeholder",
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="photo",
            field=filer.fields.image.FilerImageField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="%(app_label)s_%(class)s_images",
                to=settings.FILER_IMAGE_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="article",
            name="tags",
            field=models.ManyToManyField(
                related_name="%(app_label)s_%(class)s_tags",
                to="giant_news.tag",
                verbose_name="Tags",
            ),
        ),
        migrations.AlterField(
            model_name="relatedarticlecardplugin",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="%(app_label)s_%(class)s",
                serialize=False,
                to="cms.cmsplugin",
            ),
        ),
        migrations.AlterField(
            model_name="relatedarticleplugin",
            name="cmsplugin_ptr",
            field=models.OneToOneField(
                auto_created=True,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                related_name="%(app_label)s_%(class)s",
                serialize=False,
                to="cms.cmsplugin",
            ),
        ),
    ]
