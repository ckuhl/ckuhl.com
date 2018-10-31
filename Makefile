PLAYBOOK=pipenv run ansible-playbook
MASTER_COMMIT=$(shell git rev-parse --short HEAD)
ARGS=--extra-vars "version=${MASTER_COMMIT}"
ANSIBLE_PLAYBOOK=${PLAYBOOK} ${ARGS}

DEPLOY_FILES_DIR=deploy/roles/deploy/files


# TODO: If I use tar & gzip instead of zip, it _should_ only unpack the archive when files change
bundles: code static resources ## Bundle up everything for deployment

code: clean
	pipenv run pip freeze > ckuhl/requirements.txt
	zip -r ${DEPLOY_FILES_DIR}/${MASTER_COMMIT}-code.zip ckuhl
	zip -d ${DEPLOY_FILES_DIR}/${MASTER_COMMIT}-code.zip ckuhl/db.sqlite3

static: clean
	zip -r ${DEPLOY_FILES_DIR}/${MASTER_COMMIT}-static.zip static

resources: clean
	zip -r ${DEPLOY_FILES_DIR}/${MASTER_COMMIT}-resources.zip resources


.PHONY: clean deploy
clean: ## Remove temporary deployment files
	rm -rf ${DEPLOY_FILES_DIR}/*.zip

	# Delete _ALL_ bytecode files
	find .. -type d -name __pycache__ \
		-o \( -type f -name '*.py[co]' \) -print0 \
		| xargs -0 rm -rf

deploy: bundles ## Do the entire deployment
	cd deploy/; ${ANSIBLE_PLAYBOOK} deploy.yml; cd -;

update: bundles
	cd deploy/; ${ANSIBLE_PLAYBOOK} update.yml; cd -;
