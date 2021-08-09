import os
import pynoteslib as nl

TESTKEY = 'A692697DCC57084C4E87D66C7D34402EBB3EB284'


def test_copy_to_notebookfile():
    cf = nl.get_config()
    cf['gpgkey'] = TESTKEY
    nl.write_config(cf)
    my = nl.Notes(title='copyto note', plaintext='Hello World')
    my.encrypt()
    my.save_ciphertext()
    assert os.path.exists(nl.get_note_fullpath('copyto_note.asc'))

    assert nl.create_notebook('copy2notebook')

    nl.copy_to_notebook(my.filename, 'copy2notebook')
    assert os.path.exists(nl.get_note_fullpath('copyto_note.asc'))

    assert os.path.exists(os.path.join(nl.get_notesdir(), 'copy2notebook' , 'copyto_note.asc'))

    assert not nl.copy_to_notebook('DOESNT_EXIST', 'copy2notebook')

    nl.delete_notebook('copy2notebook')


def test_copy_to_notebookfile_invalid_notebook():
    cf = nl.get_config()
    cf['gpgkey'] = TESTKEY
    nl.write_config(cf)
    my = nl.Notes(title='copyto note fake notebook', plaintext='Hello World')
    my.encrypt()
    my.save_ciphertext()
    assert not nl.copy_to_notebook(my.filename, 'NOTEBOOK_DOESNT_EXIST')

    os.remove(nl.get_note_fullpath('copyto_note_fake_notebook.asc'))
