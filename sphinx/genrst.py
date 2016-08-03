#!/usr/bin/python
"""
Generate the Cartd sphinx documentation templates.
"""
from os import environ, walk, sep
from os.path import join, abspath, relpath
from re import compile as re_compile

def gen_rst(pacifica_project, module_in_project):
    """
    Generate the rst files for a project by walking the directory
    structure matching python files.
    """
    init_py_re = re_compile(r'^__init__\.py$')
    reg_py_re = re_compile(r'.*\.py$')

    modules_to_load = {}

    try:
        root = environ['PACIFICA_ROOT']
    except KeyError, ex:
        print "You should set PACIFICA_ROOT to the root of the Pacifica code tree"
        print ex
        exit(-1)
    basedir = abspath(join(root, pacifica_project))

    for root, dirs, files in walk(join(basedir, module_in_project), topdown=False):
        del dirs
        root_hash = modules_to_load
        parts = relpath(root, basedir).split(sep)
        for part in parts:
            if not part in root_hash:
                root_hash[part] = {}
            root_hash = root_hash[part]
        for name in files:
            if reg_py_re.match(name) and not init_py_re.match(name):
                root_hash[name.replace('.py', '')] = 'file'
    rec_build(module_in_project, modules_to_load[module_in_project])

def rec_build(base, root_hash):
    """
    Recursively build the rst files from the modules present in
    the file tree.
    """
    mod_nice_name = base.split('.')
    new_nice_name = []
    for part in mod_nice_name:
        if '_' in part and part[0] != '_':
            new_nice_name += part.split('_')
        else:
            new_nice_name.append(part)
    mod_nice_name = [x[0].upper()+x[1:] for x in new_nice_name]
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
