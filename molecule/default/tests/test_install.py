import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_application_running(Service):
    application = Service("spring-boot-sample")
    assert application.is_enabled


def test_application_properties_exists(File):
    propertyFile = File("/opt/spring-boot-sample/application.yml")
    assert propertyFile.exists


def test_application_conf_exists(File):
    configFile = File("/opt/spring-boot-sample/spring-boot-sample.conf")
    assert configFile.exists
