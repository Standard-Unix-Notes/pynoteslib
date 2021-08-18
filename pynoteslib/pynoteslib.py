"""
PYNOTESLIB the Python library implementation of Standard Unix Notes.

It implements the notes() class and a number of functions to manipulate
notebooks and configuration.

NOTES allows the user to have multiple notebooks and even a default
notebook.  The initial notebook is called simply 'Notes' and all notes
created or imported will default to this notebook.

The user may create additional notebooks at any time and choose to USE
a preferred notebook where all future notes will be created until the
user chooses to USE another notebook. The user can quickly switch back
to a DEFAULT notebook by not specifying which notebook to USE.

Full documentation can be found at
https://pynoteslib.readthedocs.io/en/latest/
"""

import datetime
import os
import shutil
import sys
import tarfile

import gnupg  # see https://docs.red-dove.com/python-gnupg/
import toml

_default_config = {
    "gpgkey": "A692697DCC57084C4E87D66C7D34402EBB3EB284",
    "spelling": "none",
    "default": "Notes",
    "use": "Notes",
    "HOME": os.environ["HOME"],
    "notesdir": "",
    "configfile": "",
}

os.environ["NOTESDIR"] = os.getcwd() + "/__testing__/notesdir"


GPGEXT = ".asc"


def _init_dirs():  # pragma: no cover
    """ Setup the NOTESDIR directory structure. _init_dirs() is called by
    create_config()

    1.  This function gets the base NOTESDIR from get_notedir() which in
        turn examines the environment variable for NOTESDIR else uses
        ~/.notes
    2.  Creates NOTESDIR directory
    3.  Creates first Notebook 'NOTESDIR/Notes/'

    :param: none

    :return: none
    """

    notesdir = os.path.realpath(get_notesdir())

    if not os.path.exists(notesdir):
        os.mkdir(notesdir, mode=0o700)

    if not os.path.exists(notesdir + "/Notes"):
        print(f"Creating Default notebook {notesdir + '/Notes'}")
        os.mkdir(notesdir + "/Notes", mode=0o700)


def create_config():
    """ Create directory structure under NOTESDIR and TOML config file
    NOTESDIR/config

    :param: none

    :return: none
    """

    _init_dirs()
    conf = dict(_default_config)

    conf["notesdir"] = get_notesdir()
    conf["configfile"] = get_config_file()
    conf["gpgkey"] = get_default_gpg_key()

    write_config(conf)


def get_config():
    """ Reads configuration from the TOML file NOTESDIR/config.
    If 'config' file does not exist, calls create_config() to create

    :param: none

    :return: Configuration loaded from the TOML file 'config'
    :rtype: dict
    """

    if not config_file_exists():
        create_config()

    with open(get_config_file(), "r") as config:
        return toml.load(config)


def write_config(conf):
    """ Writes app configuration to TOML file NOTESDIR/config (see
    _default_config as a sample structure)

    :param conf: Dictionary containing configuration data
    :type: dict

    :return: True on successful write of configfile
    :rtype: bool

    """

    with open(get_config_file(), "w") as configf:
        toml.dump(conf, configf)
        return True


def get_config_file():
    """ Get the fullpath to the app configuration file NOTESDIR/config

    :param: none

    :return: fullpath to the config file fullpath
    :rtype: str
    """

    return get_notesdir() + "/config"


def get_notesdir():
    """ Gets the fullpath to the main app directory

    :param: none

    :return: the app's home folder (either NOTESDIR or $HOME/.notes)
    :rtype: str
    """

    if "NOTESDIR" in os.environ:
        notesdir = os.environ["NOTESDIR"]
    else:
        notesdir = os.environ["HOME"] + "/.notes"

    return os.path.realpath(notesdir)


def config_file_exists():
    """ Checks to see if NOTESDIR/config file exists

    :param: none

    :return: True if NOTESDIR/config file exists
    :rtype: bool
    """

    return os.path.exists(get_config_file())


def get_default_gpg_key():
    """ Locates the first private key in the users GPG keyring

    Under testing conditions it returns the test@pynoteslib GPG key
    shown in _default_config['gpgkey'] to use in testing

    In normal conditions it returns the first private gpgkey found in
    the user's keyring

    :param: none

    :return: The first GPG key ID found in user's keyring
    :rtype: str
    """

    if "py.test" in sys.modules.keys():
        return _default_config["gpgkey"]

    # pragma: no cover
    gpg = gnupg.GPG(gnupghome="/home/ian/.gnupg")
    private_keys = gpg.list_keys(True)
    return private_keys[0]["keyid"]


def backup(conf):
    """ Backup configuration, notes and notebook to tar file in the directory
    above the NOTESDIR (default = HOME)

    :param: none

    :return: The return code of tarfile creation/write
    :rtype: bool
    """

    now = datetime.datetime.now()
    conf = get_config()
    backupfile = f"{conf['notesdir']}/../notes_backup_{now.strftime('%Y%b%d_%H%M')}.tar"

    try:
        tar = tarfile.open(backupfile, "w")
        tar.add(conf["notesdir"])
        tar.close()
        return True, backupfile

    except tarfile.TarError as err:  # pragma: no cover
        return err


def get_default_notebook():
    """ Reads config file and returns what notebook is the default

    :param: none

    :return: The name of the default notebook
    :rtype: str
    """

    conf = get_config()
    return conf["default"]


def get_use_notebook():
    """ Reads config file and returns what notebook is currently used notebook

    :param: none

    :return: The currently 'use'd notebook (where notes will be created)
    :rtype: str
    """

    conf = get_config()
    return conf["use"]


def default_notebook(notebook):
    """ Set a notebook as th edefault notebook
    (use_notebook() defaults to the DEFAULT notebook if '' instead of
    a notebook title)

    :param notebook: notebook to set as default
    :type notebook: str

    :return: Returns True on success of write_config() with updated configuration
    :rtype: bool
    """

    conf = get_config()

    nb_fullpath = get_fullpath(notebook)

    if os.path.exists(nb_fullpath):
        conf["default"] = notebook
        return write_config(conf)

    return False


def use_notebook(notebook=""):
    """ Reads config file and returns the DEFAULT notebook.  If no notebook
    is specified then the USE notebook is set to the DEFAULT notebook

    :param notebook: Title of notebook to USE, optional
    :type notebook: str

    :return: Returns True on successful write of new config file
    :rtype: bool
    """

    conf = get_config()
    if notebook == "":
        notebook = conf["default"]

    nb_fullpath = get_fullpath(notebook)

    if os.path.exists(nb_fullpath):
        conf["use"] = notebook
    else:
        return False

    return write_config(conf)


def get_notebooks():
    """ Returns a list  of all notebooks in NOTESDIR

    :param: none

    :return: A list[] of notebooks
    :rtype: list
    """

    conf = get_config()
    return next(os.walk(conf["notesdir"]))[1]


def get_notes(notebook=""):
    """ Returns a list of note in given notebook (or the USE'd notebook)

    :param notebook: Specified notebook to USE, defaults to DEFAULT notebook
    :type notebook: str, optional

    :return: list of notes in notebook; or [] for invalid notebook
    :rtype: list
    """

    if notebook == "":
        conf = get_config()
        notebook = conf["use"]

    notebook = os.path.join(get_notesdir(), notebook)

    if os.path.exists(notebook):
        return os.listdir(notebook)

    return []


def new_key(newkey):
    """ Change encryption key for all notes. Traverses filesystem in
    NOTESDIR/[all notebooks]. Decrypts and re-encrypts with specified newkey

    :param newkey: New valid gpg privakey keyid
    :type newkey: str

    :return: Returns True on re-encryption; False on invalid private key
    :rtype: bool
    """

    #     Change GPG key for all notes.
    if not validate_gpg_key(newkey):  # return False if not valid private key
        return False

    # newkey -> config [picked up later by Notes.encrypt()]
    conf = get_config()
    print(conf)
    conf["gpgkey"] = newkey
    write_config(conf)

    for notebook in get_notebooks():
        for note in get_notes(notebook=notebook):
            target = Notes(filename=note)
            target.decrypt()
            target.encrypt()
            target.save_ciphertext()
    return True


def validate_gpg_key(gpgkeyid):
    """ Validates the specified gpgkeyid is a private key in the user's
    keyring

    :param: none

    :return: True if gpgkey is a valid private key
    :rtype: bool
    """

    conf = get_config()
    _gpghome = conf["HOME"] + "/.gnupg"
    gpg = gnupg.GPG(gnupghome=_gpghome)
    private_keys = gpg.list_keys(True, keys=gpgkeyid)

    return private_keys


def get_fullpath(name):
    """ Return full pathname of passed parameter

    :param name: A notebook, filename (eg. 'config') or expression`
    :type name: str

    :return: Returns full path for 'name' UNDER the NOTESDIR
    :rtype: str
    """

    conf = get_config()
    return conf["notesdir"] + "/" + name


def get_note_fullpath(note, notebook=""):
    """ Returns the full pathname of a note within the currently USE'd
    Notebook

    :param note: The title (or filename) of a note
    :type: str

    :return: Returns full path to a note
    :rtype: str
    """

    conf = get_config()
    if notebook == "":
        notebook = conf["use"]

    return conf["notesdir"] + "/" + notebook + "/" + change_spaces(note)


def change_spaces(string):
    """ Returns a string with all spaces in 'string' have been replaced with '_'

    :param string: String to have spaces replaced
    :type: str

    :return: Supplied 'string' with spaces replaced with '_'
    :rtype: str
    """

    return string.replace(" ", "_")


# ================ notebook functions ==================#


def create_notebook(title):
    """ Create a notebook with foldername 'title'

    :param title: title of notebook
    :type title: str

    :return: True on successful creation of notebook's folder
    :rtype: bool
    """

    notebookpath = get_fullpath(change_spaces(title))

    if not os.path.exists(notebookpath):
        os.mkdir(notebookpath, mode=0o700)
    else:
        return False  # notebook already exists

    return os.path.exists(notebookpath)


def rename_notebook(oldtitle, newtitle):
    """ Renames existing notebook oldtitle as newtitle

    :param oldtitle: Title of existing notebook
    :type oldtitle: str

    :param newtitle: New Title for notebook
    :type newtitle: str

    :return: True on successful rename of notebook's folder
    :rtype: bool
    """

    frompath = get_fullpath(change_spaces(oldtitle))
    topath = get_fullpath(change_spaces(newtitle))

    if os.path.exists(frompath):
        return os.rename(frompath, topath)

    return False


def duplicate_notebook(oldtitle, newtitle):
    """ Duplicates an existing notebook oldtitle as newtitle with all notes duplicated.

    :param oldtitle: Title of existing notebook
    :type oldtitle: str

    :param newtitle: New Title for notebook
    :type newtitle: str

    :return: True on successful duplication of notebook's folder
    :rtype: bool
    """

    frompath = get_fullpath(change_spaces(oldtitle))
    topath = get_fullpath(change_spaces(newtitle))

    if os.path.exists(frompath) and not os.path.exists(topath):
        return shutil.copytree(frompath, topath)

    return False


def delete_notebook(title):
    """ Deletes an existing notebook oldtitle and included notes

    :param title: Title of existing notebook
    :type title: str

    :return: True on successful deletion of notebook's folder
    :rtype: bool
    """

    notebookpath = get_fullpath(change_spaces(title))

    if os.path.exists(notebookpath):
        shutil.rmtree(notebookpath)

    return not os.path.exists(notebookpath)


# ================= Note helper functions =================#


def import_note(filename):
    """ Creates and returns a note from a file assigning to plaintext or ciphertext

    :param filename: FULLPATH of filename
    :type filename: str

    :return note: An object of class note containing contents of file
    :rtype: Note object
    """

    if os.path.exists(filename):

        mynote = Notes(filename)
        _title, _ext = os.path.splitext(mynote.filename)

        if _ext == GPGEXT:

            # load cyphertext - edge case
            # importing an already encrypted note
            with open(mynote.filename, "r") as outp:  # pragma: no cover
                mynote.ciphertext = outp.read()
                mynote.plaintext = ""

        else:
            # load plaintext
            with open(mynote.title, "r") as outp:
                mynote.plaintext = outp.read()
                mynote.ciphertext = ""

        return mynote

    return None


def rename_note(oldname, newname):
    """ Renames a note on disk inside the currently USE'd notebook

    :param oldname: The old filename for note
    :type oldname: str

    :param newname: The new filename for note

    :type newname: str

    :return: True on sucessful renaming of note
    :rtype: bool
    """

    oldname = os.path.splitext(oldname)[0]
    newname = os.path.splitext(newname)[0]

    oldname = get_note_fullpath(oldname) + GPGEXT
    newname = get_note_fullpath(newname) + GPGEXT

    if not os.path.exists(oldname):
        return False

    shutil.move(oldname, newname)

    return os.path.exists(newname)


def duplicate_note(oldname, newname):
    """ Duplicates an encrypted note on disk inside the currently USE'd notebook

    :param oldname:  The new filename for note
    :type oldname: str

    :param newname: The new filename for note
    :type newname: str

    :return: True on successful rename of note
    :rtype: bool
    """

    oldname = os.path.splitext(oldname)[0]
    newname = os.path.splitext(newname)[0]

    oldname = get_note_fullpath(oldname) + GPGEXT
    newname = get_note_fullpath(newname) + GPGEXT

    if not os.path.exists(oldname):
        return False

    shutil.copy2(oldname, newname)

    return os.path.exists(newname)


def delete_note(filename):
    """ Deletes a note on disk inside the currently USE'd notebook

    :param filename:            A string containing the filename of note to be deleted
    :type filename: str

    :return: True on successful deletion of note
    :rtype: bool
    """

    filename = get_note_fullpath(os.path.splitext(filename)[0] + GPGEXT)

    if os.path.exists(filename):
        return os.remove(filename)

    return False


def copy_to_notebook(filename, notebook):
    """ Copies note from current USE'd notebook to another notebook

    :param filename: The filename of note to be copied
    :type filename: str

    :param notebook: The target notebook name
    :type notebook: str

    :returnl: True on successful copy
    :rtype: bool
    """

    note = get_note_fullpath(os.path.splitext(filename)[0] + GPGEXT)
    notebook = os.path.join(get_notesdir(), os.path.splitext(notebook)[0])

    if not os.path.exists(note) or not os.path.exists(notebook):
        return False

    shutil.copy2(note, notebook)

    return os.path.exists(notebook + note)


def move_to_notebook(filename, notebook):
    """ Moves a note from the currently USE'd notebook to another notebook

    :param filename: The filename to move
    :type filename: str

    :param notebook: The target notebook name
    :type filename: str

    :return: True on successful move of note to notebook
    :rtype: bool
    """

    filename = os.path.splitext(filename)[0] + GPGEXT
    note = get_note_fullpath(filename)
    notebook = os.path.join(get_notesdir(), os.path.splitext(notebook)[0])

    if not os.path.exists(note) or not os.path.exists(notebook):
        return False

    os.rename(note, os.path.join(notebook, filename))

    return os.path.exists(os.path.join(notebook, filename))


# ==================== CLASS NOTES =====================#


class Notes:
    """ Object for managing a noteand it's plaintext/ciphertext

    Attributes:

        title:      title of note
        filename:   filename of note
        ciphertext: string containing the ciphertext of note
        plaintext:  string containing the plaintext of note

    NB only one of either ciphertext or plaintext should be set at any time.
    """

    def __init__(self, title="", plaintext="", ciphertext="", filename=""):
        """ Notes class constructor. Valid constructors:

            Note()

            Note(title='my title')

            Note(title='my title', plaintext='plaintext')

            Note(title='my title', ciphertext='ascii encoded GPG ciphertext')

            Note(filename='my note filename.asc')

            Note(filename='my note filename')

        :param title: Note title (filename derived from title), default to ''
        :type title: str, optional

        :param plaintext: Plaintext of note, default to ''
        :type plaintext: str, optional

        :param ciphertext: GPG encrypted Ciphertext, default to ''
        :type ciphertext: str, optional

        :param filename: filename for note including extension
        :type filename: str
        """

        self.plaintext = plaintext
        self.ciphertext = ciphertext
        self.title = change_spaces(title)
        self.filename = change_spaces(filename)

        _config = get_config()
        _gpghome = _config["HOME"] + "/.gnupg"
        self.gpghandle = gnupg.GPG(gnupghome=_gpghome)
        self.gpgkey = _config["gpgkey"]

        if filename == "":
            self.set_filename(self.title)
        else:
            self.load_note(self.filename)

    def __repr__(self):
        return (
            f"['title': '{self.title}', 'filename': '{self.filename}', "
            + f"'ciphertext': '{self.ciphertext}', 'plaintext': '{self.plaintext}',]"
        )

    def add_extension(self):
        """ Appends '.asc' to the basename of self.filename

        :param: none

        :return: none
        """

        self.filename = os.path.splitext(self.filename)[0] + GPGEXT

    def remove_extension(self):  # pragma: no cover
        """ Removes extension from self.filename

        :param: none

        :return: none
        """

        self.filename = os.path.splitext(self.filename)[0]

    def get_extension(self):
        """ Returns extension of self.filename

        :param: none

        :return: self.filename's extension
        :rtype: str
        """

        return os.path.splitext(self.filename)[1]

    def set_filename(self, filename):
        """ Sets self.filename to 'filename'

        :param: set self.filename to 'filename'
        :type filename: str

        :return: none
        """

        self.filename = change_spaces(filename)

    def get_filename(self):
        """ Gets self.filename

        :param: none

        :return: self.filename
        :rtype: str
        """

        return self.filename

    def set_plaintext(self, plaintext):
        """ Sets self.plaintext = plaintext & self.ciphertext = ''

        :param plaintext:                  String containing plaintext
        :type plaintext:

        :return: none
        """

        self.plaintext = plaintext
        self.clear_ciphertext()

    def set_ciphertext(self, ciphertext):
        """ Sets self.ciphertext to ciphertext and
        self.plaintext = ''. Appends .asc to filename

        :param ciphertext: String containing the ciphertext
        :type ciphertext: str

        :return: none
        """

        self.ciphertext = ciphertext
        self.clear_plaintext()
        self.add_extension()

    def clear_plaintext(self):
        """ Sets self.plaintext to ''

        :param: none
        :return: none
        """

        self.plaintext = ""

    def clear_ciphertext(self):
        """ Sets self.ciphertext to ''

        :param: none
        :return: none
        """

        self.ciphertext = ""

    def save_ciphertext(self):
        """ Saves Ciphertext of note to file named self.filename adding the extension '.asc'

        :param: none

        :return: none
        """

        if self.filename == "":
            self.set_filename(self.title + GPGEXT)  # pragma: no cover
        else:
            self.set_filename(os.path.splitext(self.filename)[0] + GPGEXT)

        with open(get_note_fullpath(self.filename), "w") as outp:
            outp.write(self.ciphertext)

    def save_plaintext(self):
        """ Saves Plaintext of note to file named self.filename

        :param: none

        :return: none
        """

        if self.filename == "":
            self.set_filename(self.title)  # pragma: no cover
        else:
            self.set_filename(os.path.splitext(self.filename)[0])

        with open(get_note_fullpath(self.title), "w") as outp:
            outp.write(self.plaintext)

    def load_ciphertext(self):
        """ Loads ciphertext from file self.filename

        :param: none

        :return: none
        """

        with open(get_note_fullpath(self.filename), "r") as outp:
            self.ciphertext = outp.read()
            self.clear_plaintext()

    def load_plaintext(self):
        """ Loads plaintext from file self.filename

        :param: none

        :return: none
        """

        with open(get_note_fullpath(self.title), "r") as outp:
            self.plaintext = outp.read()
            self.clear_ciphertext()
        print(self)

    def load_note(self, filename):
        """ Opens file self.filename and assigns to plaintext or ciphertext

        :param filename: fullpath of filename
        :type filename: str

        :return: returns success or failure
        :rtype: bool
        """

        if not os.path.exists(get_note_fullpath(filename)):
            return False

        self.title, _ext = os.path.splitext(self.filename)

        if _ext == GPGEXT:
            self.load_ciphertext()
        else:
            self.load_plaintext()

        return True

    def is_encrypted(self):
        """ Check if note is encrypted

        :param: none

        :return: True if self.ciphertext != ''
        """

        return not self.ciphertext == ""

    def encrypt(self):
        """ Encrypts self.plaintext -> selfciphertext and resets self.plaintext

        :return: self.ciphertext
        :rtype: str
        """

        self.ciphertext = str(self.gpghandle.encrypt(self.plaintext, self.gpgkey))
        self.clear_plaintext()

        if self.get_extension() != GPGEXT:
            self.add_extension()

        return self.ciphertext

    def decrypt(self):
        """ Encrypts self.plaintext -> selfciphertext and resets self.plaintext

        :return: self.ciphertext
        :rtype: str
        """

        self.plaintext = str(self.gpghandle.decrypt(self.ciphertext))
        self.clear_ciphertext()

        return self.plaintext
