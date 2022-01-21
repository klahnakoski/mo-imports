# encoding: utf-8
# THIS FILE IS AUTOGENERATED!
from __future__ import unicode_literals
from setuptools import setup
setup(
    author='Kyle Lahnakoski',
    author_email='kyle@lahnakoski.com',
    classifiers=["Development Status :: 4 - Beta","Topic :: Software Development :: Libraries","Topic :: Software Development :: Libraries :: Python Modules","License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)","Programming Language :: Python :: 3.7","Programming Language :: Python :: 3.9"],
    description='More Imports! - Delayed importing',
    extras_require={"tests":["mo-logs"]},
    install_requires=["mo-future==6.2.21303"],
    license='MPL 2.0',
    long_description='# More Imports! - Delayed importing \n\nA couple of methods to make late importing cleaner\n\n\n|Branch      |Status   |\n|------------|---------|\n|master      | [![Build Status](https://app.travis-ci.com/klahnakoski/mo-imports.svg?branch=master)](https://travis-ci.com/github/klahnakoski/mo-imports) |\n|dev         | [![Build Status](https://app.travis-ci.com/klahnakoski/mo-imports.svg?branch=dev)](https://travis-ci.com/github/klahnakoski/mo-imports)    |\n\n\n\n## Problem\n\nSplitting code into modules is nice, but it can result in cyclic dependencies.  \n\n\n**foos.py**\n\n```python\nfrom bars import bar\n\ndef foo():\n    bar()\n```\n\n**bars.py**\n\n```python\nfrom foos import foo\n\ndef bar():\n    foo()\n```\n\n> We are not concerned with the infinite recursion; this is only for demonstrating cyclic dependencies. \n\n\n## More Imports!\n\n### Solution: Use `expect`/`export` pattern\n\nAll your cyclic dependencies are covered with this one pattern: Break cycles by `expect`ing a name in the first module, and let the second module `export` to the first when the value is available\n\n**foos.py**\n\n```python\nfrom mo_imports import expect\n\nbar = expect("bar")\n\ndef foo():\n    bar()\n```\n\n**bars.py**\n\n```python\nfrom mo_imports import export\nfrom foos import foo\n\ndef bar():\n    foo()\n\nexport("bars", bar)\n```\n\n**Benefits**\n  \n \n* every `expect` is verified to match with an `export` (and visa-versa)\n* using an expected variable before `export` raises an error     \n* code is run only once, at module load time, not later\n* methods do not run import code\n* all "imports" are at the top of the file\n\n\n### Solution: Use `delay_import`\n\nProvide a proxy which is responsible for import upon first use of the module variable.\n\n**foos.py**\n\n```python\nfrom mo_imports import delay_import\nfrom bars import bar\n\nbar = delay_import("bars.bar")\n\ndef foo():\n    bar()\n\n```\n\n**bars.py**\n\n```python\nfrom foos import foo\n\ndef bar():\n    foo()\n```\n\nThis is the cleanest, but it requires any of `__call__`, `__getitem__`, `__getattr__` to be called. Sentinals, placeholders, and default values can not be imported this way\n\n\n  \n## Other solutions\n\nIf you do not use `mo-imports` your import cycles can be broken using one of the following common patterns:\n\n\n### Bad Solution: Keep in single file\n\nYou can declare yet-another-module that holds the cycles\n\n**foosbars.py**\n\n```python\n    def foo():\n        bar()\n\n    def bar():\n        foo()\n```\n\nbut this breaks the code modularity\n\n\n\n### Bad Solution: Use end-of-file imports\n\nDuring import, setup of the first module is paused while it imports a second. A bottom-of-file import will ensure the first module is mostly setup to be used by the second. \n\n**foos.py**\n\n```python\ndef foo():\n    bar()\n\nfrom bars import bar\n```\n\n**bars.py**\n\n```python\ndef bar():\n    foo()\n\nfrom foos import foo\n```\n\nLinters do not like this pattern: You may miss imports, since these are hiding at the bottom.\n    \n\n\n### Bad Solution: Inline import\n\nImport the name only when it is needed\n\n**foos.py**\n\n```python\ndef foo():\n    from bars import bar\n    bar()\n```\n    \n**bars.py**\n\n\n```python\ndef bar():\n    from foos import foo\n    foo()\n```\n\nThis is fine for rarely run code, but there is an undesirable overhead because import is checked everytime the method is run. You may miss imports because they are hiding inline rather than at the top of the file.\n  \n\n\n### Bad Solution: Use the `_late_import()` pattern\n\nWhen other bad solutions do not work work, then importing late is the remaining option\n\n**foos.py**\n\n```python\nfrom bars import bar\n\ndef foo():\n    bar()\n```\n\n**bars.py**\n\n```python\nfoo = None\n\ndef _late_import():\n    global foo\n    from foos import foo\n    _ = foo\n\ndef bar():\n    if not foo:\n        _late_import()\n    foo()\n```\n\nPlaceholders variables are added, which linters complain about type. There is the added `_late_import()` method. You risk it is not run everywhere as needed. This has less overhead than an inline import, but there is still a check.\n \n\n',
    long_description_content_type='text/markdown',
    name='mo-imports',
    packages=["mo_imports"],
    url='https://github.com/klahnakoski/mo-imports',
    version='7.109.22021'
)