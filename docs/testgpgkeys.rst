===========================
Pynotes & the test GPG keys
===========================


GPG keys used in the pytest testing suite
-----------------------------------------

The test suite GPG keys can be found in the gpgkeys directory and should be imported into the developers keyring prior to running the PYTEST test suite.

Without importing and marking them as trusted GPG will fail to use them for decrypting during testing (GPG will prompt for use anyway but this will break the tests and fail the assertions used afterwards).

____

Importing the test gpg keys
---------------------------

To import the test gpgkeys::

$ gpg --import gpgkeys/\*.asc


Changing the gpg trust level for the test keys
----------------------------------------------


You will then need to change the trust level::

$ gpg -K 

and then for each of the test@pynotes.lib and alttest@pynotes.lib run the following to mark the test gpg keys as trusted::

    $ gpg --edit-key <uid>

    gpg> trust

    Please decide how far you trust this user to correctly verify other 
    users' keys (by looking at passports, checking fingerprints from 
    different sources, etc.)
    
        1 = I don't know or won't say
        2 = I do NOT trust
        3 = I trust marginally
        4 = I trust fully
        5 = I trust ultimately
        m = back to the main menu
        
    Your decision? 5
    Do you really want to set this key to ultimate trust? (y/N) y
    
    Please note that the shown key validity is not necessarily correct
    unless you restart the program.
    
    gpg> quit
    

These two keys are only used in the pytest test suite for PYNOTESLIB and are not used elsewhere so it is safe to mark these as trust ultimately.

____

Pytest encryption errors
------------------------

Without marking the gpg keys as trusted the  GPG decryption will fail and the new_key test will crash::

    _________________________ test_new_key _________________________
    
        def test_new_key():
           conf = nl.get_config()
           print(conf['gpgkey'])
        
           # Create a note with TESTKEY1 (default in unittest)
           message = "This is some text to test new_key()"
           n1 = nl.Notes(title='testing newkey')
           n1.set_plaintext(message)
           ct = n1.encrypt()
           n1.save_ciphertext()
           assert  os.path.exists(nl.get_note_fullpath(n1.filename))
        
           # change all the notes to TESTKEY2
           assert nl.new_key(TESTKEY2)
        
           # import same key into new Notes object and decrypt
           n2 = nl.Notes(filename='testing_newkey.asc')
           print(f"n2 => {n2}")
    >      assert n2.decrypt() == message
    E      AssertionError: assert '' == 'This is some...est new_key()'
    E        - This is some text to test new_key()
    
    tests/notes_class/test_new_key.py:27: AssertionError


    _________________________ Captured log call _________________________
    WARNING  gnupg:gnupg.py:1015 gpg returned a non-zero error code: 2
    WARNING  gnupg:gnupg.py:1015 gpg returned a non-zero error code: 2
    WARNING  gnupg:gnupg.py:1015 gpg returned a non-zero error code: 2
    
    ========================== short test summary info ==========================
    FAILED tests/notes_class/test_new_key.py::test_new_key - AssertionError: 
    assert '' == 'This is some...est n...
    ======================== 1 failed, 27 passed in 2.80s ========================




