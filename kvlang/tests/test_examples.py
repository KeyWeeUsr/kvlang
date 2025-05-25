"""
Parse examples from Kivy documentation (MIT) or other places.
"""

from pathlib import Path
from unittest import TestCase, main, util

from lark import Tree, Token

from kvlang.common import ROOT

# pylint: disable=protected-access
util._MAX_LENGTH = 999999  # type: ignore
MODULES = Path(ROOT).parent / "modules"
KIVY = MODULES / "kivy"
KVEXT = MODULES / "kvext"


def load(name: str) -> str:
    """
    Load from Kivy examples.
    """
    with open(Path(ROOT) / "examples" / name, encoding="utf-8") as file:
        return file.read()


class TestExamples(TestCase):
    """
    Main test case.
    """
    def test_getting_started(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Tree(Token("RULE", "widget_rule_name"), [
                        Token("WIDGET_NAME", "LoginScreen")
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "GridLayout")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "rows"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", "2 ")
                            ])
                        ])
                    ])
                ])
            ])
        ])

        doc = KIVY / "doc" / "sources" / "gettingstarted" / "rules.rst"
        lines = []

        with open(doc, encoding="utf-8") as file:
            for line in file:
                if ".. code-block:: kv" not in line:
                    continue
                next(file)
                lines += [next(file)[4:] for _ in range(6)]
                break

        self.assertEqual(parse("".join(lines)), tree)

    def test_getting_started_drawing(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Tree(Token("RULE", "widget_rule_name"), [
                        Token("WIDGET_NAME", "MyWidget")
                    ])
                ]),
                Tree(Token("RULE", "canvas_tree"), [
                    Tree(Token("RULE", "canvas"), [
                        Token("CANVAS", "canvas")
                    ]),
                    Tree(Token("RULE", "canvas_instruction_tree"), [
                        Tree(Token("RULE", "canvas_instruction"), [
                            Token("CANVAS_INSTRUCTION", "Color")
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "rgba"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        ".5, .5, .5, .5"
                                    )
                                ])
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "canvas_instruction_tree"), [
                        Tree(Token("RULE", "canvas_instruction"), [
                            Token("CANVAS_INSTRUCTION", "Ellipse")
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "self.size"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "pos"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "self.pos")
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
        self.assertEqual(parse(load("gs-drawing.kv")), tree)

    def test_programming_guide_widgets(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_tree"), [
                Tree(Token("RULE", "widget"), [
                    Token("WIDGET", "BoxLayout")
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "Button")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "text"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", "'Button 1'")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", "1, 1")
                            ])
                        ])
                    ])
                ])
            ])
        ])

        doc = KIVY / "doc" / "sources" / "guide" / "widgets.rst"
        lines = []

        with open(doc, encoding="utf-8") as file:
            for line in file:
                if ".. code-block:: kv" not in line:
                    continue
                next(file)
                lines += [next(file)[4:] for _ in range(6)]
                break

        self.assertEqual(parse("".join(lines)), tree)

    def test_programming_guide_widgets_float(self):
        from kvlang import parse
        self.assertEqual(
            parse(load("pg-widgets-float.kv")), Tree(Token("RULE", "start"), [
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "BoxLayout")
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "Button")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "'Button 1'"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "size_hint"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "0.5, 0.5")
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        )

    def test_programming_guide_widgets_multi(self):
        from kvlang import parse
        self.assertEqual(
            parse(load("pg-widgets-multi.kv")), Tree(Token("RULE", "start"), [
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "BoxLayout")
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "Button")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "'Button 1'"
                                    )
                                ])
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "Button")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "'Button 2'"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        )

    def test_programming_guide_widgets_multi_single_prop(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_tree"), [
                Tree(Token("RULE", "widget"), [
                    Token("WIDGET", "BoxLayout")
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "Button")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "text"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE", "'Button 1'"
                                )
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", "0.5, 1")
                            ])
                        ])
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "Button")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "text"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE", "'Button 2'"
                                )
                            ])
                        ])
                    ])
                ])
            ])
        ])
        self.assertEqual(parse(load("pg-widgets-multi-single-prop.kv")), tree)

    def test_programming_guide_widgets_floatlayout(self):
        from kvlang import parse

        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_tree"), [
                Tree(Token("RULE", "widget"), [
                    Token("WIDGET", "FloatLayout")
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "Button")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "text"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE", '"We Will"'
                                )
                            ])])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "pos"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", "100, 100")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", ".2, .4")
                            ])
                        ])
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "Button")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "text"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE", '"Wee Wiill"'
                                )
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "pos"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", "200, 200")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", ".4, .2")
                            ])
                        ])
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "Button")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "text"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE",
                                    '"ROCK YOU!!"'
                                )
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "pos_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE",
                                    "{'x': .3, 'y': .6}"
                                )
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", ".5, .2")
                            ])
                        ])
                    ])
                ])
            ])
        ])

        doc = KIVY / "doc" / "sources" / "guide" / "widgets.rst"
        lines = []

        with open(doc, encoding="utf-8") as file:
            for _ in range(280):
                next(file)
            for line in file:
                if ".. code-block:: kv" not in line:
                    continue
                next(file)
                lines += [next(file)[4:] for _ in range(15)]
                break

        self.assertEqual(parse("".join(lines)), tree)

    def test_programming_guide_widgets_floatlayout_canvas(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_tree"), [
                Tree(Token("RULE", "widget"), [
                    Token("WIDGET", "FloatLayout")
                ]),
                Tree(Token("RULE", "canvas_tree"), [
                    Tree(Token("RULE", "canvas"), [
                        Token("CANVAS", "canvas"),
                        Token("CANVAS_BEFORE", "before")
                    ]),
                    Tree(Token("RULE", "canvas_instruction_tree"), [
                        Tree(Token("RULE", "canvas_instruction"), [
                            Token("CANVAS_INSTRUCTION", "Color")
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "rgba"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "0, 1, 0, 1"
                                    )
                                ])
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "canvas_instruction_tree"), [
                        Tree(Token("RULE", "canvas_instruction"), [
                            Token("CANVAS_INSTRUCTION", "Rectangle")
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "pos"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "self.pos")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "self.size"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])

        doc = KIVY / "doc" / "sources" / "guide" / "widgets.rst"
        lines = []

        with open(doc, encoding="utf-8") as file:
            for _ in range(350):
                next(file)
            for line in file:
                if ".. code-block:: kv" not in line:
                    continue
                next(file)
                lines += [next(file)[4:] for _ in range(9)]
                break

        self.assertEqual(parse("".join(lines)), tree)

    def test_programming_guide_widgets_floatlayout_canvas_button(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_tree"), [
                Tree(Token("RULE", "widget"), [
                    Token("WIDGET", "FloatLayout")
                ]),
                Tree(Token("RULE", "canvas_tree"), [
                    Tree(Token("RULE", "canvas"), [
                        Token("CANVAS", "canvas"),
                        Token("CANVAS_BEFORE", "before")
                    ]),
                    Tree(Token("RULE", "canvas_instruction_tree"), [
                        Tree(Token("RULE", "canvas_instruction"), [
                            Token("CANVAS_INSTRUCTION", "Color")
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "rgba"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "0, 1, 0, 1"
                                    )
                                ])
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "canvas_instruction_tree"), [
                        Tree(Token("RULE", "canvas_instruction"), [
                            Token("CANVAS_INSTRUCTION", "Rectangle")
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "pos"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "self.pos")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "self.size"
                                    )
                                ])
                            ])
                        ])
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "Button")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "text"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE", "'Hello World!!'"
                                )
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", ".5, .5")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "pos_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE",
                                    "{'center_x':.5, 'center_y': .5}"
                                )
                            ])
                        ])
                    ])
                ])
            ])
        ])

        doc = KIVY / "doc" / "sources" / "guide" / "widgets.rst"
        lines = []

        with open(doc, encoding="utf-8") as file:
            for _ in range(414):
                next(file)
            for line in file:
                lines += [next(file)[4:] for _ in range(12)]
                break

        self.assertEqual(parse("".join(lines)), tree)

    def test_programming_guide_widgets_customlayout(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Tree(Token("RULE", "widget_rule_name"), [
                        Token("WIDGET_NAME", "CustomLayout")
                    ])
                ]),
                Tree(Token("RULE", "canvas_tree"), [
                    Tree(Token("RULE", "canvas"), [
                        Token("CANVAS", "canvas"),
                        Token("CANVAS_BEFORE", "before")
                    ]),
                    Tree(Token("RULE", "canvas_instruction_tree"), [
                        Tree(Token("RULE", "canvas_instruction"), [
                            Token("CANVAS_INSTRUCTION", "Color")
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "rgba"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "0, 1, 0, 1"
                                    )
                                ])
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "canvas_instruction_tree"), [
                        Tree(Token("RULE", "canvas_instruction"), [
                            Token("CANVAS_INSTRUCTION", "Rectangle")
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "pos"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "self.pos")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "self.size"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ]),
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Tree(Token("RULE", "widget_rule_name"), [
                        Token("WIDGET_NAME", "RootWidget")
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "CustomLayout")
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "AsyncImage")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "source"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        (
                                            "'http://www.everythingzoomer.com"
                                            "/wp-content/uploads/2013/01/"
                                            "Monday-joke-289x277.jpg'"
                                        )
                                    )
                                ])
                            ])
                        ]), Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "size_hint"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "1, .5")
                                ])
                            ])
                        ]), Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "pos_hint"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "{'center_x':.5, 'center_y': .5}"
                                    )
                                ])
                            ])
                        ])
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "AsyncImage")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "source"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE", (
                                        "'http://www.stuffistumbledupon.com/"
                                        "wp-content/uploads/2012/05/Have-you-"
                                        "seen-this-dog-because-its-awesome-"
                                        "meme-puppy-doggy.jpg'"
                                    )
                                )
                            ])
                        ])
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "CustomLayout")
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "AsyncImage")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "source"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        (
                                            "'http://www.stuffistumbledupon"
                                            ".com/wp-content/uploads/2012/04/"
                                            "Get-a-Girlfriend-Meme-empty-"
                                            "wallet.jpg'"
                                        )
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "size_hint"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "1, .5")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "pos_hint"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "{'center_x':.5, 'center_y': .5}"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])

        doc = KIVY / "doc" / "sources" / "guide" / "widgets.rst"
        lines = []

        with open(doc, encoding="utf-8") as file:
            for _ in range(510):
                next(file)
            for line in file:
                lines += [next(file)[4:] for _ in range(21)]
                break

        self.assertEqual(parse("".join(lines)), tree)

    def test_programming_guide_widgets_gridlayout(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Tree(Token("RULE", "widget_rule_name"), [
                        Token("WIDGET_NAME", "GridLayout")
                    ])
                ]),
                Tree(Token("RULE", "canvas_tree"), [
                    Tree(Token("RULE", "canvas"), [
                        Token("CANVAS", "canvas"),
                        Token("CANVAS_BEFORE", "before")
                    ]),
                    Tree(Token("RULE", "canvas_instruction_tree"), [
                        Tree(Token("RULE", "canvas_instruction"), [
                            Token("CANVAS_INSTRUCTION", "BorderImage")
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "border"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "10, 10, 10, 10"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "source"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        (
                                            "'../examples/widgets/sequenced"
                                            "_images/data/images/button_white"
                                            ".png'"
                                        )
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "pos"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "self.pos")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "self.size"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ]),
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Tree(Token("RULE", "widget_rule_name"), [
                        Token("WIDGET_NAME", "RootWidget")
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "GridLayout")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", ".9, .9")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "pos_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE",
                                    "{'center_x': .5, 'center_y': .5}"
                                )
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "rows"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", "1")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "Label")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        '"I don\'t suffer from insanity, I'
                                        ' enjoy every minute of it"'
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text_size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "'top'")
                                ])
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "Label")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        (
                                            '"When I was born I was so'
                                            ' surprised; I didn\'t speak for a'
                                            ' year and a half."'
                                        )
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text_size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "'middle'")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "halign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "'center'")
                                ])
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "Label")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        (
                                            '"A consultant is someone who'
                                            ' takes a subject you understand'
                                            ' and makes it sound confusing"'
                                        )
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text_size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "'bottom'")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "halign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "'justify'"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])

        doc = KIVY / "doc" / "sources" / "guide" / "widgets.rst"
        lines = []

        with open(doc, encoding="utf-8") as file:
            for _ in range(576):
                next(file)
            for line in file:
                lines += [next(file)[4:] for _ in range(28)]
                break

        self.assertEqual(parse("".join(lines)), tree)

    def test_programming_guide_widgets_custom_border(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Tree(Token("RULE", "widget_rule_name"), [
                        Token("WIDGET_NAME", "CustomLayout")
                    ])
                ]),
                Tree(Token("RULE", "canvas_tree"), [
                    Tree(Token("RULE", "canvas"), [
                        Token("CANVAS", "canvas"),
                        Token("CANVAS_BEFORE", "before")
                    ]),
                    Tree(Token("RULE", "canvas_instruction_tree"), [
                        Tree(Token("RULE", "canvas_instruction"), [
                            Token("CANVAS_INSTRUCTION", "BorderImage")
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "border"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "10, 10, 10, 10"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "texture"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "self.background_image.texture"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "pos"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "self.pos")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "self.size"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ]),
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Tree(Token("RULE", "widget_rule_name"), [
                        Token("WIDGET_NAME", "RootWidget")
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "CustomLayout")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", ".9, .9")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "pos_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE",
                                    "{'center_x': .5, 'center_y': .5}"
                                )
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "rows"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", "1")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "Label")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        '"I don\'t suffer from insanity, I'
                                        ' enjoy every minute of it"'
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text_size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "'top'")
                                ])
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "Label")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        '"When I was born I was so'
                                        ' surprised; I didn\'t speak for a'
                                        ' year and a half."'
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text_size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "'middle'")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "halign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "'center'")
                                ])
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "Label")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        '"A consultant is someone who'
                                        ' takes a subject you understand'
                                        ' and makes it sound confusing"'
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "text_size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        "self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", "'bottom'")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "halign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "'justify'"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])

        doc = KIVY / "doc" / "sources" / "guide" / "widgets.rst"
        lines = []

        with open(doc, encoding="utf-8") as file:
            for _ in range(644):
                next(file)
            for line in file:
                lines += [next(file)[4:] for _ in range(28)]
                break

        self.assertEqual(parse("".join(lines)), tree)

    def test_kvext_kvext(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "set"), [
                        Token("SET_NAME", "__KV_EXT_V__"),
                        Token("SET_VALUE", "(0, 0, 1)")
                    ])
                ])
            ]),
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "set"), [
                        Token("SET_NAME", "_eat"),
                        Token("SET_VALUE", "lambda *a, **kw: None")
                    ])
                ])
            ]),
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "set"), [
                        Token("SET_NAME", "_for"),
                        Token("SET_VALUE", (
                            "lambda N, c, a=(), kw={}:"
                            " _eat([c(*a, **kw) for i in range(N)])"
                        ))
                    ])
                ])
            ]),
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "set"), [
                        Token("SET_NAME", "_forc"),
                        Token("SET_VALUE", (
                            "lambda N, c, a, kw={}:"
                            " _eat([c(a(**kw), **kw) for i in range(N)])"
                        ))
                    ])
                ])
            ]),
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "set"), [
                        Token("SET_NAME", "_forw"),
                        Token("SET_VALUE", (
                            "lambda p, N, wdg, kw={}:"
                            " _eat([p.add_widget("
                            "wdg(**kw)) for i in range(N)])"
                        ))
                    ])
                ])
            ]),
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "set"), [
                        Token("SET_NAME", "_forws"),
                        Token("SET_VALUE", (
                            "lambda p, wdgs=[]:"
                            " _eat([p.add_widget("
                            "wdgs[i][0](**wdgs[i][1]))"
                            " for i in range(len(wdgs))])"
                        ))
                    ])
                ])
            ]),
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "set"), [
                        Token("SET_NAME", "_swapw"),
                        Token("SET_VALUE", (
                            "lambda a, b: _eat(["
                            "setattr(a, '__swap_ib',"
                            " b.parent.children.index(b)),"
                            "setattr(a, '__swap_ia',"
                            " a.parent.children.index(a)),"
                            "b.parent.remove_widget(b),"
                            " a.parent.add_widget(b, a.__swap_ia),"
                            "a.parent.remove_widget(a),"
                            " b.parent.add_widget(a, a.__swap_ib),"
                            "delattr(a, '__swap_ia'),"
                            " delattr(a, '__swap_ib'),])"
                        ))
                    ])
                ])
            ])
        ])

        with open(KVEXT / "kvext.kv") as file:
            self.assertEqual(parse(file.read()), tree)

    def test_kvext_example(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "include"), [
                        Token("INCLUDE_NAME", "kvext.kv")
                    ])
                ])
            ]),
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "import"), [
                        Token("IMPORT_NAME", "Factory"),
                        Token("IMPORT_MODULE", "kivy.factory.Factory")
                    ])
                ])
            ]),
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "import"), [
                        Token("IMPORT_NAME", "r"),
                        Token("IMPORT_MODULE", "random.random")
                    ])
                ])
            ]),
            Tree(Token("RULE", "widget_tree"), [
                Tree(Token("RULE", "widget"), [
                    Token("WIDGET", "BoxLayout")
                ]),
                Tree(Token("RULE", "widget_property"), [
                    Token("PROPERTY_NAME", "orientation"),
                    Tree(Token("RULE", "property_value"), [
                        Tree(Token("RULE", "property_value_inline"), [
                            Token("PROPERTY_VALUE_INLINE", "'vertical'")
                        ])
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "BoxLayout")
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "BoxLayout")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "orientation"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "'vertical'"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Button")
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "text"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE", "'_for'"
                                        )
                                    ])
                                ])
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "on_release"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE",
                                            "_for(5, print, (str(r()), ))"
                                        )
                                    ])
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Button")
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "text"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE", "'_forc'"
                                        )
                                    ])
                                ])
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "on_release"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE",
                                            "_forc(5, print, r)"
                                        )
                                    ])
                                ])
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "BoxLayout")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "orientation"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "'vertical'"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Button")
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "text"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE", "'_forw'"
                                        )
                                    ])
                                ])
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "on_release"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_block"
                                    ), [
                                        Tree(Token(
                                            "RULE", "property_value_block_line"
                                        ), [
                                            Token(
                                                "PROPERTY_VALUE_BLOCK_LINE",
                                                (
                                                    "_forw(grid, 5,"
                                                    " Factory.ForWidget,"
                                                    " {'text': 'Hello!'})"
                                                )
                                            )
                                        ])
                                    ])
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Button")
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "text"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE",
                                            "'_forws'"
                                        )
                                    ])
                                ])
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "on_release"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_block"
                                    ), [
                                        Tree(Token(
                                            "RULE", "property_value_block_line"
                                        ), [
                                            Token(
                                                "PROPERTY_VALUE_BLOCK_LINE",
                                                "_forws(grid, ["
                                            )
                                        ]),
                                        Tree(Token(
                                            "RULE", "property_value_block_line"
                                        ), [
                                            Token(
                                                "PROPERTY_VALUE_BLOCK_LINE",
                                                (
                                                    "[Factory.Spinner, {}],"
                                                    " [Factory.Button,"
                                                    " {'text':'blob'}],"
                                                )
                                            )
                                        ]),
                                        Tree(Token(
                                            "RULE", "property_value_block_line"
                                        ), [
                                            Token(
                                                "PROPERTY_VALUE_BLOCK_LINE",
                                                "[Factory.Label,"
                                                " {'color': (1, 0, 0, 1),"
                                                " 'text':'blob'}]])"
                                            )
                                        ])
                                    ])
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Button")
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "text"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE",
                                            "'clear grid'"
                                        )
                                    ])
                                ])
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "on_release"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE",
                                            "grid.clear_widgets()"
                                        )
                                    ])
                                ])
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "BoxLayout")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "orientation"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "'vertical'"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Button")
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "id"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token("PROPERTY_VALUE_INLINE", "id_a")
                                    ])
                                ])
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "text"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token("PROPERTY_VALUE_INLINE", "'a'")
                                    ])
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Button")
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "id"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token("PROPERTY_VALUE_INLINE", "id_b")
                                    ])
                                ])
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "text"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token("PROPERTY_VALUE_INLINE", "'b'")
                                    ])
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Button")
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "id"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token("PROPERTY_VALUE_INLINE", "id_c")
                                    ])
                                ])
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "text"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token("PROPERTY_VALUE_INLINE", "'c'")
                                    ])
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Button")
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "id"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token("PROPERTY_VALUE_INLINE", "id_d")
                                    ])
                                ])
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "text"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token("PROPERTY_VALUE_INLINE", "'d'")
                                    ])
                                ])
                            ])
                        ]),
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "BoxLayout")
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "orientation"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", "'vertical'"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Button")
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "text"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE",
                                            "'swap a<->d'"
                                        )
                                    ])
                                ])
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "on_release"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE",
                                            "_swapw(id_a, id_d)"
                                        )
                                    ])
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Button")
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "text"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE",
                                            "'swap b<->c'"
                                        )
                                    ])
                                ])
                            ]),
                            Tree(Token("RULE", "widget_property"), [
                                Token("PROPERTY_NAME", "on_release"),
                                Tree(Token("RULE", "property_value"), [
                                    Tree(Token(
                                        "RULE", "property_value_inline"
                                    ), [
                                        Token(
                                            "PROPERTY_VALUE_INLINE",
                                            "_swapw(id_b, id_c)"
                                        )
                                    ])
                                ])
                            ])
                        ]),
                    ])
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "GridLayout")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "id"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", "grid")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "cols"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", "20")
                            ])
                        ])
                    ])
                ])
            ]),
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Tree(Token("RULE", "widget_rule_name"), [
                        Token("WIDGET_NAME", "ForWidget"),
                        Tree(Token("RULE", "base_classes"), [
                            Token("CLASS_NAME", "ButtonBehavior"),
                            Token("CLASS_NAME", "Label")
                        ])
                    ])
                ]),
                Tree(Token("RULE", "widget_property"), [
                    Token("PROPERTY_NAME", "on_parent"),
                    Tree(Token("RULE", "property_value"), [
                        Tree(Token("RULE", "property_value_inline"), [
                            Token("PROPERTY_VALUE_INLINE", "self.dummy += 1")
                        ])
                    ])
                ]),
                Tree(Token("RULE", "widget_property"), [
                    Token("PROPERTY_NAME", "dummy"),
                    Tree(Token("RULE", "property_value"), [
                        Tree(Token("RULE", "property_value_inline"), [
                            Token("PROPERTY_VALUE_INLINE", "0")
                        ])
                    ])
                ]),
                Tree(Token("RULE", "widget_property"), [
                    Token("PROPERTY_NAME", "on_dummy"),
                    Tree(Token("RULE", "property_value"), [
                        Tree(Token("RULE", "property_value_inline"), [
                            Token(
                                "PROPERTY_VALUE_INLINE",
                                "if self.dummy <= 2:"
                                " _forw(self.parent, 6, Factory.Button)"
                            )
                        ])
                    ])
                ])
            ])
        ])

        doc = KVEXT / "example.py"
        lines = []

        with open(doc, encoding="utf-8") as file:
            for _ in range(3):
                next(file)
            lines += [next(file) for _ in range(61)]

        self.assertEqual(parse("".join(lines)), tree)


if __name__ == "__main__":
    main()
