# [ckuhl.com](https://ckuhl.com/)

Personal website of Chris Kuhl. Written in Django for flexibility in what I
can create with it. Deployed using Ansible to make updating the site simpler.


## To - do

### Site apps

- [ ] Blog / Portfolio:
	- [ ] On loading flatpages, handle URLs for images
- [ ] Analytics
	- [ ] Create local analytics (for e.g. user-agents, etc.)
- [ ] New app: Ideas
	- Repository for "you know what would be cool?" ideas
	- Tweet-sized thoughts about anything and everything


### Project

- [ ] Tests
	- [ ] Write more comprehensive tests
		- [ ] Cover more cases
		- [ ] Cover more code
		- [ ] Cover functions that hit the DB
- [ ] Deployment
	- [ ] Split `deploy` role into smaller roles
	- [ ] Fix Let's Encrypt renewal script
- [ ] Structure
    - [ ] Look into how other people's Django sites are structured
	    - e.g. https://github.com/jacobian/jacobian.org
- [ ] Admin
	- [ ] Allow better bootstrapping


### Frontend

- [ ] Use _less_ CSS
    - Use human-readable styles instead of minified bootstrap theme
