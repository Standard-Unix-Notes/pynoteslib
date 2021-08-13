import os
import pytest
from pynoteslib import *

# import pudb; pu.db


def test_get_config():
    cf = get_config()
    assert cf["configfile"] == os.getcwd() + "/__testing__/notesdir/config"


def test_configfile_exists():
    cf = get_config()
    assert os.path.exists(cf["configfile"])


if __name__ == "__main__":
    sys.exit(pytest.main(["-qq"], plugins=[MyPlugin()]))
