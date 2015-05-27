# -*- coding: utf8 -*-
from celery import Celery
from celery_config import CeleryConfig


def create_celery(app):
    celery_app = Celery("withFlask")
    celery_app.conf.update(CeleryConfig)
    TaskBase = celery_app.Task

    class ContextTask(TaskBase):
        abstrack = True

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery_app.Task = ContextTask

    return celery_app
