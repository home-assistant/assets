# Python Quickstart

Die Python-Dokumentation bietet ein umfangreicheres [Tutorial](https://docs.python.org/3.5/tutorial/index.html) an. Die Informationen an dieser Stelle sollen nur helfen, schnell einen Überblick über Python zu erhalten und den Weg zu einer eigenen Home Assistant-Platform oder Komponente ebenen.

- [Python-Dokumentation](https://docs.python.org/3.5/index.html)
- [Python FAQ](https://docs.python.org/3.5/faq/index.html)
- [The Python Standard Library](https://docs.python.org/3.5/library/)

## Gut zu wissen...

- Python ist sensible. Einrückungen! (vier Leerschläge gemäss [PEP8](https://www.python.org/dev/peps/pep-0008/) oder einfach Tab in interaktiver Shell)
- Keine Terminierung von Zeilen nötig
- Keine starke Typisierung (dynamische Typisierung) im Gegensatz zu Java, `float f; f = 3.1415F;`, und anderen
- Scope wird nicht forciert (keine `public`, `private`, and `protected` wie bei anderen Sprachen)
- `None` entspricht `nil` oder `Null`. `False` und `True` nicht `false` und `true`
- Sind bei Tests `false`: `None`, `False`, `0`, `0.0`, `''`, `()`, `[]`, `{}`
- Mehrfachzuweisung sind möglich `a, b = 1, 10` oder 

## Glossar

- [PEP](https://www.python.org/dev/peps/): Python Enhancement Proposals (ähnlich wie JSR bei Java) 
- [PyPI](https://pypi.python.org/pypi): Python Package Index

## Interaktive Shell

Wie `irb` in Ruby.

```bash
$ python3
Python 3.5.2 (default, Oct 14 2016, 12:54:53) 
[GCC 6.2.1 20160916 (Red Hat 6.2.1-2)] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Nutzen der Online-Hilfe für `print()`, welche `System.out.println("String")` in Java entspricht.

```bash
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.
```

Anzeigen aller Methoden eines Objekts.

```bash
>>> dir(5)
['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__',
```

Den Docstring einer Methode anzeigen.

```bash
>>> abs.__doc__
'Return the absolute value of the argument.'
```

### Verwendung

Nutzung als REPL (read–eval–print loop). 

Achtung: Die Variante ohne `print()` funktioniert nur in der interaktiven Shell.

```bash
>>> print('Hello, World')
Hello, World
>>> 'Hello, World'
'Hello, World'
```

Mathematische Operationen

```bash
>>> 2 * 4 / 3
2.6666666666666665
>>> a = b = 10
>>> a + b
20
```

Inkrementierung/Dekrementierung

```bash
>>> a = 1
>>> a
1
>>> a += 4
>>> a
5
```
Auswertungen

```bash
>>> a == 5
True
>>> a == 4
False
```

```python
>>> b = None
>>> b is not None
False
>>> b is True
False
>>> b is None
True
```

Verfügbar: `<`, `<=`, `==`, `>=`, `>`, `!=`, `is`, `is not`

## Casting

- Umwandlung von Typen (built-in)
- Beispielsweise `int()`, `float()`, `str()`, `hex()`

```python
>>> x = "33"
>>> type(x)
<class 'str'>
>>> type(int(x))
<class 'int'>
```

## Strings

- einfache oder doppelte Anführungszeichen
- Escaping mit `\`
- Untersützung für Unicode

```bash
>>> string = "Hello, "
>>> string += " World"
>>> string
Hello , World
>>> a = 'ab'
>>> a*4
'abababab'
```
Multiline string.

```bash
>>> long_string="""This is a very very very
... very very long string"""
```

### Formatierung

[PEP 3101](https://www.python.org/dev/peps/pep-3101/) beschreibt die Formatierung von Strings. 

```bash
>>> string1 = "Hello"
>>> string2 = "World"
>>> '{}, {}'.format(string1, string2)
'Hello , World'
>>> '{1}, {0}'.format(string1, string2)
'World, Hello'
```

Noch oft anzutreffen:

```bash
>>> '%s, World' % 'Hello'
'Hello, World'
```

Details: [String](https://docs.python.org/3.5/library/string.html)

## Datentypen

### Listen

- Index startet bei 0
- Werte löschen `list.remove(x)`, hinzufügen `list.append(x)`, einfügen `list.insert(i, x)`
- Sortieren `list.sort()`, Index bestimmen von Element `list.index(ix)` 

```bash
>>> list = ['Hello', 1234, [1, 2]]
>>> list[0]
'Hello'
>>> list[0][0]
'H'
>>> list[2][1]
2
```

Details: [Lists](https://docs.python.org/3.5/library/stdtypes.html#lists)

### Dictionaries

- Struktur für die Speicherung von Schlüssel (key) und Werten (value), indexiert wird mit Key
- andere Sprachen kennen dies als "hash tables" oder "associative arrays"
- nicht zu verwechseln mit einem Set: `cars = {'VW', 'Audi', 'Skoda'}`
- Werte löschen `del dict['key']`, hinzufügen `dict['key'] = value`

```python
>>> dict = {"e": 2.71828, "pi": 3.14}
>>> dict
{'pi': 3.14, 'e': 2.71828}
>>> dict.keys()
dict_keys(['pi', 'e'])
>>> dict.values()
dict_values([3.14, 2.71828])
```

Auslesen von Werten

```python
>>> users = {
...     'benutzer': 'fabian',
...     'vorname': 'fabian',
... }
>>> type(users)
<class 'dict'>
>>> users['benutzer']
'fabian'
>>> users['nachname']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'nachname'
```

Standard-Wert setzen, wenn Schlüssel unbekannt.

```python
>>> users.get('vorname')
'fabian'
>>> users.get('nachname', 'affolter')
'affolter'
>>> print(users.get('nachname'))
None
```

Details [dicts](https://docs.python.org/3.5/library/stdtypes.html#mapping-types-dict)

### Tuple

- Auflistung von Komma getrennten Werten
- Indexierung beginnt bei 0
- wird oft mit Generatoren genutzt

```python
>>> tuple = (1, 2, 3)
>>> tuple[1]
2
```

Details: [Tuples](https://docs.python.org/3.5/library/stdtypes.html#tuples)

## Kontroll-Strukturen

### for

```python
>>> for x in list:
...     print(x)
... 
Hello
1234
[1, 2]
```

Bei einem dict ist `dict.key()` der Standard.

```python
>>> for x in dict:
...     print(x)
... 
pi
e
```

```python
>>> for k, v in dict.items():
...      print('Key: ', k, '  Value: ', v)
... 
Key:  pi   Value:  3.14
Key:  e   Value:  2.71828
```

### if-then-else

```python
>>> for x in dict:
...     print(x)
... 
pi
e
```

```python
>>> for x in dict:
...      if x == 'e':
...          print(x)
...      else:
...          print('Not e')
... 
Not e
e
```

### Select-case

- Bei Python nicht bekannt

```python
>>> if x in 'bc':
...     print('No a')
... elif x in 'xyz':
...     print('x present')
... else:
...     print('Everything else')
```

oder als Alternative "directory lookup" mit einem Generator

```python
>>> ICON = {
...  'eur': 'mdi:currency-eur',
...  'gbp': 'mdi:currency-gbp',
...  'usd': 'mdi:currency-usd',
... }
>>> ([k for k, v in ICON.items() if 'usd' in v][0])
'usd'
```

## Module

- Importieren mit `import` (bei Ruby `require`)
- Dateiname entspricht dem Modul-Namen, wenn Teile des Codes ausgelagert wurden
- Module-Name ist als `__name__` verfügbar

```python
>>> 1*2*3*4*5
120
>>> import math
>>> math.factorial(5)
120
>>> import math as m
>>> m.factorial(5)
120
>>> from math import factorial
>>> factorial(5)
120
>>> from math import factorial as fact
>>> fact(5)
120
```

Python nutzt einen Mechanismus, den man als "Call by Object", "Call by Object Reference" oder "Call by Sharing" bezeichnet beim Aufruf von Funktionen.

### Eigenen Funktionen/Module

- `def` leitet Fuktionen ein
- Zweite Zeile `"""String"""` ist normalerweise Docstring ([PEP257](https://www.python.org/dev/peps/pep-0257/))
- Funktionen können wie Prozduren in anderen Sprachen aussehen, sie geben aber `None` zurück 

```python
>>> import datetime
>>> def print_time():
...     print(datetime.datetime.now())
... 
>>> print_time()
2016-12-03 18:24:13.635640
```
Mit `return`

```python
>>> import datetime
>>> def print_time():
...     return datetime.datetime.now()
... 
>>> print_time()
datetime.datetime(2016, 12, 03, 19, 39, 49, 963597)
```

Argumente

```python
>>> def function(start, end):
...     x = start 
...     y = end
...     return list(range(x, y))
... 
>>> a = function(3, 9)
>>> a
[3, 4, 5, 6, 7, 8]
```

Inklusive Schlüsselwörter für die Definition von Standard-Werten

```python
>>> def function(start=0, end=10):
...     x = start 
...     y = end
...     return list(range(x, y))
... 
>>> a = function()
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Variable Anzahl von Argumenten

```python
>>> def function(*args, **kwargs):
...     for arg in args:
...             print(arg)
...     for kw, value in kwargs.items():
...             print('{}={}'.format(kw, value))
... 
>>> x = function(1, "Argument", [1, 2, 3], start=5, end=100)
1
Argument
[1, 2, 3]
end=100
start=5
```

### Ein komplettes Modul

Beispielsweise [`fibonacci.py`](fibonacci.py).

```python
def main():
    x = int(input('Please enter an integer: '))
    print(fib(x))

def fibonacci(n):
    """Calculate the fibonacci number for a given integer."""
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a

if __name__ == "__main__":
    main()
```

Benutzen als Standalone-Skript (mit Shebang `#!/usr/bin/env python3` und `chmod +x  fibonacci.py` könnte der Aufruf auch mit `./fibonacci.py` erfolgen)

```bash
$ python3 fibonacci.py
Please enter an integer: 13
233
```

Verwendung als Modul (Datei muss sich im gleichen Verzeichnis befinden, in welchen die Shell gestartet wurde)

```python
>>> import fibonacci
>>> fibonacci.__name__
'fibonacci'
>>> fibonacci.fibonacci.__doc__
'Calculate the fibonacci number for a given integer.'
>>> fibonacci.fibonacci(13)
233
```

## Exceptions

- Unterschiedung zwischen Syntaxfehler (syntax error) und Ausnahmen (exceptions)
- bei Fehlern gibt es ein sogenanntes `Trackback` mit dem Fehler-Typ
- `try ... except` erlaubt einen optionalen `else`-Block

```python
>>> 10/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

Abfangen, respektive Behandlung mit `try` und `except`:

```python
>>> for divisor in [2, 4, 0, 5]:
...     try:
...             print(20/divisor)
...     except ZeroDivisionError:
...             print('Division with zero')
... 
10.0
5.0
Division with zero
4.0
```

Details: [Exceptions](https://docs.python.org/3.5/library/exceptions.html)


## Klassen

- Klassen sind Objekte
- es können mehrere Basisklassen genutzt werden
- eine abgeleitete Klasse kann Methoden seiner Basisklasse überschreiben
- `global` und `nolocal` haben Einfluss auf den Namensraum
- `_private_var` oder `__private_var` für die Einschränkung des Scopes
- Klassen-Instanziierung benutzt die Funktionsnotation `x = Class()` und ruft, wenn vorhanden, `__init__()` auf
- [`self`](https://docs.python.org/3/faq/design.html#why-must-self-be-used-explicitly-in-method-definitions-and-calls) ist der ersten Parameter einer Methode, braucht nur in der Definition vorhanden zu sein und ist die Referenz auf die Instanz. Ähnlichkeit mit `this` in C++.

Download: [area.py](area.py)

```python
>>> class Area(object):
...     def __init__(self, a, b):
...             self.a = a
...             self.b = b
...     def calculate_area(self):
...             return self.a * self.b
>>> area = Area(4, 5)
>>> area.a, area.b
(4, 5)
>>> area.calculate_area()
20
```

Manipulation der Mitglieder

```python
>>> area.__dict__
{'b': 5, 'a': 4}
>>> area.__dict__['a'] = 10
>>> area.calculate_area()
50
```

### Properties

Properties sind Attribute mit getter- und setter-Methoden.

```python
>>> class GetterSetter(object):
...     def __init__(self):
...             self.__name = "The name"
...     def get_name(self):
...             return self.__name
...     def set_name(self, name):
...             self.__name = name
... 
>>> getter_setter = GetterSetter()
>>> getter_setter.get_name()
'The name'
>>> getter_setter.set_name('New name')
>>> getter_setter.get_name()
'New name'
```

Nutzung von `@property` als Decorator (beispielsweise bei Platformen: `def name(self):`)

```python
>>> class Properties(object):
...     def __init__(self):
...             self.__name = "The name"
...     @property
...     def name(self):
...             return self.__name
...     @name.setter
...     def name(self, name):
...             self.__name = name
... 
>>> props = Properties()
>>> props.name
'The name'
>>> props.name = 'New name'
>>> props.name
'New name'
```

### Vererbung

- Einfach-Vererbung: `class DerivedClassName(BaseClassName):`
- Mehrfach-Vererbung: `class DerivedClassName(Base1, Base2, Base3):`

```python
class AwesomeWeatherSensor(Entity):
```


Details: [Klasses](https://docs.python.org/3.5/tutorial/classes.html)
