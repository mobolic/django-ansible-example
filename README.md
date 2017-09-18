# Example Ansible Playbook for a Django Project

As you might expect, this is an simple example Ansible playbook for Django
development.

Because this is an example, it does not currently include dynamically
determining cloud-based inventories or provisioning production servers.

## Requirements

  - Virtualbox
  - Vagrant
  - virtualenv and virtualenvwrapper

## Quickstart

  - Clone this repository to your development machine.

    git clone ...

  - Activate a new virtualenv and install the required development Python
    packages:

        mkvirtualenv example
        pip install -r requirements/development.txt

  - Provision the vagrant box / virtual machine:

        vagrant up --provision`.

## Important Notes

Note that **all of the variables in `ansible/secret_vars` should be changed.
All of the files in that directory should be converted to
[Ansible Vault](http://docs.ansible.com/ansible/latest/playbooks_vault.html)
files.**

If no Ansible Vault files have been created, entering anything at the Vault
password prompt will work.
