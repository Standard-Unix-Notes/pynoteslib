import os
import pynoteslib as nl

def test_use_notebook():
    cf = nl.get_config()
    assert cf['use'] == nl.get_use_notebook()
    assert os.path.exists(nl.get_fullpath(cf['use']))

    nl.create_notebook('testSetUseNB')
    assert os.path.exists(nl.get_fullpath('testSetUseNB'))

    nl.use_notebook(notebook='testSetUseNB')
    assert nl.get_use_notebook() == 'testSetUseNB'

    assert not nl.use_notebook('dont_exists')

    nl.use_notebook(notebook='Notes')
    assert 'Notes' == nl.get_use_notebook()

    nl.delete_notebook('testSetUseNB')
