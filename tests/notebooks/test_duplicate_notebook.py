import os
import pynoteslib as nl


def test_duplicate_notebook():
    cf = nl.get_config()
    assert nl.create_notebook("testdupone")
    assert nl.duplicate_notebook("testdupone", "testduptwo")
    assert os.path.exists(nl.get_fullpath("testduptwo"))

    assert not nl.duplicate_notebook("fakenb", "newnb")

    nl.delete_notebook("testdupone")
    nl.delete_notebook("testduptwo")
