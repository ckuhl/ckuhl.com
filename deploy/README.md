# Deploy

Sadly, the fun of developing a website is only half the battle. You also have to deploy it somehow.

To avoid the headache of manually doing the work every time I deploy, I've
codified my deployment process into a series of Ansible roles.


## Structure

- `group_vars` hold variables specific to a host group
- `roles` holds units of work, involving tasks, handlers, etc. In order these are:
    1. [prepare](roles/prepare/README.md) prepares local files for deployment
    2. [configure](roles/configure/README.md) sets up the server with a user
    3. [nginx](roles/nginx/README.md) installs nginx and removes the default configuration
    4. [letsencrypt](roles/letsencrypt/README.md) gets a Let's Encrypt certificate
    5. [deploy](roles/deploy/README.md) deploys the web app

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
