from mo_imports import export
from tests.modname_value2.bars import bar


def foo():
    bar()


export("tests.modname_value.bars", foo)
