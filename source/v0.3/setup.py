# setup file for the bmm executable build
from distutils.core import setup
import py2exe, sys, os

sys.argv.append('py2exe')

setup(
    options = {'py2exe': {'bundle_files': 0, 'compressed': True}},
    windows = [{'script': "bmm_wxGUI.py"}],
    zipfile = None
)
