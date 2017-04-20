# Ansible Spring boot
[![Build Status](https://travis-ci.org/remyma/ansible-springboot.svg?branch=master)](https://travis-ci.org/remyma/ansible-springboot)

Deploy spring boot applications as linux services.

## Requirements

Your spring boot application should be previously packaged as a fully executable jar as explained here :

https://docs.spring.io/spring-boot/docs/current/reference/html/deployment-install.html#deployment-script-customization-conf-file

## Role Variables

| Variable     | Default       | Description    |
| ------------ | ------------- | -------------- |
| springboot_src |  | Mandatory. Path of the springboot jar to deploy |
| springboot_application_name |  | Mandatory. Spring application name. Use to name jar to be deployed, systemd service, ... |
| springboot_propertyfile_template | | Optional. Path towards a template to manage your app properties (eg : application.properties, application.yml).  |
| springboot_configuration_template | | Optional. Path towards a template to manage your app config (see : https://docs.spring.io/spring-boot/docs/current/reference/html/deployment-install.html#deployment-script-customization-when-it-runs).  |
| springboot_deploy_folder | /opt/{{ springboot_application_name }} | Folder where application jar is deployed |
| springboot_user | springboot | Linux user to run spring boot application |
| springboot_group | springboot | Linux group to run spring boot application |


## Example Playbook

Minimal playbook :

    - hosts: all
      vars:
        springboot_application_name: spring-boot-sample
        springboot_src: tests/spring-boot-sample.jar
      roles:
        - role: ansible-springboot
  
If you want to deploy also configuration and/or properties for you application :    
    
    - hosts: all
      vars:
        springboot_application_name: spring-boot-sample
        springboot_src: spring-boot-sample.jar
        springboot_propertyfile_template: /path/to/your/template/application.yml
        springboot_configuration_template: /path/to/your/template/spring-boot-sample.conf
      roles:
        - role: ansible-springboot

## License

BSD

