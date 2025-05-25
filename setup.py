"""
Simple packaging script.
"""
# pylint: disable=import-outside-toplevel

from pathlib import Path
from typing import Mapping as M, Collection

from setuptools import setup, find_packages, Command


class Style(Command):
    """Run Pycodestyle."""
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # pylint: disable=no-name-in-module
        from sh import pycodestyle  # type: ignore
        pycodestyle(
            "--ignore=none", "--exclude=modules",
            ".", "setup.py", "perf.py", "release.py"
        )


class Lint(Command):
    """Run Pylint."""
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # pylint: disable=no-name-in-module
        from sh import pylint  # type: ignore
        pylint(
            "--ignore=docs,modules",
            ".", "setup.py", "perf.py", "release.py"
        )


class Type(Command):
    """Run MyPy."""
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # pylint: disable=no-name-in-module
        from sh import mypy  # type: ignore
        mypy("--exclude", "modules", "--exclude", "build", ".")


class Docs(Command):
    """Generate RTD locally."""
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        # pylint: disable=no-name-in-module
        from sh import sphinx_apidoc, make  # type: ignore
        sphinx_apidoc("-o", "docs", "kvlang", "kvlang/tests")
        make("-C", "docs", "clean", "html")


NAME = "kvlang"
VERSION = "1.0.1"
ROOT = Path(__file__).parent
KWARGS: M[str, str | bool | object] | M[str, Collection[str]] = {
    "name": NAME,
    "version": VERSION,
    "packages": find_packages(exclude=["*.tests"]),
    "license": "MIT",
    "long_description": (ROOT / "README.md").read_text(),
    "long_description_content_type": "text/markdown",
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
            "types-setuptools", "sh", "sphinx"
        ],
        "kivy": [
            "kivy>=2.3.1"
        ],
        "release": ["wheel", "twine", "sh"]
    },
    "package_data": {
        "kvlang": ["*.lark"]
    },
    "include_package_data": True,
    "classifiers": [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only"
    ],
    "cmdclass": {
        "style": Style, "lint": Lint, "type": Type, "docs": Docs
    }
}


if __name__ == "__main__":
    setup(**KWARGS)
