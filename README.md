# kvlang

[![CI][ci-badge]][ci-workflow]
[![Coverage][coverage-badge]][coveralls]
[![GitHub version][gh-version-badge]][gh-version]
[![PyPI version][pypi-version-badge]][pypi-version]
[![PyPI - Python Version][pypi-py-version-badge]][pypi-py-version]
[![Latest release deps][pypi-release-badge]][pypi-release]
[![GitHub repo deps][gh-deps-badge]][gh-deps]

[![Downloads total][pepy-total]][pepy]
[![Downloads month][pepy-month]][pepy]
[![Downloads week][pepy-week]][pepy]
[![All Releases][gh-release-badge]][gh-release]
[![Code bytes][code-size]][gh]
[![Repo size][repo-size]][gh]

Grammar and parser for [Kv][kv] ([wiki][wiki]) as a more reliable approach for
reading the `.kv` files.

Install from PyPI:

```
pip install kvlang
```

or from the repo:

```
git clone https://github.com/KeyWeeUsr/kvlang
pip install -e .
# or
pip install git+https://github.com/KeyWeeUsr/kvlang.git
# or
pip install https://github.com/KeyWeeUsr/kvlang/zipball/master
# or
pip install https://github.com/KeyWeeUsr/kvlang/zipball/1.0.1
```

then

```python
from kvlang import parse

print(parse("#:kivy 2.3.1"))
# Tree(Token('RULE', 'start'), [Tree(Token('RULE', 'special'), [...])])

print(parse("#:kivy 2.3.1").pretty())
# start
#   special
#     special_directive
#       kivy_version
#         version
#           2
#           3
#           1
```

[kv]: https://kivy.org/doc/stable/guide/lang.html
[wiki]: https://en.wikipedia.org/wiki/Kivy_(framework)#Kv_language
[gh-version-badge]: https://badge.fury.io/gh/keyweeusr%2Fkvlang.svg
[gh-version]: https://badge.fury.io/gh/keyweeusr%2Fkvlang
[pypi-version-badge]: https://img.shields.io/pypi/v/kvlang.svg
[pypi-version]: https://pypi.org/project/kvlang/
[pypi-py-version-badge]: https://img.shields.io/pypi/pyversions/kvlang.svg
[pypi-py-version]: https://pypi.org/project/kvlang/
[pypi-release-badge]: https://img.shields.io/librariesio/release/pypi/kvlang.svg
[pypi-release]: https://libraries.io/pypi/kvlang
[gh-deps-badge]: https://img.shields.io/librariesio/github/keyweeusr/kvlang.svg
[gh-deps]: https://libraries.io/pypi/kvlang
[pepy-total]: https://pepy.tech/badge/kvlang
[pepy-month]: https://pepy.tech/badge/kvlang/month
[pepy-week]: https://pepy.tech/badge/kvlang/week
[pepy]: https://pepy.tech/project/kvlang
[gh-release-badge]: https://img.shields.io/github/downloads/keyweeusr/kvlang/total.svg
[gh-release]: https://github.com/KeyWeeUsr/kvlang/releases
[code-size]: https://img.shields.io/github/languages/code-size/keyweeusr/kvlang.svg
[repo-size]: https://img.shields.io/github/repo-size/keyweeusr/kvlang.svg
[gh]: https://github.com/KeyWeeUsr/kvlang
[ci-badge]: https://github.com/KeyWeeUsr/kvlang/actions/workflows/test.yml/badge.svg
[ci-workflow]: https://github.com/KeyWeeUsr/kvlang/actions/workflows/test.yml
[coverage-badge]: https://coveralls.io/repos/KeyWeeUsr/kvlang/badge.svg?branch=master
[coveralls]: https://coveralls.io/r/KeyWeeUsr/kvlang?branch=master
