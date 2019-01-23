---
title: Python Test Suite
published: True
updated: 2018-11-02
category: portfolio
---

A while back, I had to write a rudimentary testing script for a class I was taking. While it was useful, but it had enough rough edges that I kept improving on it.

When I started classes the next semester,  I found a renewed usefulness for this sort of black-box testing. Now that it was the beginning of the semester, I had plenty of time to work on it, and so I began to plan out what I wanted to create.

To store all of my tests in one file I went with the YAML format so that I could take advantage of existing libraries, and avoid worrying about accessing data. On the script side, it ended up being primarily builtin libraries hooked together, which while not exciting, will be more robust than if I were to write all of the logic myself.

Writing the base functionality, I managed to learn how to interact with the shell with ease using the `subprocess` library in Python. Additionally, I made a more portable testing system by requiring only one test file instead of the previous 3 per test. While testing my first assignment using my new test suite, I ran into a case I had not considered -- programs only outputting to stderr instead of stdout. However to extend my code in this way was fast and painless. Overall this project is a success even if I were to stop using it now, if only for the learning experience I had while creating it.
