import os

import pynoteslib as nl


def test_save_ciphertext():
    nl.get_config()
    n = nl.note_from_ciphertext(
        """-----BEGIN PGP MESSAGE-----

hQGMA7Af9oA7MOnKAQv9FPsceEZ/5oQDxZCKaPsDUYpVmOdr3KaaGFbefX87H3SU
Fj+BQD7zWveWxtIifKVRyI0ts/nX8uxV9RxAHjk4LkQcW3VmN3ZiZ7o+cUNycb3u
M1LcQIghV6Nyjhs7+uW2LMtMcy30Po9u0b8HUsZ4AToahTXK0jHLWOQDz8hb+Gx3
SIpwnqK7UvaMNEWjX13H9MQVAESHJcJrZQFqlLevb5TgJLcSofFWTWjsXODF7IkH
+07suuwCe6ifaliigKTlgLYou7E3TTbHWtxwLjtrOWsSZMhyQ2s0vNAU4LAqvswl
JvzFDWhr5+K057175/4lBm6OVSpJ36IMxDeLKQNLz2dr91eTYEPsQMP7WAUdtuAn
95KaYepgAdFUTxvMMtVc8yGBEYv8kjTSu2oMk6wuo9dvV3VrAiyOs9q7Dn9yFGQP
Nte04d5zbwrFAQWOkwvDxhN278SrDCL4WySpPs7Jz4w2HSN0L2MvtejIWIkVQVBt
sSiswfmoik5JVN+Km7yt0k4BUrZDFgTFF26H/VfR2AZpoPjl2xo3RAx3312q8T13
psO7Qs9fT3nC1fQOI23rw1l6epHoT/uj032Zyokk4DpDe+KUyyIaWtoi6JvEV/w=
=akED
-----END PGP MESSAGE-----
"""
    )
    n.title = "testing CT save"
    n.save_ciphertext()
    assert os.path.exists(os.path.exists(nl.get_note_fullpath("testing_CT_save.asc")))

    noteslist = nl.get_notes()
    assert "testing_CT_save.asc" in noteslist

    filepath = nl.get_note_fullpath("testing_CT_save.asc")
    assert filepath == nl.get_notesdir() + "/Notes/testing_CT_save.asc"

    os.remove(nl.get_note_fullpath("testing_CT_save.asc", "Notes"))
