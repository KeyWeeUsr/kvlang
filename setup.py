from setuptools import setup, find_packages
from typing import Mapping as M, List, Union, Collection, Dict

NAME = "kvlang"
VERSION = "1.0.0"
KWARGS: M[str, str | bool | object] | M[str, Collection[str]] = {
    "name": NAME,
    "version": VERSION,
    "packages": find_packages(),
    "license": "MIT",
    "author": "Peter Badida",
    "author_email": "keyweeusr@gmail.com",
    "url": f"https://github.com/KeyWeeUsr/{NAME}",
    "download_url": (
        f"https://github.com/KeyWeeUsr/{NAME}/tarball/{VERSION}"
    ),
    "install_requires": ["lark>=1.2.2"],
    "extras_require": {
        "dev": [
            "pycodestyle", "pylint", "mypy",
            "types-setuptools"
        ],
        "kivy": [
            "kivy>=2.3.1"
        ],
        "release": ["wheel", "twine"]
    },
    "package_data": {
        "kvlang": ["*.lark"]
    },
    "include_package_data": True,
    "classifiers": [
        "Intended Audience :: End Users/Desktop",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only"
    ]
}


if __name__ == "__main__":
    setup(**KWARGS)
