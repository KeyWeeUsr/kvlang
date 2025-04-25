"""
Examples from Kivy documentation (MIT)
"""

from unittest import TestCase, main, util
from lark import Tree, Token

util._MAX_LENGTH = 999999  # type: ignore

# 6e23344/doc/sources/gettingstarted/rules.rst#L18
GETTING_STARTED = """
<LoginScreen>:  # every class in your app can be represented by a rule like
                # this in the kv file
    GridLayout: # this is how you add your widget/layout to the parent
                # (note the indentation).
        rows: 2 # this how you set each property of your widget/layout
"""

# 6e23344/doc/sources/images/gs-drawing.png
GS_DRAWING = """
#kivy 1.0
<MyWidget>
    canvas:
        Color:
            rgba: .5,.5,.5,.5
        Ellipse:
            size: self.size
            pos: self.pos
"""


class TestExamples(TestCase):
    def test_getting_started(self):
        from kvlang import parse
        self.assertEqual(parse(GETTING_STARTED), Tree(Token('RULE', 'start'), [
            Tree(Token('RULE', 'widget_rule_tree'), [
                Tree(Token('RULE', 'widget_rule'), [
                    Token('WIDGET_RULE', 'LoginScreen')
                ]),
                Tree(Token('RULE', 'widget_tree'), [
                    Tree(Token('RULE', 'widget'), [
                        Token('WIDGET', 'GridLayout')
                    ]),
                    Tree(Token('RULE', 'widget_property'), [
                        Token('PROPERTY_NAME', 'rows'),
                        Token('PROPERTY_VALUE', '2')
                    ])
                ])
            ])
        ]))

    def test_getting_started_drawing(self):
        from kvlang import parse
        self.assertEqual(parse(GS_DRAWING), Tree(Token('RULE', 'start'), [
            Tree(Token('RULE', 'widget_rule_tree'), [
                Tree(Token('RULE', 'widget_rule'), [
                    Token('WIDGET_RULE', 'MyWidget')
                ]),
                Tree(Token('RULE', 'widget_tree'), [
                    Tree(Token('RULE', 'widget'), [
                        Token('WIDGET', 'canvas')
                    ]),
                    Tree(Token('RULE', 'widget_tree'), [
                        Tree(Token('RULE', 'widget'), [
                            Token('WIDGET', 'Color')
                        ]),
                        Tree(Token('RULE', 'widget_property'), [
                            Token('PROPERTY_NAME', 'rgba'),
                            Token('PROPERTY_VALUE', '.5,.5,.5,.5')
                        ])
                    ]),
                    Tree(Token('RULE', 'widget_tree'), [
                        Tree(Token('RULE', 'widget'), [
                            Token('WIDGET', 'Ellipse')
                        ]),
                        Tree(Token('RULE', 'widget_property'), [
                            Token('PROPERTY_NAME', 'size'),
                            Token('PROPERTY_VALUE', 'self.size')
                        ]),
                        Tree(Token('RULE', 'widget_property'), [
                            Token('PROPERTY_NAME', 'pos'),
                            Token('PROPERTY_VALUE', 'self.pos')
                        ])
                    ])
                ])
            ])
        ]))


if __name__ == "__main__":
    main()
