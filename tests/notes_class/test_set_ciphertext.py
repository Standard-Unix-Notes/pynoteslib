import pynoteslib as nl


def test_set_ciphertext():
    my = nl.Notes(title="this is my note title")
    my.plaintext = "This is my secret in plaintext"
    assert "this_is_my_note_title" == my.title
    assert my.filename == "this_is_my_note_title"
    assert my.plaintext == "This is my secret in plaintext"
    assert my.ciphertext == ""

    my.encrypt()

    assert my.filename == "this_is_my_note_title.asc"
    assert my.plaintext == ""
    assert not my.ciphertext == "This is my secret in plaintext"
