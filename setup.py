import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()


# complete list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
# 'Development Status :: 5 - Production/Stable',
classifiers = [
    "Development Status :: 2 - Pre-Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Operating System :: Unix",
    "Operating System :: POSIX",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Utilities",
]

setuptools.setup(
    name="pynoteslib",
    version="0.5.0",
    license="MIT",
    description="Library of classes/functions for GPG encrypted notes",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Ian Stanley",
    author_email="iandstanley@gmail.com",
    url="https://github.com/Standard-Unix-Notes/pynoteslib",
    py_modules=["pynoteslib"],
    package_dir={"": "pynoteslib"},
    packages=setuptools.find_packages(where="pynoteslib"),
    python_requires=">=3.7",
    classifiers=classifiers,
    project_urls={
        "Documentation": "https://pynoteslib.readthedocs.io/",
        "Changelog": "https://pynoteslib.readthedocs.io/en/latest/changelog.html",
        "Issue Tracker": "https://github.com/Standard-Unix-Notes/pynoteslib/issues",
    },
    keywords=[
        "gnupg",
        "gpg",
        "encryption",
        "notes",
        "notebook",
        "pynotes",
    ],
    install_requires=[
        "python-gnupg ~= 0.4.7",
        "toml ~= 0.10.2",
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
            "wheel>=0.36.2",
            "black>=21.0",
            "bump2version~=1.0.1",
            "flake8>=3.9.2",
            "isort>=5.9.3",
        ],
        "docs": [
            "ReText",
            "Sphinx>=4.1.2",
            "sphinx-rtd-theme>=0.5.2",
        ],
    },
)
