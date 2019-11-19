import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.mark.parametrize('extension', [
    'ms-python.python',
    'vscoss.vscode-ansible'
])
def test_extensions(host, extension):
    output = host.check_output('sudo -u testuser -H code %s %s',
                               '--install-extension', extension)
    assert 'already installed' in output
