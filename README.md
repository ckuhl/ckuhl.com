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
### Tools
I've created `example-tools.js` and `example-tools.css` to allow creating
JavaScript demonstrations directly inside blog posts.

### Favicon
Made using [favicon.io](https://favicon.io/), with the following settings:

- Text: CK
- Shape: Square
- Font Family: Nunito Sans
- Font Size: 95
- Font Colour: (255, 255, 255)
- Background Colour: (26, 26, 26)

### FlatPage schema
#### nb. currently this isn't comprehensive
- `title`: Title of the page
- `created`: 2018-08-31 20:39 -7
- `updated`: 2018-08-31 20:39 -7
- `published`: True
- `category`: blog (where the post appears (blog, portfolio, etc.))
- `tags`: (list of tags group posts by)
  - `programming`
- `pre_js`: (list of scripts to embed before the content)
  - "d3.v5.min.js"
      - "example-tools.js"
- `post_js`: (list of scripts to embed after the content)
- `styles`: (list of styles to embed before the content)
  - "example-tools.css"

