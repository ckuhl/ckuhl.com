# [ckuhl.com](https://ckuhl.com/)
The personal website, portfolio, and blog of Chris Kuhl.

## How to run this?
The following command is enough to clone, configure, and run the site:

    git clone https://github.com/ckuhl/ckuhl.com && cd ckuhl.com && make demo

Then the site will be accessible at `http://127.0.0.1:5000`.


## Features
- a blog
	- contains RSS feeds, categories, tags, and more!
- a portfolio of my projects
- respectful analytics
	- simple reports on the local analytics data
	- Google Analytics (if the user doesn't have Do Not Track enabled)
- [a rather large to-do list](TODO.md)


## Notes
### FlatPage schema
Arity | Name | Value | Description
--- | --- | --- | ---
`1` | `title` | str | Title of the page
`?` | `published` | bool | Whether or not the page is published yet
`1` | `category` | str | where the post appears (blog, portfolio, etc.)
`*` | `tags` | List[str] | list of tags to group posts by
`*` | `pre_js` | List[str] | JavaScript files to embed before the content
`*` | `post_js` | List[str] | JavaScript files embed after the content
`*` | `styles` | List[str] | list of css style files to embed before the content
`?` | `repo` | str | Git repository related to the post (used by Portfolio)
`?` | `description`| str | Short "teaser" of the Post (used by Portfolio)

### Favicon
Made using [favicon.io](https://favicon.io/), with the following settings:

- Text: CK
- Shape: Square
- Font Family: Nunito Sans
- Font Size: 95
- Font Colour: `(255, 255, 255)`
- Background Colour: `(26, 26, 26)`

### Tools
I've created `example-tools.js` and `example-tools.css` to allow creating
JavaScript demonstrations directly inside blog posts.
