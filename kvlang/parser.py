from lark import Transformer, Lark

from kvlang.grammar import load_grammar
from kvlang.transformer import KvTransformer


def create_parser(transformer: type[Transformer] = KvTransformer) -> Lark:
    return Lark(load_grammar(), parser="lalr", transformer=transformer())


def parse(text: str):
    parser = create_parser()
    return parser.parse(text)
