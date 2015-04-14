#!/bin/bash

# Sebangsa SDP - Kelas Python
# Bash script for installing python2.6.8, python3.3.5 and pip
# Author	: @fafa_shiro
# Date		: 04/14/2014

#Stop on error
set -e

# Installing dependencies
sudo apt-get install zlib1g-dev openssl libssl-dev

# Python 2.6.8
wget -nc http://python.org/ftp/python/2.6.8/Python-2.6.8.tar.xz
tar xf Python-2.6.8.tar.xz
cd Python-2.6.8

# Patching bugs on python2.6.8 > Ubuntu 11.04
# Issue http://bugs.python.org/issue9762
wget -nc http://bugs.python.org/file26938/py26-fix.diff
patch -p1 < py26-fix.diff

# Patching bugs zlib modules on python2.6.8 > Ubuntu 12.04
sudo ln -s /lib/x86_64-linux-gnu/libz.so.1 /lib/x86_64-linux-gnu/libz.so

./configure --prefix=/usr/local --enable-unicode=ucs4 --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
make && sudo make altinstall

# Python 3.3.5
wget -nc http://python.org/ftp/python/3.3.5/Python-3.3.5.tar.xz
tar xf Python-3.3.5.tar.xz
cd Python-3.3.5
./configure --prefix=/usr/local --enable-shared LDFLAGS="-Wl,-rpath /usr/local/lib"
make && sudo make altinstall

# Installing Setuptools & pip
# Download ez_setup
wget -nc https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py

# Installing easy_install
sudo python2.6 ez_setup.py
sudo python3.3 ez_setup.py

# Installing pip
sudo easy_install-2.6 pip
sudo easy_install-3.3 pip
