import os
import pynoteslib as nl

TESTKEY = "A692697DCC57084C4E87D66C7D34402EBB3EB284"


def test_duplicate_notefile():
    cf = nl.get_config()
    cf["gpgkey"] = TESTKEY
    nl.write_config(cf)
    nl.use_notebook()
    my = nl.Notes(title="before dup note", plaintext="Hello World")
    my.encrypt()
    my.save_ciphertext()
    assert os.path.exists(nl.get_note_fullpath(my.filename))

    nl.duplicate_note("before dup note", "after dup note")
    assert os.path.exists(nl.get_note_fullpath(my.filename))

    assert os.path.exists(nl.get_note_fullpath("after_dup_note.asc", notebook="Notes"))

    assert not nl.duplicate_note("DOESNT_EXIST", "DOES_EXIST")

    os.remove(nl.get_note_fullpath("before_dup_note.asc"))
    os.remove(nl.get_note_fullpath("after_dup_note.asc"))
