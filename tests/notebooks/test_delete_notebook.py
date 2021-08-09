import os
import pynoteslib as nl

def test_delete_notebook():
    cf = nl.get_config()
    assert nl.create_notebook('testDeleteNB')
    assert os.path.exists(nl.get_fullpath('testDeleteNB'))
    assert nl.delete_notebook('testDeleteNB')
    assert not os.path.exists(nl.get_fullpath('testDeleteNB'))

    nl.delete_notebook('testDeleteNB')
