from __future__ import absolute_import,unicode_literals
import os
from celery import Celery
from django.conf import settings

# 设置celery工作目录
os.environ.setdefault('DJAGO_SETTINGS_MODULE','CeleryTask.settings')
# 实例化celery
app=Celery('Project')
# celery配置的；来源
app.config_from_object('django.conf:settings')
# 如果在app当中有创建tasks.py就会自动检索
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)
