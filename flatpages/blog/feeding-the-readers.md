---
title: Feed-ing the Readers
created: 2017-12-07 18:12 -5
updated: 2017-12-07 18:12 -5
published: True
tags:
  - news
  - dev
  - tweet+
...

Initially an MVP[^1], I have been progressively fleshing out my blog as I have
time, usually with whatever catches my fancy. My latest (re)discovery on this
front has been RSS[^2] feeds. Being able to keep up-to-date on blogs
that post infrequently is beneficial to me. Not only because I can
keep up on content I care about, but also because this form of passive following
allows me to use the internet less.

With that in mind, my latest update to the site has been to add an RSS feed.
Again trying to follow my focus on
[taking the easy way](/blog/the-easiest-route/),
I used the python library [feedgen](https://github.com/lkiesow/python-feedgen)
to do all the heavy lifting for me. Combined with FlatPages for flask, and I
have another handy feature added to my blog in just under an hour.


[^1]: Minimum Viable Product

[^2]: [Rich Site Summary](https://en.wikipedia.org/wiki/RSS), a way to
publish updates to sites in a computer-readable format.

