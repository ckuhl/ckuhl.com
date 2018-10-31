# Deploy

Sadly, the fun of developing a website is only half the battle.

You also have to deploy it somehow.

To avoid the headache of manually doing the work every time I deploy, I've
codified my deployment process into a series of Ansible roles.


## Structure

- `group_vars` hold variables specific to a host group
- `roles` holds units of work, involving tasks, handlers, etc.
    - [configure](roles/configure/README.md) sets up the server with a user
    - [nginx](roles/nginx/README.md) installs nginx and removes the default configuration
    - [letsencrypt](roles/letsencrypt/README.md) gets a LE certificate 
    - [deploy](roles/deploy/README.md) deploys the webapp

- inside of each role:
    - `tasks`: a list of actions to run
    - `templates`: files, template
    - `vars`: role-specific variables
    - `handlers`: tasks to run after certain tasks


## Notes

Hidden / untracked files necessary for deployment:
- `.vault_password`
    - used to store user password
- `~/.ssh/id_rsa`
    - private key, used for logging into remote servers
- `~/.ssh/id_rsa.pub`
    - public key, installed into created users
- `project.yml` -> Environment variable secrets
