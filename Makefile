# Get the latest commit hash for tagging the deployment
DEPLOY_COMMIT=$(shell git rev-parse --short HEAD)
ARGS=--extra-vars "version=${DEPLOY_COMMIT}"
PLAYBOOK=pipenv run ansible-playbook
ANSIBLE_PLAYBOOK=${PLAYBOOK} ${ARGS}

DEPLOY_FILES_DIR=deploy/roles/deploy/files


.PHONY: clean test run migrate deploy update
setup:  ## Set up local development environment
	which pipenv || echo "Pipenv must be installed" && exit 1
	pipenv install --dev

clean:  ## Remove temporary deployment files
	rm -f ${DEPLOY_FILES_DIR}/*.zip
	rm -f ${DEPLOY_FILES_DIR}/*.txt

test: setup  ## Run all tests
	pipenv run python ckuhl/manage.py test

run: setup migrate  ## Run the site locally
	pipenv run python ckuhl/manage.py runserver

migrate: setup  ## Apply migrations
	pipenv run python ckuhl/manage.py runserver

deploy: test  ## Deploy to fresh Ubuntu 18.04 server
	cd deploy/; ${ANSIBLE_PLAYBOOK} deploy.yml; cd -;

update: test  ## Update existing, configured server
	cd deploy/; ${ANSIBLE_PLAYBOOK} update.yml; cd -;
