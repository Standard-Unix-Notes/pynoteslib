import os

import pynoteslib as nl


def test_load_plaintext():
    nl.get_config()
    n1 = nl.note_from_plaintext("testing plaintext save")
    n1.title = "testing PT save"
    n1.save_plaintext()
    assert os.path.exists(nl.get_note_fullpath("testing_PT_save"))

    n2 = nl.load_note_from_file("testing_PT_save")

    print(n1)
    print(n2)
    assert n2.plaintext == n1.plaintext

    os.remove(nl.get_note_fullpath("testing_PT_save", "Notes"))
