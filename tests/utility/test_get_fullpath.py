import os
import pynoteslib as nl


def test_get_fullpath():
    assert os.environ['NOTESDIR'] + '/config' == nl.get_fullpath('config')

