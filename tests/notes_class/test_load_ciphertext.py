import os

import pytest

import pynoteslib as nl


def test_load_ciphertext():
    nl.get_config()
    n1 = nl.Notes()
    n1.title = "testing CT load"
    n1.plaintext = "This is the plaintext"
    n1.encrypt()
    n1.save_ciphertext()
    assert os.path.exists(nl.get_note_fullpath("testing_CT_load.asc"))

    n2 = nl.load_note_from_file("testing_CT_load.asc")

    assert n1.ciphertext == n2.ciphertext
    assert n1.is_encrypted()
    assert n1.plaintext == n2.plaintext

    os.remove(nl.get_note_fullpath(n1.filename, "Notes"))

    with pytest.raises(FileNotFoundError):
        nl.load_note_from_file("doesnt_exist.asc")
