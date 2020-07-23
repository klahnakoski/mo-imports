# More Imports! - Delayed importing 

A couple of methods to make late importing cleaner

## Problem

Splitting code into modules is nice, but it can result in cyclic dependencies.  


**foos.py**

```python
from bars import bar

def foo():
    bar()
```

**bars.py**

```python
from foos import foo

def bar():
    foo()
```

> We are not concerned with the infinite recursion; this is only for demonstrating cyclic dependencies. 


## More Imports!

### Solution: Use `expect`/`export` pattern

All your cyclic dependencies are covered with this one pattern: Break cycles by `expect`ing a name in the first module, and let the second module `export` to the first when the value is available

**foos.py**

```python
from mo_imports import expect

bar, = expect("bar")

def foo():
    bar()
```

**bars.py**

```python
from mo_imports import export
from foos import foo

def bar():
    foo()

export("bars", bar)
```

**Benefits**
  
 
* every `expect` is verified to match with an `export` (and visa-versa)
* using an expected variable before `export` raises an error     
* code is run only once, at module load time, not later
* methods do not run import code
* all "imports" are at the top of the file


### Solution: Use `delay_import`

Provide a proxy which is responsible for import upon first use of the module variable.

**foos.py**

```python
from mo_imports import delay_import
from bars import bar

bar = delay_import("bars.bar")

def foo():
    bar()

```

**bars.py**

```python
from foos import foo

def bar():
    foo()
```

This is the cleanest, but it requires any of `__call__`, `__getitem__`, `__getattr__` to be called. Sentinals, placeholders, and default values can not be imported this way


  
## Other solutions

If you do not use `mo-imports` your import cycles can be broken using one of the following common patterns:


### Bad Solution: Keep in single file

You can declare yet-another-module that holds the cycles

**foosbars.py**

```python
    def foo():
        bar()

    def bar():
        foo()
```

but this breaks the code modularity



### Bad Solution: Use end-of-file imports

During import, setup of the first module is paused while it imports a second. A bottom-of-file import will ensure the first module is mostly setup to be used by the second. 

**foos.py**

```python
def foo():
    bar()

from bars import bar
```

**bars.py**

```python
def bar():
    foo()

from foos import foo
```

Linters do not like this pattern: You may miss imports, since these are hiding at the bottom.
    


### Bad Solution: Inline import

Import the name only when it is needed

**foos.py**

```python
def foo():
    from bars import bar
    bar()
```
    
**bars.py**


```python
def bar():
    from foos import foo
    foo()
```

This is fine for rarely run code, but there is an undesirable overhead because import is checked everytime the method is run. You may miss imports because they are hiding inline rather than at the top of the file.
  


### Bad Solution: Use the `_late_import()` pattern

When other options do not work work, then importing late is the remaining option

**foos.py**

```python
from bars import bar

def foo():
    bar()
```

**bars.py**

```python
foo = None

def _late_import():
    global foo
    from foos import foo
    _ = foo

def bar():
    if not foo:
        _late_import()
    foo()
```

Placeholders variables are added, which linters complain about type. There is the added `_late_import()` method. Run risk it is not run everywhere as needed.  This has less overhead than an import, but there is still a check.
 

