from pathlib import Path
import os
import sys
import traceback

from pypdf import PdfWriter
from pypdf.constants import PageLabelStyle


def wrap(f):
    def wrapped(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except BaseException as e:
            traceback.print_stack(file=sys.stderr)
            print(f"\033[91m{e}\033[0m", file=sys.stderr)
    return wrapped


@wrap
def writeFullScore():
    writer = PdfWriter("01 - Full score - Songs from The Princess.pdf")
    writer.add_outline_item("Cover", 0)
    writer.add_outline_item("1. Sweet and low", 2)
    writer.add_outline_item("2. The splendour falls", 6)
    writer.add_outline_item("3. Tears, idle tears", 10)
    writer.add_outline_item("4. O Swallow, Swallow", 13)
    writer.add_outline_item("(5). Home they brought her warrior dead", 15)
    writer.add_outline_item("5. Now sleeps the crimson petal", 17)
    writer.set_page_layout("/TwoPageRight")
    writer.set_page_label(0, 0, prefix="Cover")
    writer.set_page_label(1, 1, prefix="Contents")
    writer.set_page_label(2, 19, style=PageLabelStyle.DECIMAL)
    writer.write("Gustav Holst - Songs from the Princess.pdf")


@wrap
def writeReduction():
    writer = PdfWriter("01 - Piano score - Songs from The Princess.pdf")
    writer.add_outline_item("Cover", 0)
    writer.add_outline_item("1. Sweet and low", 2)
    writer.add_outline_item("2. The splendour falls", 6)
    writer.add_outline_item("3. Tears, idle tears", 10)
    writer.add_outline_item("4. O Swallow, Swallow", 13)
    writer.add_outline_item("(5). Home they brought her warrior dead", 15)
    writer.add_outline_item("5. Now sleeps the crimson petal", 17)
    writer.set_page_layout("/TwoPageRight")
    writer.set_page_label(0, 0, prefix="Cover")
    writer.set_page_label(1, 1, prefix="Contents")
    writer.set_page_label(2, 19, style=PageLabelStyle.DECIMAL)
    writer.write("Gustav Holst - Songs from the Princess, piano score.pdf")


def main():
    print("Processing Full Score")
    writeFullScore()


if __name__ == "__main__":
    main()
