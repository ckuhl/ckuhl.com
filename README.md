# My `personal_site` — ChristianKuhl.com
The personal website, resume, and blog of Christian Kuhl.

This is intended to be a showcase of my abilities, both from a computer
science perspective and from a business / communication perspective.

Built primarily using Python3, Flask, and Flask-Flatpages.


## Running the project
Required packages are listed in `requirements.txt` and the
virtual environment is stored in `.venv/`. However it's git-ignored so that
everyone builds their own from the latest versions). In theory all you should
need to do to run this site is:
1. `git clone https://bitbucket.org/ckuhl/flask-personal-site.git`

2. `cd personal_site`

3. `virtualenv -p python3 .venv`

4. `pip3 install requirements.txt`


## Project structure
* `/` init script and setup files
	* `/.venv` python virtual environment
	* `/static` all the static files the website serves
		* `/css`
		* `/img`
		* `/js`
	* `/templates` HTML fragments that site uses
		* `/base` base fragments -- footer, header, container
		* `/blog` blog partials
		* `/pages` display pages off of the main site


## Website structure
* `/` (homepage)
    * `/about`
    * `/contact`
    * `/blog`
        * `/posts` -- only used with a slug for each blog post
    * `/portfolio`


## Things I've used
### Resources
* Server setup:
	* [Initial Server Setup for Ubuntu 14.04 ](https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04)
	* [Using Git to manage a web site](http://toroid.org/git-website-howto)
	* [How to run sudo from a script without a password](http://askubuntu.com/questions/155791/)
* Flask setup: [Serve Flask Applications with uWSGI and Nginx on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04)
* LetsEncrypt setup: [Let's Encrypt your Ubuntu 14.04 + Flask + Nginx server](https://hjlog.me/post/177)
* Javascript: [InstantClick - Preload pages on hover](http://instantclick.io/)


### Inspiration
* Style: [Marco Going Places](http://www.marcogoingplaces.com/home/trekking-to-chota-bangal)
* Style & structure: [Nicolas Perriault's blog](https://nicolas.perriault.net/)
* Simplicity: [Focus is on content, not style](http://rudenoise.uk/)
