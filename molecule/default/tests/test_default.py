import os

import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


# These tests are broken, because testinfra wants to test whether a port is
# "listening", and can't test on whether a port is just open.

@pytest.mark.parametrize('socket_def', [
    # ('tcp://80'),
    # ('udp://80'),
    # ('tcp://100'),
    # ('tcp://101'),
    # ('tcp://102'),
    # ('tcp://103'),
    # ('udp://300'),
])
def test_listening_sockets(host, socket_def):
    socket = host.socket(socket_def)
    assert socket.is_listening


@pytest.mark.parametrize('socket_def', [
    ('udp://100'),
    ('udp://101'),
    ('udp://102'),
    ('udp://103'),
    ('tcp://300'),
])
def test_closed_sockets(host, socket_def):
    socket = host.socket(socket_def)
    assert not socket.is_listening
