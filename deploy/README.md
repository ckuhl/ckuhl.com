# Deploy

Sadly, the fun of developing a website is only half the battle.

You also have to deploy it somehow.

To avoid the headache of manually doing the work every time I deploy, I've
codified my deployment process into a series of Ansible roles.


## Structure

- `group_vars` hold variables specific to a host group
- `roles` holds units of work, involving tasks, handlers, etc.
    - [prepare](roles/prepare/README.md) prepares local files for deployment
    - [configure](roles/configure/README.md) sets up the server with a user
    - [nginx](roles/nginx/README.md) installs nginx and removes the default configuration
    - [letsencrypt](roles/letsencrypt/README.md) gets a LE certificate 
    - [deploy](roles/deploy/README.md) deploys the webapp

- Inside of each role:
    - `files`: files to be used in the deployment process
    - `tasks`: a list of actions to run
    - `templates`: files, template
    - `vars`: role-specific variables
    - `handlers`: tasks to run after certain tasks


## Notes

There are a few files that are not tracked in git that are necessary for
deployment:

- `.vault_password`
    - Plaintext password for encrypting / decrypting secrets
- `~/.ssh/id_rsa`
    - Private key for password-free access to remote
- `~/.ssh/id_rsa.pub`
    - Installed for new users to allow password-free access to them


## To do

- [ ] local preparation in Ansible, not Make using `prepare` role
