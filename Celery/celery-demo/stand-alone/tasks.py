from celery_factory import celery_app


@celery_app.task
def penjumlahan(x, y):
    data = x + y
    print "result penjumlahan > %s" % data
    return data
