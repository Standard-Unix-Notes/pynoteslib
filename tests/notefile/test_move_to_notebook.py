import os

import pynoteslib as nl

TESTKEY = "A692697DCC57084C4E87D66C7D34402EBB3EB284"


def test_move_to_notebook():
    cf = nl.get_config()
    cf["gpgkey"] = TESTKEY
    nl.write_config(cf)
    my = nl.Notes(title="moveto note", plaintext="Hello World")
    my.encrypt()
    my.save_ciphertext()
    assert os.path.exists(nl.get_note_fullpath("moveto_note.asc"))

    assert nl.create_notebook("move2notebook")

    nl.move_to_notebook(my.filename, "move2notebook")
    assert not os.path.exists(nl.get_note_fullpath("moveto_note.asc"))

    assert os.path.exists(
        os.path.join(nl.get_notesdir(), "move2notebook", "moveto_note.asc")
    )

    assert not nl.move_to_notebook("DOESNT_EXIST", "move2notebook")

    assert not nl.move_to_notebook(my.filename, "NOTEBOOK_DOESNT_EXIST")

    nl.delete_notebook("move2notebook")
