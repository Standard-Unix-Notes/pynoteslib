import os

import pynoteslib as nl


def test_get_notes_from_notebook():
    nl.get_config()
    assert nl.create_notebook("testgetnotesNB")

    nl.use_notebook(notebook="testgetnotesNB")
    n1 = nl.note_from_plaintext("Hello World")
    n1.title = "note1"
    n1.encrypt()
    n1.save_ciphertext()
    assert os.path.exists(
        os.path.join(nl.get_notesdir(), "testgetnotesNB", n1.filename)
    )

    n2 = nl.note_from_plaintext("Hello World")
    n2.title = "note2"
    n2.encrypt()
    n2.save_ciphertext()
    assert os.path.exists(
        os.path.join(nl.get_notesdir(), "testgetnotesNB", n2.filename)
    )

    notelist = nl.get_notes("testgetnotesNB")
    assert notelist.sort() == ["note1.asc", "note2.asc"].sort()

    assert [] == nl.get_notes("doesnot_exist")

    nl.use_notebook(notebook="Notes")

    nl.delete_notebook("testgetnotesNB")
