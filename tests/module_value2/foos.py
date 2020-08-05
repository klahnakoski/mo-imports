from mo_imports import export
from tests.module_value2.bars import bar
from tests.module_value2 import bars


def foo():
    bar()


export(bars, foo)
