# KVLANG_TEST_ROOT=./kvlang/tests VERSION=1.0.0 DRY=0 python release.py
from contextlib import ExitStack
from os import environ
from glob import glob
from sh import git, python  # type: ignore


def main():
    version = environ["VERSION"]
    dry = environ.get("DRY", "1")
    if dry == "1":
        git("clean", "-dxfn", _out="/dev/stdout")
        exit(0)
    git("clean", "-dxf", _out="/dev/stdout")

    dists = [
        ("sdist", f"dist/kvlang-{version}.tar.gz"),
        ("bdist_wheel", f"dist/kvlang-{version}-py3-none-any.whl")
    ]
    for cmd, dist in dists:
        with ExitStack() as stack:
            stack.callback(
                lambda: python("-m", "pip", "uninstall", "-y", "kvlang")
            )
            stack.callback(lambda: git("clean", "-dxf", "-e", "dist"))

            python("setup.py", cmd)
            python("-m", "pip", "install", dist)
            python(
                "-m", "unittest", *glob("./kvlang/tests/*.py"),
                _err="/dev/stdout"
            )


if __name__ == "__main__":
    main()
