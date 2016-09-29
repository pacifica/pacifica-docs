#!/usr/bin/python
"""
Generate the Cartd sphinx documentation templates.
"""
from sys import argv
from os import environ, sep, listdir
from os.path import join, abspath, relpath, isdir, isfile
from re import compile as re_compile

def gen_rst(pacifica_project):
    """
    Generate the rst files for a project by walking the directory
    structure matching python files.
    """
    try:
        root = environ['PACIFICA_ROOT']
    except KeyError, ex:
        print "You should set PACIFICA_ROOT to the root of the Pacifica code tree"
        print ex
        exit(-1)
    absroot = abspath(root)
    basedir = abspath(join(root, pacifica_project))

    rec_build(absroot, basedir)

def rec_build(root, base):
    """
    Recursively build the rst files from the modules present in
    the file tree.
    """
    if isdir(base):
        process_module(root, base)
        for fname in listdir(base):
            rec_build(root, join(base, fname))

def process_module(rootpath, modulepath):
    """
    build the contents of fname
    """
    mods_to_process = []
    pys_to_process = []
    hidden_py_re = re_compile(r'^__.*__\.py$')
    reg_py_re = re_compile(r'.*\.py$')
    for fname in listdir(modulepath):
        new_mod = join(modulepath, fname)
        if isfile(join(new_mod, '__init__.py')):
            mods_to_process.append(new_mod)
        elif reg_py_re.match(fname) and not hidden_py_re.match(fname):
            pys_to_process.append(new_mod)
    rel_mod_path = relpath(modulepath, rootpath)
    mod_nice_name = rel_mod_path.split(sep)
    new_nice_name = mod_nice_name[-1]
    mod_nice_name = []
    if '_' in new_nice_name and new_nice_name[0] != '_':
        mod_nice_name += new_nice_name.split('_')
    else:
        mod_nice_name.append(new_nice_name)
    mod_nice_name = [x[0].upper()+x[1:] for x in mod_nice_name]
    new_nice_name = ' '.join(mod_nice_name)
    if len(mods_to_process) or len(pys_to_process):
        new_file = open("%s.rst"%(rel_mod_path.replace(sep, '.')), "w")
        new_file.write("""
%s Module
**************************************************************

"""%(new_nice_name))

        if len(mods_to_process):
            new_file.write("""
Contents:

.. toctree::
   :maxdepth: 2

""")
            for new_mod in mods_to_process:
                new_file.write("   "+relpath(new_mod, rootpath).replace(sep, '.')+"\n")
        for new_mod in pys_to_process:
            new_file.write("""
.. automodule:: %s
   :members:
   :private-members:

"""%('.'.join(relpath(new_mod, rootpath).replace(sep, '.').split('.')[1:-1])))
        new_file.close()

for proj in argv:
    gen_rst(proj)
