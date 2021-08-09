import os
import pynoteslib as nl


def test_default_notebook():
    cf = nl.get_config()
    assert cf['use'] == nl.get_default_notebook()
    assert os.path.exists(nl.get_fullpath(cf['use']))

    nl.create_notebook('testSetDefNB')
    assert os.path.exists(nl.get_fullpath('testSetDefNB'))

    nl.default_notebook('testSetDefNB')
    assert nl.get_default_notebook() == 'testSetDefNB'

    assert not nl.default_notebook('doesnt_exist')

    assert nl.default_notebook(cf['default'])

    assert nl.default_notebook('Notes')
    assert 'Notes' == nl.get_default_notebook()

    nl.delete_notebook('testSetDefNB')
