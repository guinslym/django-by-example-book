# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('verb', models.CharField(max_length=255)),
                ('target_id', models.PositiveIntegerField(null=True, db_index=True, blank=True)),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('target_ct', models.ForeignKey(related_name='target_obj', to='contenttypes.ContentType', null=True, blank=True)),
                ('user', models.ForeignKey(related_name='actions', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-created',),
            },
            bases=(models.Model,),
        ),
    ]
