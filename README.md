# Ansible Spring boot
[![Build Status](https://travis-ci.org/remyma/ansible-springboot.svg?branch=master)](https://travis-ci.org/remyma/ansible-springboot)

Deploy spring boot applications.

## Role Variables

| Variable     | Default       | Description    |
| ------------ | ------------- | -------------- |
| springboot_src |  | Mandatory. Path of the springboot jar to deploy |
| springboot_application_name |  | Mandatory. Spring application name. Use to name jar to be deployed, systemd service, ... |
| springboot_target | /opt/{{ springboot_application_name }}.jar | Target path for the jar to be deployed |
| springboot_user | springboot | Linux user to run spring boot application |
| springboot_group | springboot | Linux group to run spring boot application |


## Example Playbook

    - hosts: all
      vars:
        springboot_application_name: spring-boot-sample
        springboot_src: tests/spring-boot-sample.jar
      roles:
        - role: ansible-springboot

## License

BSD

