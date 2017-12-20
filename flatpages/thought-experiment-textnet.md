---
    title: "Thought Experiment: The TextNet"
    created: 2017-12-19 19:45 -5
    updated: 2017-12-19 19:45 -5
    published: True
    category: blog
    tags:
      - thought experiment
...

On the forums I follow, there has been a growth in people begrudging the
"JavaScript-ization" of modern web content. On one hand I can absolutely agree
-- why should loading a text-only recipe take dozens of megabytes? At the same
time I feel it is a boon to allow for more efficient development (i.e. allowing
developers to focus on development instead of design). But I think that those
naysayers are onto something. So what would it look like if we banished all
JavaScript from (a segment of) the internet?

# The proposal

The TextNet, a text-only portion of the internet. A new `.text` TLD is
introduced. With a covenant that only plain text and HTML can be served from
such domains.


# What does that mean?

JavaScript doesn't run. It can still be loaded, but it's just a static text
file, like everything else. Same for images or files: You can
[Base64](https://en.wikipedia.org/wiki/Base64) encode them, but they will not
display. CSS would either be forbidden or restricted to a simple subset.


# What effects would this have?

## Fewer advertisements

First and foremost, conventional advertisers would not be attracted to it.
Without images for ads, or JavaScript to track users, there is no way to run
advertisements. This would prevent the advertising-driven formatting of
content. Slideshows of content, "Click to read full article", and clickbait
would disappear, as there would be no financial incentive to format articles in
that way. Who instead would create content? I expect you would see two groups
creating content:

### Indirect Beneficiaries

Businesses or professionals, creating content for indirect benefits. This could
include providing access to news in emergencies (for example when cell towers
are overloaded, as text uses little bandwidth, and could still be loaded). For
example, [NPR](http://text.npr.org/) and [CNN](http://lite.cnn.com/en) take
this approach. Here they do not benefit directly by providing ad-free articles.
Rather they gain a reputation for being available even when a user can not load
competitors' sites. Professionals self-promoting also fall in this group. Such
technical blogs are intended to develop a brand, and signal to employers that
the professional is competent.

### The Hobbyists and Artists

The other group would be those creating content for the joy of it. The medium
of plaintext imposes a set of constraints that allows people to focus their
creativity. Similar to using a reduced palette and canvas in [pixel
art](https://en.wikipedia.org/wiki/Pixel_art), text forces one to focus on the
content they produce, instead of the decoration that surrounds it. This
category includes both art and technical writing on niche topics, such as
[programming for a Game Boy](http://pp.feeb.dog/gb_z80_helloworld.txt).

In effect, removing advertising as a form of funding content creation would
disincentive the creation of low-quality content. In turn this increases the
signal-to-noise ratio of the content.

## Unconventional consumption

### Sneakernet

Since plaintext is lightweight, the entirety of the TextNet could be save to a
single thumb drive.  While the
[sneakernet](https://en.wikipedia.org/wiki/Sneakernet) currently exists, being
able to save a copy of everything would mean that any and all links within the
content would work. This would allow for a more natural "exploration" of the
internet by those without conventional access.

### New Ways of Interacting

The magnitude of JavaScript and CSS in modern webpages means that today's web
browsers can be used to run entire operating systems in them. The trade-off to
this is that you require the resources to run an entire operating system within
a browser. By reducing the required overhead from arbitrary scripts and styles
to text, new classes of devices could be used to interface with the internet.
eReaders would become first-class citizens, allowing months of internet
browsing on a single charge. More whimsically, teletypewriters could make a
comeback. Print off the web pages you want to read, and when you are done you
clear the browser history with a paper shredder.


# Conclusion

It is hard to know how a new, restricted medium would be treated. Especially
when the goal of such a medium is to encourage the creativity that emerges from
restriction. However I feel that such a medium would be a net positive to the
world, allowing broader access to the internet, and renewed interest for those
burnt out by the current madness.

