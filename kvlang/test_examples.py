"""
Examples from Kivy documentation (MIT)
"""

from os.path import dirname, join, abspath
from unittest import TestCase, main, util

from lark import Tree, Token

util._MAX_LENGTH = 999999  # type: ignore
KIVY = join(dirname(dirname(abspath(__file__))), "kivy")

def load(name: str) -> str:
    folder = dirname(abspath(__file__))
    with open(join(folder, "examples", name), encoding="utf-8") as file:
        return file.read()


class TestExamples(TestCase):
    def test_getting_started(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Token("WIDGET_RULE", "LoginScreen")
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "GridLayout")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "rows"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", " 2 ")
                            ])
                        ])
                    ])
                ])
            ])
        ])

        doc = join(KIVY, "doc", "sources", "gettingstarted", "rules.rst")
        lines = []

        with open(doc, encoding="utf-8") as file:
            for line in file:
                if ".. code-block:: kv" not in line:
                    continue
                next(file)
                lines += [next(file)[4:] for _ in range(6)]

        self.assertEqual(parse("\n".join(lines)), tree)

    def test_getting_started_drawing(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Token("WIDGET_RULE", "MyWidget")
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
                                        " .5, .5, .5, .5"
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
                                        "PROPERTY_VALUE_INLINE", " self.size"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "pos"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", " self.pos")
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
                                Token("PROPERTY_VALUE_INLINE", " 'Button 1'")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", " 1, 1")
                            ])
                        ])
                    ])
                ])
            ])
        ])
        self.assertEqual(parse(load("pg-widgets.kv")), tree)

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
                                        "PROPERTY_VALUE_INLINE", " 'Button 1'"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "size_hint"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", " 0.5, 0.5")
                                ])
                            ])
                        ])
                    ])
                ])
            ]))

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
                                        "PROPERTY_VALUE_INLINE", " 'Button 1'"
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
                                        "PROPERTY_VALUE_INLINE", " 'Button 2'"
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
                                    "PROPERTY_VALUE_INLINE", " 'Button 1'"
                                )
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", " 0.5, 1")
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
                                    "PROPERTY_VALUE_INLINE", " 'Button 2'"
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
                                    "PROPERTY_VALUE_INLINE", ' "We Will"'
                                )
                            ])])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "pos"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", " 100, 100")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", " .2, .4")
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
                                    "PROPERTY_VALUE_INLINE", ' "Wee Wiill"'
                                )
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "pos"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", " 200, 200")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", " .4, .2")
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
                                    ' "ROCK YOU!!"'
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
                                    " {'x': .3, 'y': .6}"
                                )
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", " .5, .2")
                            ])
                        ])
                    ])
                ])
            ])
        ])
        self.assertEqual(parse(load("pg-widgets-floatlayout.kv")), tree)

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
                                        "PROPERTY_VALUE_INLINE", " 0, 1, 0, 1"
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
                                    Token("PROPERTY_VALUE_INLINE", " self.pos")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", " self.size"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
        self.assertEqual(parse(load("pg-widgets-floatlayout-canvas.kv")), tree)

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
                                        " 0, 1, 0, 1"
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
                                    Token("PROPERTY_VALUE_INLINE", " self.pos")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", " self.size"
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
                                    "PROPERTY_VALUE_INLINE", " 'Hello World!!'"
                                )
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", " .5, .5")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "pos_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE",
                                    " {'center_x':.5, 'center_y': .5}"
                                )
                            ])
                        ])
                    ])
                ])
            ])
        ])
        self.assertEqual(
            parse(load("pg-widgets-floatlayout-canvas-button.kv")), tree
        )

    def test_programming_guide_widgets_customlayout(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Token("WIDGET_RULE", "CustomLayout")
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
                                        "PROPERTY_VALUE_INLINE", " 0, 1, 0, 1"
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
                                    Token("PROPERTY_VALUE_INLINE", " self.pos")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", " self.size"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ]),
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Token("WIDGET_RULE", "RootWidget")
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
                                            " 'http://www.everythingzoomer.com"
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
                                    Token("PROPERTY_VALUE_INLINE", " 1, .5")
                                ])
                            ])
                        ]), Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "pos_hint"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        " {'center_x':.5, 'center_y': .5}"
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
                                        " 'http://www.stuffistumbledupon.com/"
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
                                            " 'http://www.stuffistumbledupon"
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
                                    Token("PROPERTY_VALUE_INLINE", " 1, .5")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "pos_hint"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        " {'center_x':.5, 'center_y': .5}"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
        self.assertEqual(parse(load("pg-widgets-customlayout.kv")), tree)

    def test_programming_guide_widgets_gridlayout(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Token("WIDGET_RULE", "GridLayout")
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
                                        " 10, 10, 10, 10"
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
                                            " '../examples/widgets/sequenced"
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
                                    Token("PROPERTY_VALUE_INLINE", " self.pos")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", " self.size"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ]),
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Token("WIDGET_RULE", "RootWidget")
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "GridLayout")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", " .9, .9")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "pos_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE",
                                    " {'center_x': .5, 'center_y': .5}"
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
                                        ' "I don\'t suffer from insanity, I'
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
                                        " self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", " 'top'")
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
                                            ' "When I was born I was so'
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
                                        " self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", " 'middle'")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "halign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", " 'center'")
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
                                            ' "A consultant is someone who'
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
                                        " self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", " 'bottom'")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "halign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE",
                                        " 'justify'"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
        self.assertEqual(parse(load("pg-widgets-gridlayout.kv")), tree)

    def test_programming_guide_widgets_custom_border(self):
        from kvlang import parse
        tree = Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Token("WIDGET_RULE", "CustomLayout")
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
                                        " 10, 10, 10, 10"
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
                                        " self.background_image.texture"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "pos"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", " self.pos")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "canvas_instruction_property"), [
                            Token("PROPERTY_NAME", "size"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", " self.size"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ]),
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Token("WIDGET_RULE", "RootWidget")
                ]),
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "CustomLayout")
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "size_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token("PROPERTY_VALUE_INLINE", " .9, .9")
                            ])
                        ])
                    ]),
                    Tree(Token("RULE", "widget_property"), [
                        Token("PROPERTY_NAME", "pos_hint"),
                        Tree(Token("RULE", "property_value"), [
                            Tree(Token("RULE", "property_value_inline"), [
                                Token(
                                    "PROPERTY_VALUE_INLINE",
                                    " {'center_x': .5, 'center_y': .5}"
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
                                        ' "I don\'t suffer from insanity, I'
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
                                        " self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", " 'top'")
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
                                        ' "When I was born I was so'
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
                                        " self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", " 'middle'")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "halign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", " 'center'")
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
                                        ' "A consultant is someone who'
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
                                        " self.width-20, self.height-20"
                                    )
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "valign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token("PROPERTY_VALUE_INLINE", " 'bottom'")
                                ])
                            ])
                        ]),
                        Tree(Token("RULE", "widget_property"), [
                            Token("PROPERTY_NAME", "halign"),
                            Tree(Token("RULE", "property_value"), [
                                Tree(Token("RULE", "property_value_inline"), [
                                    Token(
                                        "PROPERTY_VALUE_INLINE", " 'justify'"
                                    )
                                ])
                            ])
                        ])
                    ])
                ])
            ])
        ])
        self.assertEqual(parse(load("pg-widgets-custom-border.kv")), tree)


if __name__ == "__main__":
    main()
