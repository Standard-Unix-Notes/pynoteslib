import os

import pynoteslib as nl


def test_create_notebook():
    nl.get_config()
    assert nl.create_notebook("testCreateNB")
    assert os.path.exists(nl.get_fullpath("testCreateNB"))

    assert not nl.create_notebook("testCreateNB")  # cannot create existing notebook

    nl.delete_notebook("testCreateNB")
