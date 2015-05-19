#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, Blueprint

blueprint = Blueprint('error_handlers', __name__)

@blueprint.app_errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


@blueprint.app_errorhandler(401)
def unauthorized(error=None):
    """
    401 Unauthorized response should be used for missing or
    bad authentication
    """
    message = {
            'status': 401,
            'message': 'Unauthorized: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 401

    return resp


@blueprint.app_errorhandler(403)
def forbidden(error=None):
    """
    403 Forbidden response should be used afterwards,
    when the user is authenticated but isn’t authorized to
    perform the requested operation on the given resource.
    """
    message = {
            'status': 403,
            'message': 'Forbidden: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 403

    return resp

@blueprint.app_errorhandler(400)
def forbidden(error=None):
    """
    404 The browser (or proxy) sent a request that
    this server could not understand.
    """
    message = {
            'status': 400,
            'message': 'Bad Request: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp