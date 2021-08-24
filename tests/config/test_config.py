import os

# import pynoteslib
import pynoteslib as nl

# from pynoteslib import get_config


# import pudb; pu.db


def test_get_config():
    cf = nl.get_config()
    assert cf["configfile"] == os.getcwd() + "/__testing__/notesdir/config"


def test_configfile_exists():
    cf = nl.get_config()
    assert os.path.exists(cf["configfile"])
