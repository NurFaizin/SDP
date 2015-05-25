#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, jsonify, request, Blueprint

blueprint = Blueprint('error_handlers', __name__)

@blueprint.app_errorhandler(404)
def not_found(error=None):
    """
    404 Not found request rule
    """
    message = {
        'errors': {
            'status': 404,
            'detail': 'Not Found: ' + request.url,
        }
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
        'errors': {
            'status': 401,
            'detail': 'Unauthorized: ' + request.url,
        }
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
        'errors': {
            'status': 403,
            'detail': 'Forbidden: ' + error,
        }
    }
    resp = jsonify(message)
    resp.status_code = 403

    return resp


@blueprint.app_errorhandler(400)
def bad_request(error=None):
    """
    400 The browser (or proxy) sent a request that
    this server could not understand.
    """
    message = {
        'errors': {
            'status': 400,
            'detail': 'Bad Request: ' + error,
        }
    }
    resp = jsonify(message)
    resp.status_code = 400

    return resp


@blueprint.app_errorhandler(500)
def internal_error(error=None):
    """
    500 Internal server error
    """
    message = {
        'errors': {
            'status': 500,
            'detail': 'Internal server error',
        }
    }
    resp = jsonify(message)
    resp.status_code = 500

    return resp