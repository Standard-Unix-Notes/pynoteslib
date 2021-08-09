import os
import pynoteslib as nl

TESTKEY = 'A692697DCC57084C4E87D66C7D34402EBB3EB284'


def test_delete_notefile():
    cf = nl.get_config()
    cf['gpgkey'] = TESTKEY
    nl.write_config(cf)
    my = nl.Notes(title='delete note', plaintext='Hello World')
    my.encrypt()
    my.save_ciphertext()
    assert os.path.exists(nl.get_note_fullpath('delete_note.asc'))

    nl.delete_note('delete_note.asc')
    assert not os.path.exists(nl.get_note_fullpath('delete_note.asc'))

    assert not nl.delete_note('DOESNT_EXIST')

