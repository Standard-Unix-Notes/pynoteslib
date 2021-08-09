import os
import pynoteslib as nl

def test_save_ciphertext():
    conf = nl.get_config()
    n = nl.Notes(title="testing CT save")
    n.set_ciphertext("%% GI&THJhO&GyoIyuOBy")
    n.save_ciphertext()
    assert os.path.exists(os.path.exists(nl.get_note_fullpath("testing_CT_save.asc")))

    noteslist = nl.get_notes()
    assert "testing_CT_save.asc" in noteslist

    filepath = nl.get_note_fullpath("testing_CT_save.asc")
    assert filepath == nl.get_notesdir()+"/Notes/testing_CT_save.asc"

    os.remove(nl.get_note_fullpath('testing_CT_save.asc', 'Notes'))
