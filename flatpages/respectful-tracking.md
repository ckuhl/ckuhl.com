---
    title: "Respectful Tracking"
    created: 2018-03-09 18:53 -8
    updated: 2018-03-09 18:53 -8
    published: True
    category: blog
    tags:
      - "technology"
      - "python"
      - "flask"
...

As a university student in a co-op program, at most times I either working at a
job, or preparing to start applying to the next one. Sometimes both at the same
time. I have been working on this site to provide a portfolio of some of my
past projects, and of my writing. However I faced a problem. How would I
know if my site was actually capturing users or not? Of course I could use
Google Analytics, however I didn't like the idea of trusting any third party to
do something against their own interest. In this case, an advertising company
promising not to track third parties.

Goal: Implement server-side responses to [Do Not
Track](https://en.wikipedia.org/wiki/Do_Not_Track) headers, so that if users do
not want to be tracked, they will not even see Google Analytics code.

Now to do this, I first need to get whether the user has Do Not Track enabled
or not, and use that to conditionally render any templates. Thankfully the
Flask API makes this dead-simple to do. With the handler
`@app.context_processor` you can define a function to insert variables into the
context for ever render request.

```python3
# inject Do Not Track header variable for all contexts
@app.context_processor
def inject_dnt():
    dnt = False
    try:
        if request.headers['DNT']:
            dnt = True
        elif request.headers['dnt']:
            dnt = True
    except KeyError:
        pass
    return {'do_not_track': dnt}
```

With that in place, it's as easy as inserting an if statement into your base
template:

```jinja2
{% if not do_not_track %}
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-XXXXXXXXX-X"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'UA-XXXXXXXXX-X');
    </script>
{% endif %}
```

That's it! If you want to test this out, try enabling / disabling Do Not Track
in your web browser, and observing a change in the number of network requests
(or just the number on your adblocker) when you reload the page.

