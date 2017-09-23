---
title: ckuhl.com
created: 2017-09-18
updated: 2017-09-19
published: True
tags:
  - website
  - python
  - portfolio
description: A personal website to use as a testing bed for new projects,
             a way to market myself (as a developer and
             writer/communicator), and to establish an online presence.
...

I've been working on a website in some form or other for more than a year
now but every time it's been an ordeal with choosing a framework and then
trying to get it to work. So this time around I decided to lay out what my
requirements were first, and then make a decision based on that criteria.

# Project Requirements

## Familiar tooling
As a side project, I don't have a lot of time to dedicate so I want to be as
efficient as possible.

## Simple content format
If I do change things in the future, I want to be able to take my documents
with me easily.

## Simple modules
I wanted to avoid fiddling with settings and various files in order to get the
extensions I need working.

*Not* a requirement:
- using a full-on JavaScript, CSS, etc. framework

With these requirements in mind, I went with the
[Flask](http://flask.pocoo.org/) micro webdevelopment framework for Python,
as well as
[Flask-Flatpages](http://flask-flatpages.readthedocs.io/en/latest/)
to host static content written in a mix of YAML and Markdown. Flask was
chosed because it is a very low-cost server in terms of learning the system,
and Flask-Flatpages for its fantastic formatting and ease of integration
with Flask.

# Project Details
Built with:

- python3
- Flask
- Flask-Flatpages

View the source to ckuhl.com on
[GitHub](https://github.com/ckuhl/ckuhl.com).

