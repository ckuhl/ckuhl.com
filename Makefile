BASE ?= $(shell pwd)
TESTS=tests
ENV=env
PYTHON3=env/bin/python3
PIP=env/bin/pip
DOCS=docs
PROJECT=personal_site

EXEC=personal_site.py

.PHONY: clean docs run debug test setup init
clean:
	find . -regex "\(.*__pycache__.*\|*.py[co]\)" -delete

run:
	${PYTHON3} -O ${EXEC}

debug:
	${PYTHON3} ${EXEC}

setup:
	test -d ${ENV} || virtualenv -p /usr/bin/python3 --no-site-packages ${ENV}
	test -e requirements.txt && ${PIP}  install -r requirements.txt
	${PIP} install --upgrade pip
	${PIP} install --upgrade setuptools

