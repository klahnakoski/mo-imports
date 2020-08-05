from mo_imports import export
from tests.module_value1.bars import bar
from tests.module_value1 import bars


def foo():
    bar()


export(bars, foo)
