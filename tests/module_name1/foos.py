from mo_imports import export
from tests.module_name1.bars import bar
from tests.module_name1 import bars


def foo():
    bar()


export(bars, "foos")
