# To-do

[TOC]

## Development

- [ ] replace Makefile with more sensible tool
  - alternately, only use it for Making an executable
- [ ] add types to code as necessary
  - for now, support Python 3.5+

## Deployment

- [ ] include Ansible playbook for deployment
  - [ ] Also avoid including secrets in that
  - [ ] Optimization: Enable compression in nginx (gzip / deflate)

## Website

- [ ] investigate why moving from markdown 2.x to 3 breaks things (related to "safe" HTML parsing)
- [ ] create one FlatPage post template with different options
  - e.g. "show_tags", "show_date", etc.
- [ ] add email integration to subdomain
  - [x] allow loading / storing secrets
- [ ] Optimize page speed ([As per Google's assessment](https://developers.google.com/speed/pagespeed/insights/?url=https%3A%2F%2Fckuhl.com%2F))
  - [x] Optimize images (e.g. `navbar-brand.png`)
  - [ ] Use browser caching
  - [ ] Eliminate / reduce blocking CSS resources
- [ ] Create static resource pipeline
  - [ ] Optimize all / new images
  - [ ] Bundle & minify JavaScript and CSS files
  - [ ] Aggressively cache e.g. font files

### Backend

- [x] Create middleware file (for Jinja2 templates, etc.)
- [x] Remove wiki (for now)
- [x] Make settings available from modules
- [ ] Require synopsis / lead for each flatpage

### Analytics

- [ ] use a Geo IP database to determine where viewers are from
- [ ] send reports on analytics to myself (using email integration)
  - [ ] Create "scheduled" scripts to run from cron jobs
    - look into using [APScheduler](https://apscheduler.readthedocs.io/en/v3.5.3/index.html)

### Core pages

- [x] update landing page Jumbotron with "best of Chris Kuhl" link
- [x] write jumbotron as a "hook" for employers

### FlatPages

- [ ] Add a "publish_on" YAML tag to allow writing / submitting content ahead of time

#### Blog pages

- [ ] add a "Next post" / "Previous post" to individual posts
- [ ] add month / time pages (e.g. "September 2017", "2018", etc.)
- [ ] revise `resource-hog.md`
- [x] allow embedding JavaScript tools in blog posts
- [ ] write posts with examples of data structures
- [ ] update tags viewing page
- [ ] create tags listing page

#### Portfolio pages

- [ ] add an image to `i-want-that-pet.md`
- [ ] add more images in general
- [ ] rewrite most pieces
- [ ] update to same format as blog
  - [ ] Individual portfolio piece
  - [ ] Portfolio index
  - [ ] Piece archive

## Tests

- [ ] write tests for utility functions