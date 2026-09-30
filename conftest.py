import pytest
from Utils.audio_utils import AudioDevice
from Utils.logger import get_logger

logger = get_logger("Fixture")

"""
| Scope      | Runs                       |
| ---------- | -------------------------- |
| `function` | Once per test              |
| `class`    | Once per test class        |
| `module`   | Once per `.py` test file   |
| `session`  | Once for entire Pytest run |

"""


@pytest.fixture(scope="module")
def test_environment():
    logger.info("creating test env")
    return {
        "device_name": "Test Audio Device",
        "connection": "USB"
    }


@pytest.fixture(scope="module")
def test_config(test_environment):
    logger.info(f"creating test config for {test_environment['device_name']}")
    return {
        "volume": 50,
        "sample_rate": 48000,
        "device": test_environment["device_name"]
    }


@pytest.fixture(scope="module")# we can say one setup and one teardown
def audio_device(test_config):

    logger.info("Setting up audio device")
    device = AudioDevice("Test_Amplifier")
    device.set_volume(test_config["volume"])
    logger.info("\nSetting up audio device...")
    device.connect()

    yield device

    logger.info("\nTearing down audio device...")
    device.disconnect()

