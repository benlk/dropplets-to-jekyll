# This is experimental.

## Example:

```diff
# Sunset solar eclipse to brush Columbus Sunday
- Ben Keith
- benlkeith
- 2012-05-18 04:19
- Blog
- published
+---
+title: 'Sunset solar eclipse to brush Columbus Sunday'
+author: Ben Keith
+twitter_handle: benlkeith
+date: 2012-05-18
+time: 04:19
+categories: Blog
+classes: published
+---

```

## How to use this:

1. Copy your [Dropplets](https://github.com/johnroper100/dropplets) post markdown files into your jekyll site's `_posts` directory
	- If your site's filenames are not named with the extension `.md`, rename them now, or edit `script.sh` to read from a different filename.
1. Clone this repository in the same directory that contains your `_posts` directory, so that your directory layout looks like this:
	```
	├── 404.html
	├── Gemfile
	├── Gemfile.lock
	├── _config.yml
	├── _posts
	│   └── example.md
	├── _site
	├── converter
	│   ├── convert.py
	│   ├── requirements.txt
	│   └── script.sh
	└── index.md
	```
1. in the converter directory, run `pip install -r requirements.txt`.
	- I recommend using a [virtualenv](https://pypi.python.org/pypi/virtualenv) with [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).
	- We're only using this to install Chris Amico's [frontmatter](https://github.com/eyeseast/python-frontmatter/) library [from pypi](https://pypi.python.org/pypi/python-frontmatter/0.2.1). This script uses frontmatter to make sure that the post-conversion frontmatter is validly formatted, and it's only partially effective at doing so. Jekyll barfs on some things; it's best to run `jekyll serve` or `jekyll build` to make sure. If you don't want to rely on `frontmatter`, delete the line in `convert.py` in `main` that calls `frontmatter_parse`
1. copy `script.sh` from `/converter` to the parent directory:
	```
	├── 404.html
	├── Gemfile
	├── Gemfile.lock
	├── _config.yml
	├── _posts
	│   └── example.md
	├── _site
	├── converter
	│   ├── convert.py
	│   └── requirements.txt
	├── index.md
	└── script.sh
	```
1. Run the converter: `./script.sh`. 

This assumes:

- that you're running Python 2 as `python`
- that your files are named `.md`
- that your files are using `\n` for end-of-line; use [`dos2unix`](https://en.wikipedia.org/wiki/Unix2dos) to fix this if not.
- some things that were true for my files that may not be true for yours; see the contents of `convert.py`. I hacked the "post status" line item to support multiple words, which were then added as class names and separate templates.
