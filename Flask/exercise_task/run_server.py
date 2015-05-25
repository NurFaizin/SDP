#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Import the main Flask app
from app import app
import routes, error_handlers

# Register Blueprint modules
app.register_blueprint(routes.blueprint)
app.register_blueprint(error_handlers.blueprint)

# Run server
if __name__ == '__main__':
	app.run(port=5000, debug=True)