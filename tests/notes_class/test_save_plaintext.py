import os

import pynoteslib as nl


def test_save_plaintext():
    nl.get_config()
    n = nl.note_from_plaintext("text for testing PT save")
    n.title = "testing PT save"
    n.save_plaintext()
    assert os.path.exists(nl.get_note_fullpath("testing_PT_save"))

    os.remove(nl.get_note_fullpath("testing_PT_save", "Notes"))
