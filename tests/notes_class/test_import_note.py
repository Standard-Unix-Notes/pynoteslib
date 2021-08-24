import pytest

import pynoteslib as nl


def test_import_note():  # imports a note from full pathname file
    n = nl.import_note_from_file("/etc/passwd")
    assert not n.plaintext == ""
    assert n.ciphertext == ""

    with pytest.raises(FileNotFoundError):
        nl.import_note_from_file("/fakenote")
