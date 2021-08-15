import datetime
import os

import pynoteslib as nl


def test_backup():
    cf = nl.get_config()
    t = datetime.datetime.now()
    tarfile = f"../notes_backup_{t.strftime('%Y%b%d_%H%M')}.tar"
    result, tf = nl.backup(cf)
    assert result
    assert os.path.exists(nl.get_fullpath(tarfile))

    os.remove(nl.get_fullpath(tarfile))
