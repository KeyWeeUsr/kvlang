# pylint: disable=import-outside-toplevel # always, to auto-clean import cache
# pylint: disable=missing-class-docstring,missing-function-docstring
"""
Test weird allowed things in Kvlang due to flexible token parsing or eval().
"""
import sys
from contextlib import ExitStack
from os import environ
from unittest import TestCase, main
from unittest.mock import patch, MagicMock

CHECKED_VERSIONS = (
    (2, 3, 1),
)
SAMPLE = """
#:set    x      "abc"
# -> whitespace around is stripped
# (6e23344/kivy/lang/parser.py#L554)

#:set     0x                1+2
# -> set 0x in global_idmap["0x"] = 3
# (ref: 6e23344/kivy/lang/parser.py#L512)

                               #:import        parser          kivy.lang.parser
                               # -> prefix whitespace is stripped too
                               # (6e23344/kivy/lang/parser.py#L497)

##:kv 3.0
# -> invalid directive, has to be stripped or implemented, eval-d as passing
# (6e23344/kivy/lang/parser.py#L578)

#-> indentation isn't strict to 4 spaces but has to be consistent
# (6e23344/kivy/lang/parser.py#L650)
BoxLayout:
 Widget:
  size_hint: None, None
  size: 0, 0
  on_parent: root.evaluated = True
 Label:
  # #:set directive evaluated prior to widget/properties
  # (6e23344/kivy/lang/parser.py#L599)
  # property eval-d prior and on_parent executed first but "on constant"/eval-d
  # (6e23344/kivy/lang/parser.py#L606)
  text: str(str(parser.global_idmap["!š"]) == "<built-in function time>")
  on_parent:
   # multiline not wrapped, but simply shoved to exec()
   # (6e23344/kivy/lang/parser.py#L181)
   assert str(parser.global_idmap["!š"]) == "<built-in function time>" \
   and \
   self.text == "True"
 Label:#:set no_value 123
  text: str(parser.global_idmap["0x"] == 3)
  on_parent:
   # multiline not wrapped, but simply shoved to exec()
   # (6e23344/kivy/lang/parser.py#L181)
   assert (
   parser.global_idmap["0x"] == 3
   and
   self.text == "True"
   )
        #:import !š time.time
    #:import sys sys
    # -> imported fine, in-between widget properties
    # (6e23344/kivy/lang/parser.py#L599)
  #:kivy 1.0
  #:kivy 1.1
  #:kivy 1.1.1
  #-> triggers version error during parsing, multiple occurrences are fine
  # (6e23344/kivy/lang/parser.py#L504)

 Label: #:set no_value 456
  text: str(str(sys) == "<module 'sys' (built-in)>") #:set no_value 789
  on_parent: #:set no_value 012
   assert str(sys) == "<module 'sys' (built-in)>" and self.text == "True"

 Label:
  text: str(parser.global_idmap.get("no_value") is None)
  on_parent:
   assert parser.global_idmap.get("no_value") is None and self.text == "True"
"""


def clean():
    for name in list(sys.modules.keys()):
        if not name.startswith("kivy"):
            continue
        del sys.modules[name]


class TestLangQuirks(TestCase):
    def setUp(self):
        environ["KIVY_NO_FILELOG"] = "1"
        environ["KIVY_NO_CONSOLELOG"] = "1"
        environ["KIVY_NO_CONFIG"] = "1"
        clean()

    def tearDown(self):
        clean()
        del environ["KIVY_NO_FILELOG"]
        del environ["KIVY_NO_CONSOLELOG"]
        del environ["KIVY_NO_CONFIG"]

    def test_quirks(self):
        ignored_mods = ("kivy._version", "kivy")
        patched_modules = {
            "kivy.compat": MagicMock(),
            "kivy.utils": MagicMock(),
            "kivy.logger": MagicMock(),
            "kivy.config": MagicMock(),
            "kivy.deps": MagicMock(__path__=[]),
            "kivy.modules": MagicMock(),
        }
        with patch.dict(sys.modules, patched_modules):
            # pylint: disable=import-error
            from kivy._version import (  # type: ignore
                __version__ as kivy_version
            )
            version = tuple(int(num) for num in kivy_version.split("."))
            for key, val in sys.modules.items():
                if not key.startswith("kivy"):
                    continue
                if not isinstance(val, MagicMock) and key not in ignored_mods:
                    # pylint: disable=broad-exception-raised
                    raise Exception(f"Unexpected import: {key} ({val})")

        if version not in CHECKED_VERSIONS:
            self.skipTest(
                "Unchecked version."
                " Check and add if the same or implement the new behavior."
            )

        # pylint: disable=import-error
        noises = [
            patch("kivy.uix.widget.EventLoop"),
            patch("kivy.uix.label.Label.fbind"),
            patch("kivy.uix.label.Label._create_label"),
            patch("kivy.lang.builder.BuilderBase._build_canvas"),
        ]
        with ExitStack() as patches:
            for noise in noises:
                patches.enter_context(noise)

            from kivy.lang import Builder  # type: ignore
            root = Builder.load_string(SAMPLE)
            assert root.evaluated
            assert len(root.children) == 1 + 4, root.children
            for child in root.children:
                if "Widget" in str(child):
                    continue
                assert child.text == "True"


if __name__ == "__main__":
    main()
