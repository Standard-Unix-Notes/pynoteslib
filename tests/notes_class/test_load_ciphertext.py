import os
import pynoteslib as nl


def test_load_ciphertext():
    conf = nl.get_config()
    n1 = nl.Notes(title="testing CT load")
    n1.set_plaintext("This is the plaintext")
    n1.encrypt()
    n1.save_ciphertext()
    assert os.path.exists(nl.get_note_fullpath("testing_CT_load.asc"))

    n2 = nl.Notes(filename="testing_CT_load.asc")

    assert os.path.exists(nl.get_note_fullpath("testing_CT_load.asc"))
    assert n1.ciphertext == n2.ciphertext
    assert n1.is_encrypted()
    assert n1.plaintext == n2.plaintext

    os.remove(nl.get_note_fullpath(n1.filename, 'Notes'))

    n3 = nl.Notes(filename="doesnt_exist.asc")
    assert not n3.is_encrypted()
