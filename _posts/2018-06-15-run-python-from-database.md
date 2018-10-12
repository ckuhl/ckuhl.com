---
title: Running python from a database
published: True
category: blog
tags: [what-if, programming, python]
---

While having my morning coffee, I had a strange idea. Is it possible to run
code stored inside a sqlite database? I had no idea if it was possible, but I
was curious. So I wrote a little project to find out.

First things first, I needed some code to store in the database. To keep things
simple, I wrote a basic hello world in `demo.py`.

```python3
print('Hello world!')
```

With that out of the way, now we need somewhere to store our code. I use 
[Peewee](http://docs.peewee-orm.com/en/latest/) as an ORM out of convenience.
So we create a basic table with a module name and code field.

```python3
import sqlite3

from peewee import SqliteDatabase, Model, TextField, CharField


db = SqliteDatabase('code.db')

class Module(Model):
    name = CharField()
    code = TextField()

    class Meta:
        database = db

db.connect()
db.create_tables([Module])
```

With the table set up, we can load our code into it.

```python3
with open('demo.py') as f:
    demo_module = Module(code=f.read(), name='demo')
    demo_module.save()
```

Now for the secret sauce: getting the code back out. With Python's built-in
[imp](https://docs.python.org/3/library/imp.html) module, you can access
the internals for importing code, which is exactly what we need to import our
module from the database as though it was from a file. First we create an empty
module with our desired name. Then we execute our code,
assigning the output into the module. Since Python modules are actually
dictionaries, executing the module means running any code that is
runnable, and otherwise mapping function names, etc. to their code. This is why
a lot of code has the `if __name__ == '__main__':` guard. Lastly we
return the module, allowing it to be bound to a name (equivalent to `import x
as y`).

```python3
def import_code(name, code):
    module = imp.new_module(name)

    exec(code) in module.__dict__

    return module
```

With all that out of the way, we can import our code from the database!

```python3
m = Module.get()
import_code(m.name, m.code)
```

The reveal:

```sh
$ python import_db.py
Hello world!
```

Cool!

If you want to take a look at the full script yourself, you can find it as a
[gist on GitHub](https://gist.github.com/ckuhl/76c3e0d59db86cc1c8666a49f0f21814).

## Uses
Truth be told, I still cannot think of any solid uses for this. Still, it was
fun to find out that it's possible to run code from the database. Who knows,
this knowledge might just come in handy in the future!

