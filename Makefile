BASE ?= $(shell pwd)
TESTS=tests
ENV=env
PYTHON=${ENV}/bin/python3
PIP=${ENV}/bin/pip
DOCS=docs
PROJECT=ckuhl
EXEC=manage.py


.PHONY: clean run debug setup
clean:
	find . -regex "\(.*__pycache__.*\|*.py[co]\)" -delete
	find . -name "*.log" -type f -delete
	find . -name "*.sqlite" -type f -delete
	find . -name "*.db" -type f -delete

run:
	${PYTHON} ${EXEC} run

debug:
	${PYTHON} ${EXEC} debug

setup:
	test -d ${ENV} \
		|| virtualenv -p /usr/bin/python3 --no-site-packages ${ENV}
	test -e requirements.txt && ${PIP} install -r requirements.txt
	${PIP} install --upgrade pip
	${PIP} install --upgrade setuptools

