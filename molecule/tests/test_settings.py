import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_settings(host):
    settings_file = host.file('/home/testuser/.config/Code/User/settings.json')

    assert settings_file.exists
    assert settings_file.is_file
    assert settings_file.contains('"telemetry.enableTelemetry": false')
