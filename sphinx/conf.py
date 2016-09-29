# -*- coding: utf-8 -*-
#
# Pacifica Metadata documentation build configuration file.
#
"""
Sphinx Configuration for Pacifica Python Documentation
"""
from os import environ
from os.path import isdir, join, abspath
from sys import path
try:
    ROOT = environ['PACIFICA_ROOT']
except KeyError, ex:
    print "You should set PACIFICA_ROOT to the root of the Pacifica code tree"
    exit(-1)
PACIFICA_PATHS = """
metadata
cartd
archiveinterface
ingest
policy
uniqueid
uploader
""".split()
PATHS = [join(ROOT, d) for d in PACIFICA_PATHS if isdir(join(ROOT, d))]
for d in PATHS:
    path.insert(0, abspath(d))
# pylint: disable=invalid-name
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.imgmath',
    'sphinx.ext.viewcode',
    'sphinx.ext.githubpages',
]
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = u'Pacifica'
# pylint: disable=redefined-builtin
copyright = u'2016, David Brown'
# pylint: enable=redefined-builtin
author = u'David Brown'
version = u'1.0'
release = u'1.0.0'
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = True
html_theme = 'sphinx_rtd_theme'
html_title = u'Pacifica v1.0.0'
html_static_path = ['_static']
htmlhelp_basename = 'PacificaDoc'
latex_elements = {}
latex_documents = [
    (master_doc, 'PacificaMetadata.tex', u'Pacifica Metadata Documentation',
     u'David Brown', 'manual'),
]
man_pages = [
    (master_doc, 'pacifica', u'Pacifica Code Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'Pacifica', u'Pacifica Code Documentation',
     author, 'Pacifica', 'Data asset life cycle management software.',
     'Miscellaneous'),
]
intersphinx_mapping = {'https://docs.python.org/': None}
# pylint: enable=invalid-name
