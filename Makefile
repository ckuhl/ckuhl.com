BASE ?= $(shell pwd)
TESTS=tests
ENV=env
PYTHON=${ENV}/bin/python3
PIP=${ENV}/bin/pip
DOCS=docs
PROJECT=ckuhl

EXEC=app.py

.PHONY: clean run debug setup
clean:
	find . -regex "\(.*__pycache__.*\|*.py[co]\)" -delete

run:
	${PYTHON} -O ${EXEC}

debug:
	${PYTHON} ${EXEC}

setup:
	test -d ${ENV} || virtualenv -p /usr/bin/python3 --no-site-packages ${ENV}
	test -e requirements.txt && ${PIP}  install -r requirements.txt
	${PIP} install --upgrade pip
	${PIP} install --upgrade setuptools

