from mo_imports import delay_import

foo = delay_import("tests.module_value1.foos.foo")

try:
    foo()
except Exception as cause:
    print("ok")
