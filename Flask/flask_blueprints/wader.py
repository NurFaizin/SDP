#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template


wader = Blueprint('wader', __name__, template_folder='templates')


@wader.route('/')
def list():
    return render_template('wader/list.html')


@wader.route('/create')
def create():
    return 'Create wader'


@wader.route('/read')
def read():
    return 'Read wader'


@wader.route('/update')
def update():
    return 'Update wader'


@wader.route('/delete')
def delete():
    return 'Delete wader'

