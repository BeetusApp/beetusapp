"Test module"
from beetusapp import beetusapp_lib


def test_add_numbers():
    "Test function"
    value = beetusapp_lib.add_numbers(1, 2)
    assert value == 3
