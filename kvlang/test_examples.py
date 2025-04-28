"""
Examples from Kivy documentation (MIT)
"""

from os.path import dirname, join, abspath
from unittest import TestCase, main, util

from lark import Tree, Token

util._MAX_LENGTH = 999999  # type: ignore


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
        self.assertEqual(parse(load("getting-started.kv")), tree)

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


if __name__ == "__main__":
    main()
