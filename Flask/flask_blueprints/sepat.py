#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template, redirect, abort


sepat = Blueprint('sepat', __name__, template_folder='templates')


@sepat.route('/')
def list():
    return render_template('sepat/list.html')


@sepat.route('/create')
def create():
    return 'Create sepat'


@sepat.route('/read')
def read():
    return 'Read sepat'


@sepat.route('/update')
def update():
    return 'Update sepat'


@sepat.route('/delete')
def delete():
    return 'Delete sepat'


@sepat.before_request
def restrict_sepat_to_admins():
    # return redirect('/unauthorized')
    abort(403)
