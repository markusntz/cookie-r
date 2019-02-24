#!/usr/bin/env python

import os
import shutil

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_dir(filepath):
    shutil.rmtree(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':

    if '{{ cookiecutter.models }}' == 'n':
        remove_dir('models/')

    if '{{ cookiecutter.tests }}' == 'n':
        remove_dir('tests/')