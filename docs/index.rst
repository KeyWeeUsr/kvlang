.. kvlang documentation master file, created by
   sphinx-quickstart on Wed Apr 30 23:49:36 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Kvlang's documentation!
==================================

.. toctree::
   :maxdepth: 2
   :hidden:

   modules

Kvlang is a Python library for easier manipulation of `Kv language
<https://en.wikipedia.org/wiki/Kivy_(framework)#Kv_language>`_.

Install Kvlang
--------------

.. code:: sh

   pip install kvlang

Quick start
-----------

The most important function is :func:`parse() <kvlang.parse>` which provides
most of the core functionality. Simply pass your Kv string into it or load a
``.kv`` file's contents.

.. code:: python

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

Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
