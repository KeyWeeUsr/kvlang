from lark import Transformer, Lark, Tree

from kvlang.grammar import load_grammar
from kvlang.transformer import KvTransformer


def create_parser(transformer: type[Transformer] = KvTransformer) -> Lark:
    return Lark(load_grammar(), parser="lalr", transformer=transformer())


def parse(text: str) -> Tree:
    parser = create_parser()
    return parser.parse(text)
