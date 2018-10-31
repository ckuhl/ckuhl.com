---
title: How does Flask work?
published: True
category: blog
tags: [technology, python]
---

When you first start using the [Flask framework](http://flask.pocoo.org/) it
feels a little magical. You write a function to return some text, add a single
line above it, call run, and your text is somehow being sent to your web
browser! Most introductions will show you a little sample of code something
like this.

```python3
from flask import Flask


app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Hello World!"
 
if __name__ == "__main__":
    app.run()
```

At most you'll get a handwavy explanation that `@app.route` defines URLs, and
usually you are just expected to accept that that is how it works. Now
certainly that is enough to start adding more code that usually works. However
personally it bugs me. How does Flask know to serve my content at that URL?

I find it easiest to start from as high up as possible and work my way down the
chain of calls until it all starts making sense. So we start with the last
function what is called: `app.run()`.

## Off and run()-ing

`app.run()` isn't too exciting itself. It takes a number of optional parameters
(for example, whether debug mode is set, or what port to operate on) and then
sets them inside the Flask object. Right at the end it imports
[Werkzeug](http://werkzeug.pocoo.org/), and then calls `run_simple(host, port,
self, **options)`.

Inside of `run_simple` we see more setting up. This is focused on the server
though. In addition, it defines a few internal functions. The key function is
`inner()`, which creates a server. It calls `make_server`, passes it the Flask
application and then runs it in a loop.

Depending on what optional parameters are passed into it, `make_server` creates
one of several kinds of servers. ThreadingWSGIServer, ForkingWSGIServer, or in
our case, BaseWSGIServer. This is a subclass of Python's builtin HTTPServer
object. This server includes the [Web Server Gateway
Interface](https://en.wikipedia.org/wiki/Web_Server_Gateway_Interface) (WSGI),
which is a standardized API for Python frameworks to communicate with
webservers.

In essence, a server implementing WSGI will call the `__call__(environ,
start_response)` method on the application it has been passed. To dig deeper,
`environ` is a dictionary of CGI variables (CGI itself being a
language-agnostic predecessor to WSGI, and an initialism for [_Common Gateway
Interface_](https://en.wikipedia.org/wiki/Common_Gateway_Interface)).
`start_response` is a function that returns a tuple of an HTTP status code, and
the headers to respond with.

## How does Flask handle `__call__`s?

`Flask.__call__` is actually a thin wrapper around another function,
`Flask.wsgi_app`. This is done so that middleware (add-ons that can intercept
the messages between the WSGI server and application, and extend them) can be
applied.  After doing some error handling, this calls the internal function
`full_dispatch_request`

Here we do some more error handling, before call `dispatch_request`, which is
the real focus. This gets the request and the URL associated with the request.
Then it looks up the URL in an internal map for functions that handle requests,
and calls the corresponding function for that URL with the view arguments.

## What functions?

Now where does the map of URLs come from?
[Decorators!](https://en.wikipedia.org/wiki/Decorator_pattern)

Moving upwards from the bottom of our sample, we look into `@app.route("/")`
now.  This is a function decorator (that is, a function that takes a function
as input and returns a (possibly modified) function).

Our `route` decorator takes a rule (parameterized URL as a string), the view
function (hello in our case), and other optional parameters. From there we call
the internal function `add_url_rule`.

This creates a Rule object (from Werkzeug). This is a wrapper for the
parameterized URL string and the other optional arguments. For example, by
creating Rules we can have different views defined for the same URL depending
on whether the browser request is `GET` or `POST`. These rules are then added to
the internal map `self.url_map`, which is what Flask's `__call__` method looks
up URLs in!


The cycle is complete! With this adventure, we've dug (with excruciating
detail) into what Flask _does_ when you run the simple application. While this
information may not be useful when writing your own Flask application, it is
very good to know. Being able to dig into the guts of your application and know
what it is actually doing has been incredibly valuable in efficiently debugging
Flask when things stop going according to plan.

Did I miss something, or mess up a detail? Appreciate it? I'd [love to
hear](mailto:blog@ckuhl.com) from you if you have any comments on this article!

