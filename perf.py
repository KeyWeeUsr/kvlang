"""
Measure performance against Kivy core parser.
"""
from os import environ
from pathlib import Path
from statistics import mean
from time import time
from typing import Dict, Iterable

from kivy.lang import Builder, Parser  # type: ignore
from kvlang import parse

SAMPLES = int(environ.get("SAMPLES", "1"))


def load_kv() -> str:
    """Read complex kv string from Kivy docs."""
    lines = []
    modules = Path(__file__).parent / "modules"
    kivy = modules / "kivy"
    doc = kivy / "doc" / "sources" / "guide" / "widgets.rst"
    with open(doc, encoding="utf-8") as file:
        for _ in range(645):
            next(file)
        lines += [next(file)[4:] for _ in range(28)]
        return "".join(lines)


def measure_kivy_build_root(text: str) -> Iterable[float]:
    """Measure kv parsing in Kivy core."""
    kivy = []
    for _ in range(SAMPLES):
        kivy_before = time()
        Builder.load_string(text)
        kivy_after = time()
        kivy.append(kivy_after - kivy_before)
    return kivy


def measure_kivy_parse(text: str) -> Iterable[float]:
    """Measure kv parsing in Kivy core."""
    kivy = []
    for _ in range(SAMPLES):
        kivy_before = time()
        Parser(content=text)
        kivy_after = time()
        kivy.append(kivy_after - kivy_before)
    return kivy


def measure_kivy(text: str) -> Dict[str, Iterable[float]]:
    """Measure using Kivy core for handling Kvlang."""
    return {
        "parse": measure_kivy_parse(text),
        "build_root": measure_kivy_build_root(text)
    }


def measure_kvlang_build_root(text: str) -> Iterable[float]:
    """Measure Kvlang parsing into a tree."""
    return [-0.001]


def measure_kvlang_parse(text: str) -> Iterable[float]:
    """Measure Kvlang parsing into a tree."""
    kvlang = []
    for _ in range(SAMPLES):
        kvlang_before = time()
        parse(text)
        kvlang_after = time()
        kvlang.append(kvlang_after - kvlang_before)
    return kvlang


def measure_kvlang(text: str) -> Dict[str, Iterable[float]]:
    """Measure using Kvlang package for handling Kvlang."""
    return {
        "parse": measure_kvlang_parse(text),
        "build_root": measure_kvlang_build_root(text)
    }


def prettify(num: Iterable[float]) -> str:
    """Prettify number."""
    return f"{mean(num) * 1000:>10.5f}"


if __name__ == "__main__":
    print(f"{SAMPLES=}")
    KV = load_kv()

    print(
        prettify(measure_kivy(KV)["parse"]), "ms",
        "kivy.lang.Parser()"
    )
    print(
        prettify(measure_kvlang(KV)["parse"]), "ms",
        "kvlang.parse()"
    )
    print(
        prettify(measure_kivy(KV)["build_root"]), "ms",
        "kivy.lang.Builder()"
    )
    print(
        prettify(measure_kvlang(KV)["build_root"]), "ms",
        "kvlang.build_root()"
    )
