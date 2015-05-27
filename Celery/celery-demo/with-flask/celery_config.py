# -*- coding: utf8 -*-


CeleryConfig = dict(

    #: jumlah connection pool yang boleh dibuka oleh tiap worker.
    BROKER_POOL_LIMIT=10,

    #: num of task per child worker.
    CELERYD_MAX_TASKS_PER_CHILD=100,

    #: serializer yang disupport
    CELERY_ACCEPT_CONTENT=['json', 'msgpack', 'yaml'],

    #: broker, dalam demo ini rabbitmq
    CELERY_BROKER_URL="amqp://guest@localhost//",

    #: rate limit untuk tiap task. 200 task per detik per worker
    CELERY_DEFAULT_RATE_LIMIT='200/s',

    #: import tasknya.
    CELERY_IMPORTS=(
        "tasks",
    ),

    #: backend. penyimpanan result dari task
    CELERY_RESULT_BACKEND="amqp",
    CELERY_RESULT_SERIALIZER="json",

    #: masing-masing result akan expired setelah 43200 detik
    CELERY_TASK_RESULT_EXPIRES=43200,
    CELERY_TASK_SERIALIZER="json",

    #: timezone
    CELERY_TIMEZONE='Asia/Jakarta',
)
