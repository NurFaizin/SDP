from flask import Flask

# Initilize the Flask application
app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/hello/<name>', methods=['GET', 'POST'])
def hello_name(name):
    return 'Hello %s!' % name

@app.route('/random-number/<int:number>')
def random_number(number):
    return 'Number %d!' % number

@app.route('/tag/<reqtag>', defaults={'pagenumber': 1})
@app.route('/tag/<reqtag>/page/<int:pagenumber>')
def posts_by_tag(reqtag, pagenumber):
    return "Showing post with tag %s, page %d" % (reqtag, pagenumber)

if __name__ == '__main__':
    app.debug = True
    app.run(
        host = "0.0.0.0",
        port = int("80")
    )
