---
title: Python Test Suite
published: True
category: portfolio
tags: [pts, portfolio]
description: A black box testing library built with Python and YAML. Useful
    for testing programs or scripts that don't have builtin testing
    functionality (e.g. MIPS assembly).
repo: https://github.com/ckuhl/pts
---

Last year for a computer science class (CS 246) I was required to write a
rudimentary testing script. I found it useful at the time, but it had a
number of rough edges that I found annoying enough to want to improve on.

When I started Introduction to Sequential Programming (colloquially, _baby
compilers_), I found a renewed need to test my programs against inputs. Now that
it was the beginning of the semester, I had plenty of time to work on it,
and so I began to plan out what I wanted to create.

## Goals
- Write a more extensible testing script
- Learn how to interact with the shell in Python
- store all tests in one file (instead of the previous 3 per test case)

## Process
To store all of my tests in one file I went with the YAML format so that I
could take advantage of existing libraries, and avoid worrying about
accessing data. On the script side, it ended up being primarily builtin
libraries hooked together, which while not exciting, will be more robust
than if I were to write all of the logic myself.

## Outcome
Writing the base functionality, I managed to learn how to interact with the
shell with ease using the `subprocess` library in Python. Additionally, I
made a more portable testing system by requiring only one test file instead
of the previous 3 per test. While testing my first assignment using my new
test suite, I ran into a case I had not considered -- programs only
outputting to stderr instead of stdout. However to extend my code in this
way was fast and painless. Overall this project is a success even if I were
to stop using it now, if only for the learning experience I had while
creating it.

## Project Details
Built with:

- Python3
- PyYAML

