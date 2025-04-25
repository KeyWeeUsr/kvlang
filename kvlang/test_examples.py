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


if __name__ == "__main__":
    main()
