# -*- coding: utf8 -*-
from celery import Celery
from celery_config import CeleryConfig


celery_app = Celery("standAlone")
celery_app.conf.update(CeleryConfig)
