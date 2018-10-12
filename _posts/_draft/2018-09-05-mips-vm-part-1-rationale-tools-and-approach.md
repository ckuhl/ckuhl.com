---
title: "MIPS VM part 1: Rationale, tools, and approach"
published: False
category: blog
tags: [programming, project, MIPS VM]
---

## Rationale
After completing a class in compilers at school ([CS
241](https://www.student.cs.uwaterloo.ca/~cs241/) at the University of
Waterloo), I ran into a problem. Following the semester, I lost access to the
tools provided by the class. This meant that all of the code I had written --
from binaries to an assembler and a compiler -- were useless. Without a virtual
machine to run my binaries on, what use was all of this?

Thankfully, I have saved some resources from the class. Included in this was a
description of the subset of the MIPS Instruction set architecture (ISA) that
the class had made use of. Together with some other notes, and my saved test
cases from the semester, I had enough to recreate the virtual machine (VM).

## Tools
What tools will I use to complete this? First and foremost there is the
programming language to write the VM in. Writing a VM means I'll be dealing
almost entirely taking in pure data (save for taking input), and operating on
that data. Given this description, a functional programming language seems
appropriate. Since I'm not trying to learn a new language, I'll stick to the
functional language I know best,
[Racket](https://en.wikipedia.org/wiki/Racket_(programming_language)).

Beyond writing the VM, I need a way to verify that it is operating according to
the specification (in this case,  a specification by example, of the VM used at
school). As a part of doing assignments for CS 241, I had written tests for my
code to run on the school-provided VM using my [Python Test
Suite](https://ckuhl.com/portfolio/python-test-suite/). With all of that work
already in place, it's an obvious choice to continue using it.

## Approach
Since this is only a hobby project, I don't have a rigid plan that I'll be
adhering to. That being said, having thought about this on the bus for a while,
there is a general structure I expect to be following. Since I'm emulating a
processor, the code will follow the fetch-decode-execute cycle. In addition,
there will need to be some set-up work done on starting, and some output done
on program termination.

