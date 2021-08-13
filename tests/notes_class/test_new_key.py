import pytest
import os
import pynoteslib as nl

TESTKEY1 = "A692697DCC57084C4E87D66C7D34402EBB3EB284"
TESTKEY2 = "FE326B58CDD40DF70FEAB2722822B15BB44A9055"
FAKEKEY = "Not Really a GPG key"


def test_new_key():
    conf = nl.get_config()
    print(conf["gpgkey"])

    # Create a note with TESTKEY1 (default in unittest)
    message = "This is some text to test new_key()"
    n1 = nl.Notes(title="testing newkey")
    n1.set_plaintext(message)
    ct = n1.encrypt()
    n1.save_ciphertext()
    assert os.path.exists(nl.get_note_fullpath(n1.filename))

    # change all the notes to TESTKEY2
    assert nl.new_key(TESTKEY2)

    # import same key into new Notes object and decrypt
    n2 = nl.Notes(filename="testing_newkey.asc")
    print(f"n2 => {n2}")
    assert n2.decrypt() == message

    assert not nl.new_key(FAKEKEY)

    nl.new_key(TESTKEY1)
