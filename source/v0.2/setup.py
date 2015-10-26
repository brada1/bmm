# setup file for the bmm executable build
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 0, 'compressed': True}},
    console = [{'script': "bmm0.2.py"}],
    zipfile = None,
)
