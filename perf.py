from os import environ
from pathlib import Path
from statistics import mean
from time import time

from kivy.lang import Builder
from kvlang import parse

SAMPLES = int(environ["SAMPLES"])


def load_kv() -> str:
    lines = []
    modules = Path(__file__).parent / "modules"
    kivy = modules / "kivy"
    doc = kivy / "doc" / "sources" / "guide" / "widgets.rst"
    with open(doc, encoding="utf-8") as file:
        for _ in range(644):
            next(file)
        for line in file:
            lines += [next(file)[4:] for _ in range(28)]
            break
        return "".join(lines)


def measure_kivy():
    kivy = []
    for _ in range(SAMPLES):
        kivy_before = time()
        Builder.load_string(kv)
        kivy_after = time()
        kivy.append(kivy_after - kivy_before)
    return kivy


def measure_kvlang():
    kvlang = []
    for _ in range(SAMPLES):
        kvlang_before = time()
        parse(kv)
        kvlang_after = time()
        kvlang.append(kvlang_after - kvlang_before)
    return kvlang


print(
    str(round(mean(measure_kivy()) * 1000, 5)).rjust(8, " "), "ms",
    "Kivy Builder.load_string()"
)
print(
    str(round(mean(measure_kvlang()) * 1000, 5)).rjust(8, " "), "ms",
    "Kvlang parse()"
)
