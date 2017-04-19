# Ansible Spring boot

Deploy spring boot applications.

## Requirements

* java : spring boot needs java to run.


## Role Variables

| Variable     | Default       | Description    |
| ------------ | ------------- | -------------- |
| springboot_src |  | Mandatory. Path of the springboot jar to deploy |


## Example Playbook

    - hosts: all
      roles:
        - role: ansible-springboot

## License

BSD

