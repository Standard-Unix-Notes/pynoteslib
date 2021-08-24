import os

import pynoteslib as nl

TESTKEY = "A692697DCC57084C4E87D66C7D34402EBB3EB284"


def test_rename_notefile():
    cf = nl.get_config()
    cf["gpgkey"] = TESTKEY
    nl.write_config(cf)
    my = nl.note_from_plaintext("Hello World")
    my.title = "before rename note"
    my.encrypt()
    my.save_ciphertext()
    assert os.path.exists(nl.get_note_fullpath(my.filename))

    nl.rename_note("before_rename_note.asc", "after rename note")

    assert os.path.exists(nl.get_note_fullpath("after_rename_note.asc"))
    assert not nl.rename_note("DOESNT_EXIST", "DOES_EXIST")

    os.remove(nl.get_note_fullpath("after_rename_note.asc"))
