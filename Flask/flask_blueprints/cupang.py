#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template


cupang = Blueprint('cupang', __name__, template_folder='templates')


@cupang.route('/')
def list():
    return render_template('cupang/list.html')


@cupang.route('/create')
def create():
    return 'Create cupang'


@cupang.route('/read')
def read():
    return 'Read cupang'


@cupang.route('/update')
def update():
    return 'Update cupang'


@cupang.route('/delete')
def delete():
    return 'Delete cupang'

