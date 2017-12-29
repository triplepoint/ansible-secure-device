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
- Install `ntp` to ensure reliable system time
- Install `logwatch` and configure to email daily log reports to an admin email address

Obviously this is a role best inspected for details before using, as no possible guarantees can be made about security.
