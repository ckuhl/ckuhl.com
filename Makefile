# Directories
ENV=env
DOCS=docs
DIST=dist
PROJECT=ckuhl

# Executables
PYTHON=${ENV}/bin/python3
PIP=${ENV}/bin/pip
EXEC=manage.py


package: clean	## bundle together all files essential for deployment
	git archive -o ${PROJECT}.tar HEAD
	tar -f ${PROJECT}.tar --delete README.md
	tar -f ${PROJECT}.tar --delete TODO.md
	tar -f ${PROJECT}.tar --delete Makefile
	tar -f ${PROJECT}.tar --delete .gitignore
	gzip ${PROJECT}.tar
	mkdir -p ${DIST} && mv ${PROJECT}.tar.gz ${DIST}

docs:	## generate documentation from docstrings in modules
	${PYTHON} -m pydoc -w ${PROJECT}
	ls ${PROJECT}/*.py \
		| sed 's/\//\./g' \
		| sed 's/\.py//g' \
		| xargs ${PYTHON} -m pydoc -w
	ls ${PROJECT}/views/*.py \
		| sed 's/\//\./g' \
		| sed 's/\.py//g' \
		| xargs ${PYTHON} -m pydoc -w
	test -d ${DOCS}/ || mkdir ${DOCS}
	mv ${PROJECT}.*html ${DOCS}


.PHONY: clean help run debug setup
clean:	## remove compiled python files, packages, logging, and docs
	find . -regex "\(.*__pycache__.*\|*.py[co]\)" -delete
	find . -name '*.tar.gz' -delete
	find . -name '*.sqlite' -delete
	find . -name '*.log' -delete
	rm -rf ${DOCS}/ ${DIST}/

help:	## show this help message
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

run:	## run in production mode
	${PYTHON} ${EXEC} run


debug:	## run in debug mode
	${PYTHON} ${EXEC} debug

setup:	## set up development environment
	test -d ${ENV} \
		|| virtualenv -p /usr/bin/python3 --no-site-packages ${ENV}
	test -e requirements.txt && ${PIP} install -r requirements.txt
	${PIP} install --upgrade pip
	${PIP} install --upgrade setuptools

demo: setup debug	## demonstrate this application

