from mo_imports import DelayedValue


def make_value():
    return "hello world"


value = DelayedValue(make_value)
