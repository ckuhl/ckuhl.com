---
title: (Web) Extending my knowledge
created: 2017-09-23
updated: 2017-09-23
published: True
tags:
  - dev
  - extensions
  - learning
...

With the announcement that Firefox would be deprecating XUL extensions,
I recently went through my addons to see which would be updated in time,
and which wouldn't. While most were being updated, I found that
[Image Block](https://addons.mozilla.org/en-us/firefox/addon/image-block/)
had not been. Considering the scale of the extension, I decided that
writing my own version as a web extension would be a good way to dip my
toes in the add-on development water.

This turned out to be surprisingly easy, much in part thanks to the
[fantastic documentation](https://developer.mozilla.org/en-US/Add-ons/WebExtensions)
that Mozilla provides. After an hour or two banging around, I ended up with
[Image Block X](https://addons.mozilla.org/en-US/firefox/addon/image-block-x/), which is a minimum viable product of the image blocker. It simply
toggles whether or not Firefox should load image type resources. There's
lots that can still be done, and with the ease of developing this, I
definitely look forward to it.

