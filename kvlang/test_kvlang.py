from unittest import TestCase, main, util
from lark import Tree, Token

util._MAX_LENGTH = 999999  # type: ignore


class TestGrammar(TestCase):
    def test_kivy_version_lone(self):
        from kvlang import parse
        text = "#:kivy 1.0"
        out = parse(text)
        self.assertEqual(out, Tree(
            Token('RULE', 'start'), [
                Tree(Token('RULE', 'header'), [
                    Token('KIVY_VERSION', text)
                ]),
                Tree(Token('RULE', 'content'), [])
            ]
        ))

    def test_kivy_version_newlined(self):
        from kvlang import parse
        text = "#:kivy 1.0\n"
        out = parse(text)
        self.assertEqual(out, Tree(
            Token('RULE', 'start'), [
                Tree(Token('RULE', 'header'), [
                    Token('KIVY_VERSION', text.rstrip("\n")),
                    Token("NEWLINE", "\n")
                ]),
                Tree(Token('RULE', 'content'), [])
            ]
        ))

    def test_kv_version_lone(self):
        from kvlang import parse
        text = "#:kv 1.0"
        out = parse(text)
        self.assertEqual(out, Tree(
            Token('RULE', 'start'), [
                Tree(Token('RULE', 'header'), [
                    Token('KV_VERSION', text)
                ]),
                Tree(Token('RULE', 'content'), [])
            ]
        ))

    def test_kv_version_newlined(self):
        from kvlang import parse
        text = "#:kv 1.0\n"
        out = parse(text)
        self.assertEqual(out, Tree(
            Token('RULE', 'start'), [
                Tree(Token('RULE', 'header'), [
                    Token('KV_VERSION', text.rstrip("\n")),
                    Token("NEWLINE", "\n")
                ]),
                Tree(Token('RULE', 'content'), [])
            ]
        ))

    def test_kivy_kv_version_newlined(self):
        from kvlang import parse
        kv = "#:kv 1.0"
        kivy = "#:kivy 1.0"
        out = parse("\n".join([kv, kivy]))
        self.assertEqual(out, Tree(
            Token('RULE', 'start'), [
                Tree(Token('RULE', 'header'), [
                    Token('KV_VERSION', kv),
                    Token("NEWLINE", "\n"),
                    Token('KIVY_VERSION', kivy)
                ]),
                Tree(Token('RULE', 'content'), [])
            ]
        ))


if __name__ == "__main__":
    main()
