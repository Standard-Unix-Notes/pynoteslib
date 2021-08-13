import pynoteslib as nl


def test_import_note():  # imports a note from full pathname file
    n = nl.import_note("makefile")
    assert not n.plaintext == ""
    assert n.ciphertext == ""

    assert not nl.import_note("fakenote")
