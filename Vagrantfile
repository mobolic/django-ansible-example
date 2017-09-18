# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
    # Use Ubuntu Xenial/16.04 - it's the latest LTS Ubuntu version
    # (as of September 2016).
    config.vm.box = "ubuntu/xenial64"

    # Forward port 80 in the virtual machine to 8080 on our computer.
    # We should be able to access the webapp at http://127.0.0.1:8080/.
    config.vm.network :forwarded_port, guest: 80,
        host_ip: "127.0.0.1", host: 8080, auto_correct: true

    # Put our webapp code at /srv/example instead of /vagrant.
    # This will be synchronized with the virtual machine, so any
    # changes will carry over.
    config.vm.synced_folder ".", "/srv/example"

    # Provision using Ansible:
    #  - with a static inventory located at ansible/hosts
    #  - only work on the "vagrant" host (we can put staging hosts in this
    #    file if we need to)
    #  - use the "development" playbook
    #  - ask for a password to use on Vault files
    config.vm.provision "ansible" do |ansible|
        ansible.inventory_path = "ansible/hosts"
        ansible.limit = "vagrant"
        ansible.playbook = "ansible/development.yml"
        ansible.raw_arguments = ["--ask-vault-pass"]
    end

end
