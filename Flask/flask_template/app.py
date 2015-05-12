import os
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/route1/')
@app.route('/route2/')
@app.route('/lengthy/route3/')
def multiple_routes():
    message = "A single vier can handle multiple routes"
    return render_template('page.html', message=message)


@app.route('/no-slash')
@app.route('/slash/')
def trailing_slash():
    message = "If the route URL has a trailing slash, there will be a redirect"
    return render_template('page.html', message=message)


@app.route('/message/<msg>/')
def capture_value(msg):
    message = "Variable parts in the route can be specified with \
                angular bracket"
    message = "Value captured in this view is the message - %s" % (msg)
    return render_template('page.html', message=message)


@app.route('/users/<int:userid>/')
def capture_value_int(userid):
    message = "It is possible to capture variable parts and \
                convert to various type"
    return render_template('page.html', message=message)


@app.route('/method/get/', methods=['GET'])
def handle_get_only():
    message = "It is possible to specify the methods a view will handle."
    return render_template('page.html', message=message)


@app.route('/page/', defaults={'page': 1})
@app.route('/page/<int:page>/')
def show_page(page):
    message = "This is page number %d. If no page number is specified, \
                the view get defaults value" % (page)
    return render_template('page.html', message=message)


if __name__ == '__main__':
    app.debug = True
    app.run(
        host="0.0.0.0",
        port=int("5000")
    )
