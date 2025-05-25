# pylint: disable=missing-module-docstring
from typing import Type

from lark import Transformer, Lark, Tree
from lark.indenter import Indenter

from kvlang.grammar import load_grammar
from kvlang.transformer import KvTransformer


# pylint: disable=missing-class-docstring
# pylint: disable=too-few-public-methods
class TreeIndenter(Indenter):
    NL_type = '_NL'
    OPEN_PAREN_types = []
    CLOSE_PAREN_types = []
    INDENT_type = '_INDENT'
    DEDENT_type = '_DEDENT'
    tab_len = 4

    def handle_NL(self, token):
        if '\n' not in token:
            return
        yield from super().handle_NL(token)


def create_parser(transformer: Type[Transformer] = KvTransformer) -> Lark:
    # pylint: disable=missing-function-docstring
    return Lark(
        load_grammar(), parser="lalr",
        postlex=TreeIndenter(), transformer=transformer()
    )


def parse(text: str) -> Tree:
    """
    Main parsing function.
    """
    parser = create_parser()
    return parser.parse(text)
