PLAYBOOK=pipenv run ansible-playbook
MASTER_COMMIT=$(shell git rev-parse --short HEAD)
ARGS=--extra-vars "version=${MASTER_COMMIT}"
ANSIBLE_PLAYBOOK=${PLAYBOOK} ${ARGS}

DEPLOY_FILES_DIR=deploy/roles/deploy/files


.PHONY: clean test run deploy update
clean: ## Remove temporary deployment files
	rm -f ${DEPLOY_FILES_DIR}/*.zip
	rm -f ${DEPLOY_FILES_DIR}/*.txt

test:  ## Run all tests
	pipenv run python ckuhl/manage.py test

run:  ## Run the site locally
	pipenv run python ckuhl/manage.py runserver

deploy: test  ## Deploy to fresh Ubuntu 18.04 server
	cd deploy/; ${ANSIBLE_PLAYBOOK} deploy.yml; cd -;

update: test  ## Update existing, configured server
	cd deploy/; ${ANSIBLE_PLAYBOOK} update.yml; cd -;
