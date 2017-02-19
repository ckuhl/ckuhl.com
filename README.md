# personal_site
## ChristianKuhl.com
The personal website, resume, and blog of Christian Kuhl.

This is intended to be a showcase of my abilities, both from a computer
science perspective and from a business / communication perspective.


## Setting up the site
Python requirements are stored in `requirements.txt` and the
virtualenvironment is stored in `.venv/` (but it is git ignored so that
everyone builds their own from the latest sources).


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


## Site structure
* `/` (homepage)
    * `/about`
    * `/contact`
    * `/blog`
        * `/posts`
    * `/portfolio`


## Links I've used
### Resources
Server setup:
* https://www.digitalocean.com/community/tutorials/initial-server-setup-with-ubuntu-14-04
* http://toroid.org/git-website-howto


* http://askubuntu.com/questions/155791/how-do-i-sudo-a-command-in-a-script-without-being-asked-for-a-password


Flask setup:
* https://www.digitalocean.com/community/tutorials/how-to-serve-flask-applications-with-uwsgi-and-nginx-on-ubuntu-14-04


LetsEncrypt setup:
* https://hjlog.me/post/177


Javascript:
* http://instantclick.io/


### Inspiration
* Style: http://www.marcogoingplaces.com/home/trekking-to-chota-bangal
* Style & structure: https://nicolas.perriault.net/
* Simplicity: http://rudenoise.uk/
