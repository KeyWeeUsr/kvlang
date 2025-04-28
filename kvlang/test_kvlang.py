from unittest import TestCase, main, util
from lark import Tree, Token

util._MAX_LENGTH = 999999  # type: ignore


class TestGrammar(TestCase):
    def test_empty(self):
        from kvlang import parse
        self.assertEqual(parse(""), Tree(Token("RULE", "start"), []))

    def test_kivy_version_newlined(self):
        from kvlang import parse
        major = "1"
        minor = "0"
        text = f"#:kivy {major}.{minor}\n"
        self.assertEqual(parse(text), Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "kivy_version"), [
                        Token("WHITESPACE", " "),
                        Tree(Token("RULE", "version"), [
                            Token("V_MAJOR", major),
                            Token("V_MINOR", minor)
                        ])
                    ])
                ])
            ])
        ]))

    def test_kv_version_newlined(self):
        from kvlang import parse
        major = "1"
        minor = "0"
        text = f"#:kv {major}.{minor}\n"
        self.assertEqual(parse(text), Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "kv_version"), [
                        Token("WHITESPACE", " "),
                        Tree(Token("RULE", "version"), [
                            Token("V_MAJOR", major),
                            Token("V_MINOR", minor)
                        ])
                    ])
                ])
            ])
        ]))

    def test_kivy_kv_version_newlined(self):
        from kvlang import parse
        major = "1"
        minor = "0"
        text = f"#:kv {major}.{minor}\n#:kivy {major}.{minor}\n"
        self.assertEqual(parse(text), Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "kv_version"), [
                        Token("WHITESPACE", " "),
                        Tree(Token("RULE", "version"), [
                            Token("V_MAJOR", major),
                            Token("V_MINOR", minor)
                        ])
                    ])
                ])
            ]),
            Tree(Token("RULE", "special"), [
                Tree(Token("RULE", "special_directive"), [
                    Tree(Token("RULE", "kivy_version"), [
                        Token("WHITESPACE", " "),
                        Tree(Token("RULE", "version"), [
                            Token("V_MAJOR", major),
                            Token("V_MINOR", minor)
                        ])
                    ])
                ])
            ]),
        ]))

    def test_root_widget(self):
        from kvlang import parse
        text = "Widget:"
        self.assertEqual(parse(text), Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_tree"), [
                Tree(Token("RULE", "widget"), [Token("WIDGET", "Widget")])
            ])
        ]))

    def test_root_widget_with_comment_start(self):
        from kvlang import parse
        text = "Widget:#"
        self.assertEqual(parse(text), Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_tree"), [
                Tree(Token("RULE", "widget"), [
                    Token("WIDGET", "Widget")
                ])
            ])
        ]))

    def test_root_widget_with_comment(self):
        from kvlang import parse
        for prefix, comment in (("", "text"), (" ", " text"), ("    ", "    text")):
            text = f"Widget:{prefix}#{comment}"
            self.assertEqual(parse(text), Tree(Token("RULE", "start"), [
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "Widget")
                    ])
                ])
            ]))

    def test_root_widget_tree(self):
        from kvlang import parse
        for prefix, comment in (("", "text"), (" ", " text"), ("    ", "    text")):
            text = "Widget:\n Widget:\n  Widget:"
            self.assertEqual(parse(text), Tree(Token("RULE", "start"), [
                Tree(Token("RULE", "widget_tree"), [
                    Tree(Token("RULE", "widget"), [
                        Token("WIDGET", "Widget")
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "Widget")
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [Token("WIDGET", "Widget")])
                        ])
                    ])
                ])
            ]))

    def test_root_widget_rule(self):
        from kvlang import parse
        text = "<MyWidget>:"
        self.assertEqual(parse(text), Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Token("WIDGET_RULE", "MyWidget")
                ])
            ])
        ]))

    def test_root_widget_rule_with_comment_start(self):
        from kvlang import parse
        text = "<MyWidget>:#"
        self.assertEqual(parse(text), Tree(Token("RULE", "start"), [
            Tree(Token("RULE", "widget_rule_tree"), [
                Tree(Token("RULE", "widget_rule"), [
                    Token("WIDGET_RULE", "MyWidget")
                ])
            ])
        ]))

    def test_root_widget_rule_with_comment(self):
        from kvlang import parse
        for prefix, comment in (("", "text"), (" ", " text"), ("    ", "    text")):
            text = f"<MyWidget>:{prefix}#{comment}"
            self.assertEqual(parse(text), Tree(Token("RULE", "start"), [
                Tree(Token("RULE", "widget_rule_tree"), [
                    Tree(Token("RULE", "widget_rule"), [
                        Token("WIDGET_RULE", "MyWidget")
                    ])
                ])
            ]))

    def test_root_widget_tree(self):
        from kvlang import parse
        for prefix, comment in (("", "text"), (" ", " text"), ("    ", "    text")):
            text = "<MyWidget>:\n Widget:\n  Widget:"
            self.assertEqual(parse(text), Tree(Token("RULE", "start"), [
                Tree(Token("RULE", "widget_rule_tree"), [
                    Tree(Token("RULE", "widget_rule"), [
                        Token("WIDGET_RULE", "MyWidget")
                    ]),
                    Tree(Token("RULE", "widget_tree"), [
                        Tree(Token("RULE", "widget"), [
                            Token("WIDGET", "Widget")
                        ]),
                        Tree(Token("RULE", "widget_tree"), [
                            Tree(Token("RULE", "widget"), [
                                Token("WIDGET", "Widget")
                            ])
                        ])
                    ])
                ])
            ]))


class TestQuirks(TestCase):
    def test_number_as_variable(self):
        """
        supports quirks like these
        - #:set <any string> <any eval()-ready expr>
          - e.g.: #:set 0a "abc"
          (Pdb) from kivy.app import App
          (Pdb) App._running_app = App()
          (Pdb) from kivy.lang.parser import global_idmap
          (Pdb) global_idmap["0a"]
          3
        """
        from kvlang import parse
        for prefix, value in [("#:set 0a", "'thing'"), ("#:set 0a", '"thing"')]:
            self.assertEqual(
                parse(" ".join([prefix, value]) + "\n"),
                Tree(Token("RULE", "start"), [
                    Tree(Token("RULE", "special"), [
                        Tree(Token("RULE", "special_directive"), [
                            Tree(Token("RULE", "set"), [
                                Token("SET_NAME", "0a"),
                                Token("WHITESPACE", " "),
                                Token("SET_VALUE", value)
                            ])
                        ])
                    ])
                ])
            )


if __name__ == "__main__":
    main()
