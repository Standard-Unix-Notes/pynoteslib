import os
import pynoteslib as nl


def test_get_use_notebook():
    cf = nl.get_config()
    assert cf["use"] == "Notes"
    assert cf["use"] == nl.get_use_notebook()
    assert os.path.exists(nl.get_fullpath(cf["use"]))
