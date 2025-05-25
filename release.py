"""
Releasing script.

KVLANG_TEST_ROOT=./kvlang/tests VERSION=1.0.0 DRY=0 python release.py
"""

import sys
from contextlib import ExitStack
from os import environ
from glob import glob

# pylint: disable=no-name-in-module
from sh import git, python  # type: ignore


def main():
    """Entrypoint."""
    version = environ["VERSION"]
    dry = environ.get("DRY", "1")
    if dry == "1":
        # pylint: disable=unexpected-keyword-arg, too-many-function-args
        git("clean", "-dxfn", _out="/dev/stdout")
        sys.exit(0)
    # pylint: disable=unexpected-keyword-arg, too-many-function-args
    git("clean", "-dxf", _out="/dev/stdout")

    dists = [
        ("sdist", f"dist/kvlang-{version}.tar.gz"),
        ("bdist_wheel", f"dist/kvlang-{version}-py3-none-any.whl")
    ]
    for cmd, dist in dists:
        with ExitStack() as stack:
            stack.callback(
                # pylint: disable=too-many-function-args
                lambda: python("-m", "pip", "uninstall", "-y", "kvlang")
            )
            # pylint: disable=too-many-function-args
            stack.callback(lambda: git("clean", "-dxf", "-e", "dist"))

            python("setup.py", cmd)
            python("-m", "pip", "install", dist)
            python(
                "-m", "unittest", *glob("./kvlang/tests/*.py"),
                _err="/dev/stdout"
            )


if __name__ == "__main__":
    main()
