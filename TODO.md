# To-do
## Admin
- [ ] replace Makefile with more sensible tool
  - alternately, only use it for Making an executable

## General site

- [ ] investigate why moving from markdown 2 -> 3 breaks things
- [ ] create one blog post template with different options
  - e.g. "show_tags", "show_date", etc.
  - instead of blog / portfolio being slightly different
- [ ] add email integration to subdomain
  * i.e. `alerts.ckuhl.com` for sending myself notifications, etc.
- [ ] Optimize page speed ([As per Google's assessment](https://developers.google.com/speed/pagespeed/insights/?url=https%3A%2F%2Fckuhl.com%2F))

## Backend

- [x] Create middleware file (for jinja templates, etc.)
- [x] Remove wiki (for now)
- [ ] Make settings available from modules
- [ ] Require synopsis / lead for each flatpage

## Analytics

- [ ] use a Geo IP database to determine where viewers are from
- [ ] after creating email integration, send reports

## Core pages

- [ ] update landing page Jumbotron with "best of Chris Kuhl" link
  - i.e. a brag sheet
- [x] write jumbotron as a "hook" for employers

## FlatPages

* [ ] Add a "publish_on" YAML tag to allow writing / submitting content ahead of time

### Blog pages

- [ ] add a "Next post" / "Previous post" to individual posts
- [ ] add month / time pages (e.g. "September 2017", "2018", etc.)
- [ ] revise `resource-hog.md`
- [x] allow embedding JavaScript tools in blog posts
- [ ] write posts with examples of data structures
- [ ] update tags viewing page
- [ ] create tags listing page

### Portfolio pages

- [ ] add an image to `i-want-that-pet.md`
- [ ] add more images in general
- [ ] rewrite most pieces
- [ ] update to same format as blog
  - [ ] Individual portfolio piece
  - [ ] Portfolio index
  - [ ] Piece archive
