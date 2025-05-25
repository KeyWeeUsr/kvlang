"""
Python reader for the Lark grammar file.
"""
from kvlang.common import ROOT


def load_grammar() -> str:
    """
    Load .lark file under UTF-8 encoding.
    """
    with open(ROOT / "kv.lark", encoding="utf-8") as kv:
        return kv.read()
