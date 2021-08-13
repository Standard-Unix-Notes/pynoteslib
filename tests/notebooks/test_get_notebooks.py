import os

import pynoteslib as nl


def test_get_notebooks():
    nl.get_config()

    # create a new notebook, and check if 'Notes' and new notebook in returned list
    nl.create_notebook("testGetNB")

    assert os.path.exists(nl.get_fullpath("testGetNB"))
    assert not set(["Notes", "testGetNB"]).intersection(nl.get_notebooks()) == set()

    nl.delete_notebook("testGetNB")
