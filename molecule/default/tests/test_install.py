import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_artemis_running(Service):
    artemis = Service("artemis-broker")
    assert artemis.is_enabled
    assert artemis.is_running
