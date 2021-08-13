import pynoteslib as nl


def test_set_plaintext():
    my = nl.Notes(title="this is my note title")
    assert "this_is_my_note_title", my.title

    assert my.filename == "this_is_my_note_title"

    assert my.get_filename() == "this_is_my_note_title"

    assert my.plaintext == ""

    assert my.ciphertext == ""

    my.set_plaintext("Hello World")
    assert my.plaintext == "Hello World"

    assert my.ciphertext == ""
