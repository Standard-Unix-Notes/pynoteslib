import pynoteslib as nl


def test_set_plaintext():
    my = nl.Notes()
    my.title = "this is my note title"
    assert "this_is_my_note_title" == my.title

    assert my.filename == "this_is_my_note_title"

    assert my.plaintext == ""

    assert my.ciphertext == ""

    my.plaintext = "Hello World"
    assert my.plaintext == "Hello World"

    assert my.ciphertext == ""
