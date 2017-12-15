# Directories
ENV=env
DOCS=docs
DIST=dist
PROJECT=ckuhl

# Executables
PYTHON=${ENV}/bin/python3
PIP=${ENV}/bin/pip
EXEC=manage.py


# package: bundle together all files essential for deployment
package: clean
	git archive -o ${PROJECT}.tar HEAD
	tar -f ${PROJECT}.tar --delete README.md
	tar -f ${PROJECT}.tar --delete TODO.md
	tar -f ${PROJECT}.tar --delete Makefile
	tar -f ${PROJECT}.tar --delete .gitignore
	gzip ${PROJECT}.tar
	mkdir -p ${DIST} && mv ${PROJECT}.tar.gz ${DIST}

# docs: generate documentation from docstrings in modules
docs:
	${PYTHON} -m pydoc -w ${PROJECT}
	ls ${PROJECT}/*.py \
		| sed 's/\//\./g' \
		| sed 's/\.py//g' \
		| xargs ${PYTHON} -m pydoc -w
	test -d ${DOCS}/ || mkdir ${DOCS}
	mv ${PROJECT}.*html ${DOCS}


.PHONY: clean run debug setup
# clean: remove compiled python files, packages, logging, and docs
clean:
	find . -regex "\(.*__pycache__.*\|*.py[co]\)" -delete
	find . -name '*.tar.gz' -delete
	find . -name '*.sqlite' -delete
	find . -name '*.log' -delete
	rm -rf ${DOCS}/

# run in production mode
run:
	${PYTHON} ${EXEC} run

# run in debug mode
debug:
	${PYTHON} ${EXEC} debug

# set up development environment
setup:
	test -d ${ENV} \
		|| virtualenv -p /usr/bin/python3 --no-site-packages ${ENV}
	test -e requirements.txt && ${PIP} install -r requirements.txt
	${PIP} install --upgrade pip
	${PIP} install --upgrade setuptools

demo: setup debug

