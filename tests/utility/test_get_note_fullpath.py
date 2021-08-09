import os
import pynoteslib as nl


def test_get_note_fullpath():
    assert os.environ['NOTESDIR'] + '/Notes/my_note' == nl.get_note_fullpath('my_note')

