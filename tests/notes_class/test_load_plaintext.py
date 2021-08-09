import os
import pynoteslib as nl


def test_load_plaintext():
    conf = nl.get_config()
    n1 = nl.Notes(title="testing PT save")
    n1.set_plaintext("This is some text")
    n1.save_plaintext()
    assert os.path.exists(nl.get_note_fullpath("testing_PT_save"))
    print(n1)
    n2 = nl.Notes(filename='testing_PT_save')
    print(n2)
    assert n2.plaintext == n1.plaintext

    os.remove(nl.get_note_fullpath('testing_PT_save', 'Notes'))
