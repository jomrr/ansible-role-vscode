# ansible-role-vscode

Ansible role for setting up Visual Studio Code.

## Supported Platforms

* Archlinux
* Ubuntu 16.04, 18.04

## Requirements

Ansible 2.7 or higher is recommended.

## Variables

Variables for this role:

| variable | default value in defaults/main.yml | description |
| -------- | ---------------------------------- | ----------- |
| vscode_enabled | False | determine whether role is enabled (True) or not (False) |
| vscode_users | [] | List of dicts for configuration of extensions and settings per use, see [Example Playbooks](##Example-Playbooks) |
| vscode_create_users | False | create users from vscode_users list of dicts. Meant for molecule testing only. |

## Dependencies

None.

(##Example-Playbooks)

A minimal playbook:

```yaml
---
# role: ansible-role-vscode
# file: site.yml

- hosts: vscode_systems
  become: True
  vars:
    vscode_enabled: True
  roles:
    - role: ansible-role-vscode
```

An example playbook with user extension and settings:

```yaml
---
# role: ansible-role-vscode
# file: site.yml

- hosts: vscode_systems
  become: True
  vars:
    vscode_enabled: True
    vscode_users:
      - username: jonas
        vscode_extensions_install:
          - bbenoist.vagrant
          - codezombiech.gitignore
          - davidanson.vscode-markdownlint
          - donjayamanne.githistory
          - eamodio.gitlens
          - esbenp.prettier-vscode
          - mikestead.dotenv
          - ms-azuretools.vscode-docker
          - ms-ceintl.vscode-language-pack-de
          - ms-kubernetes-tools.vscode-kubernetes-tools
          - ms-python.python
          - ms-vscode-remote.remote-ssh
          - ms-vscode-remote.remote-ssh-edit
          - openhab.openhab
          - redhat.vscode-xml
          - samuelcolvin.jinjahtml
          - vscoss.vscode-ansible
          - yzane.markdown-pdf
          - yzhang.markdown-all-in-one
          - ziyasal.vscode-open-in-github
        vscode_extensions_remove: []
        vscode_settings_force: True
        vscode_settings: {
          "telemetry.enableTelemetry": false,
          "telemetry.enableCrashReporter": false,
          "editor.rulers": [80, 100, 120, 140, 160],
          "editor.renderWhitespace": "all",
          "files.associations": {
            "install*.yml": "ansible",
            "main.yml": "ansible",
            "setup*.yml": "ansible",
            "playbook.yml": "ansible",
            "site.yml": "ansible",
            "tasks.yml": "ansible",
            "Archlinux.yml": "ansible",
            "CentOS*.yml": "ansible",
            "Debian.yml": "ansible",
            "RedHat.yml": "ansible",
            "Suse.yml": "ansible",
            "Ubuntu*.yml": "ansible",
            "Vagrantfile": "ruby"
          }
        }
  roles:
    - role: ansible-role-vscode
```

## Acknowledgements

This role uses the [ansible-aur](https://github.com/pigmonkey/ansible-aur) module from [pigmonkey](https://github.com/pigmonkey).

Thank you for putting this under MIT License and making it available.

## License and Author

* Author:: Jonas Mauer (<jam@kabelmail.net>)
* Copyright:: 2019, Jonas Mauer

Licensed under MIT License;
See LICENSE file in repository.

## References

[Visual Studio Code](https://code.visualstudio.com/docs/editor/command-line)
[pigmonkey/ansible-aur](https://github.com/pigmonkey/ansible-aur)
