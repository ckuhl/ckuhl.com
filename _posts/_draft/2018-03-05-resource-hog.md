---
title: A Different Kind of Resource Hog
published: False
category: blog
tags: [human-computer interaction]
---

The discussion around ad blockers often centres around whether it is
permissible to let advertising networks use your resources (battery life,
processing power, &c). This is well-trodden ground, often to the point of
smothering discussion around alternate uses of ad blockers. In a sense, I am
also using my blocker of choice to conserve resources. However I use it to
conserve a different kind of resource -- my attention.

In my interactions with the internet, I have found a number of patterns in
site designs that seem to increase the amount of time that I spend on a site,
regardless of the utility I get out of it. Thanks to the flexibility of
[uBlock origin](https://github.com/gorhill/uBlock), I can block various HTML
elements inside only a single domain.


## Related Links
Perhaps the most deadly of these is the "Related Content" links at the bottom
or sides of articles. Since these are usually chosen by whatever garners the
most clicks, they're optimized to grab your attention. Stack Overflow is
particularly guilty of this with it's "Hot Network Questions" that are from
different communities and entirely unrelated to what you want. But they are
just so darn interesting.

First on the block list:

* `###hot-network-questions`


## Infinite Scroll
Even the most engaging book often needs to be put down. Dinner, errands, or
other tasks must eventually be done. Thanks to the chapter format, it is easy
to find an good stopping point. Could you imagine reading a book without any
sort of separation of text? It would be an unending stream of text without any
way of knowing whether stopping now would leave you to forget minor details that
may prove crucial in the next chapter. It's stressful just to think about.

The infinite feed of Facebook, Twitter, Instagram, and others is another big
driver of unwanted consumption. It's mindlessly easy to keep flicking down the
feed without ever running into a natural stopping-point at which to break your
attention. Ultimately I've found myself utilizing
[Basic Facebook](https://mbasic.facebook.com/) as a way of avoiding the feed.


## Points and Votes
I often find myself reading all of the top posts on
[Hacker News](https://news.ycombinator.com/), even if they are not particularly
interesting themselves. Perhaps a form of distributed peer pressure, it is
much easier to pick and choose what you are actually interested in without
knowing the score. Some people may argue that you'll miss out on exposure to a
greater diversity of content. However at the same time, you'll be more
accepting of content that may not get the approval of the majority.

Some filters:

* `news.ycombinator.com##.subtext > .score`
* `www.reddit.com##.score`


## Conclusion
While this is still an experiment, I have found that my internet usage has down
down significantly since implementing these changes. At the same time, the
amount of enjoyment I get out of being online has been equally increased. Even
if you think it sounds silly, I encourage everyone to at least _try_ this for
a time. See if your media consumption habits change, and whether or not you
like the ways they change.

