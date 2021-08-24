import pytest

import pynoteslib as nl

# these tests aren't really user facing functions


def test_set_gpgkey():
    n = nl.Notes()
    n.gpgkey = "dummy_gpg_key"
    assert n.gpgkey == "dummy_gpg_key"


def test_set_gpghandle():
    n = nl.Notes()
    n.gpghandle = "dummy_gpg_handle"
    assert n.gpghandle == "dummy_gpg_handle"
