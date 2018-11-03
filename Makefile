PLAYBOOK=pipenv run ansible-playbook
MASTER_COMMIT=$(shell git rev-parse --short HEAD)
ARGS=--extra-vars "version=${MASTER_COMMIT}"
ANSIBLE_PLAYBOOK=${PLAYBOOK} ${ARGS}

DEPLOY_FILES_DIR=deploy/roles/deploy/files


code: clean
	zip -r ${DEPLOY_FILES_DIR}/${MASTER_COMMIT}-code.zip ckuhl
	zip -d ${DEPLOY_FILES_DIR}/${MASTER_COMMIT}-code.zip ckuhl/db.sqlite3

static: clean
	zip -r ${DEPLOY_FILES_DIR}/${MASTER_COMMIT}-static.zip static

resources: clean
	zip -r ${DEPLOY_FILES_DIR}/${MASTER_COMMIT}-resources.zip resources


.PHONY: clean run deploy update
clean: ## Remove temporary deployment files
	rm -rf ${DEPLOY_FILES_DIR}/*.zip
	rm -rf ${DEPLOY_FILES_DIR}/*.txt

	# Delete _ALL_ bytecode files
	find .. -type d -name __pycache__ \
		-o \( -type f -name '*.py[co]' \) -print0 \
		| xargs -0 rm -rf

run: ## Run the website locally
	pipenv run python ckuhl/manage.py runserver

deploy: ## Do the entire deployment
	cd deploy/; ${ANSIBLE_PLAYBOOK} deploy.yml; cd -;

update:
	cd deploy/; ${ANSIBLE_PLAYBOOK} update.yml; cd -;
