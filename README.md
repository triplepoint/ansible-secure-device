# Intro
The goal of this role is to bring a machine up as generically as possible, secure enough to face the public Internet and not immediately melt.

At a high level:
- Install Fail2ban, to make malicious authentication attempts harder
- Disable `root` user SSH
- Disable password SSH authentication for everyone (keys only)
- Disable SSH and `sudo` access for everyone, and create and configure a set of whitelisted users
- Limit SSH access to a specific IP address range
- Install `ufw` and disable all traffic, with configurable port exceptions (optional)
- Install `unattended-upgrades` and configure for automatic apt package security updates
- Install an `ntp` server to ensure reliable system time
- Install `logwatch` and configure to email daily log reports to an admin email address

Obviously this is a role best inspected for details before using, as no possible guarantees can be made about security.

## Requirements
None.

## Role Variables
See the [comment in the default variables file](defaults/main.yml) for information on configuration.

## Dependencies
None.

## Example Playbook
    - hosts: whatever
      roles:
        - triplepoint.secure_device

## Role Testing
This role is tested with `molecule`, using `pipenv` to handle dependencies and the Python testing environment.

### Setting Up Your Execution Environment
``` sh
pip install pipenv
```

Once you have `pipenv` installed, you can build the execution virtualenv with:
``` sh
pipenv install --dev
```

### Running Tests
Once you have your environment configured, you can execute `molecule` with:
``` sh
pipenv run molecule test
```

### Regenerating the Lock File
You shouldn't have to do this very often, but if you change the Python package requirements using `pipenv install {some_package}` commands or by editing the `Pipfile` directly, or if you find the build dependencies have fallen out of date, you might need to regenerate the `Pipfile.lock`.
``` sh
pipenv update --dev
```
Be sure and check in the regenerated `Pipfile.lock` when this process is complete.

## License
MIT
