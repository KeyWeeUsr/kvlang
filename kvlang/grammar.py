from os.path import join

from kvlang.common import ROOT


def load_grammar() -> str:
    with open(join(ROOT, "kv.lark"), encoding="utf-8") as kv:
        return kv.read()
