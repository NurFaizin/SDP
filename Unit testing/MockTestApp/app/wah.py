from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route("/_add_numbers")
def add_numbers():
	a = request.args.get('a', 0, type=int)
	b = request.args.get('b', 0, type=int)
	return jsonify(result= a + b)


@app.route("/_numbers")
def numbers():
	return jsonify(result=201)


if __name__ == '__main__':
	app.run(
		host="0.0.0.0",
		port=int(5000),
		debug=True
	)