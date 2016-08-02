#!/usr/bin/python
from os import listdir, environ, walk, sep
from os.path import isdir, join, abspath, relpath
from sys import path
from re import compile

init_py_re = compile('^__init__\.py$')
reg_py_re = compile('.*\.py$')

modules_to_load = {}

try:
  root = environ['PACIFICA_ROOT']
except:
  print "You should set PACIFICA_ROOT to the root of the Pacifica code tree"
  exit(-1)
basedir = abspath(join(root, 'metadata'))

for root, dirs, files in walk(join(basedir, 'metadata'), topdown=False):
    parts = relpath(root, basedir).split(sep)
    root_hash = modules_to_load
    for part in parts:
        if not part in root_hash:
            root_hash[part] = {}
        root_hash = root_hash[part]
    for name in files:
        if reg_py_re.match(name) and not init_py_re.match(name):
            root_hash[name.replace('.py', '')] = 'file'

def rec_build(base, root_hash):
    mod_nice_name = base.split('.')
    new_nice_name = []
    for part in mod_nice_name:
        if '_' in part and part[0] != '_':
            new_nice_name += part.split('_')
        else:
            new_nice_name.append(part)
    mod_nice_name = [ x[0].upper()+x[1:] for x in new_nice_name ]
    mod_nice_name = ' '.join(mod_nice_name)
    new_file = open("%s.rst"%(base), "w")
    new_file.write("""
%s Module
**************************************************************

"""%(mod_nice_name))

    if isinstance(root_hash, dict):
        new_file.write("""
Contents:

.. toctree::
   :maxdepth: 2

""")
        for module in root_hash.keys():
            next_base = base+'.'+module if base else module
            new_file.write("   "+next_base+"\n")
    new_file.write("""
.. automodule:: %s
   :members:
   :private-members:

"""%(base))
    new_file.close()
    if isinstance(root_hash, dict):
        for module in root_hash.keys():
            next_base = base+'.'+module if base else module
            rec_build(next_base, root_hash[module])

rec_build("metadata", modules_to_load['metadata'])
