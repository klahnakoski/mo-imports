from mo_imports import export
from tests.modname_name_value1.bars import bar


def foo():
    bar()


export("tests.modname_name_value1.bars", "alt", foo)
