from setuptools import setup
from typing import Mapping, List, Union, Collection, Dict

KWARGS: Mapping[str, str] | Mapping[str, Collection[str]] = {
    "name": "kvlang",
    "install_requires": ["lark>=1.2.2"],
    "extras_require": {
        "dev": [
            "pycodestyle", "pylint", "mypy",
            "types-setuptools"
        ],
        "kivy": [
            "kivy>=2.3.1"
        ]
    }
}


if __name__ == "__main__":
    setup(**KWARGS)
