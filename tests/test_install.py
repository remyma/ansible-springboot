import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_application_running(Service):
    application = Service("spring-boot-sample")
    assert application.is_enabled
