import os
import pynoteslib as nl

def test_get_default_notebook():
    cf = nl.get_config()
    assert cf['default'] == 'Notes'
    assert os.path.exists(nl.get_fullpath(cf['default']))
    assert cf['default'] == nl.get_default_notebook()
    assert os.path.exists(nl.get_fullpath(nl.get_default_notebook()))
