import os

import pynoteslib as nl


def test_rename_notebook():
    nl.get_config()
    assert nl.create_notebook("testRenameOne")
    assert os.path.exists(nl.get_fullpath("testRenameOne"))
    nl.rename_notebook("testRenameOne", "testRenameTwo")
    assert os.path.exists(nl.get_fullpath("testRenameTwo"))

    assert not nl.rename_notebook("notebook_doesnt_exist", "newtitle")

    nl.delete_notebook("testRenameTwo")
