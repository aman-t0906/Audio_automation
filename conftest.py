
import pytest
from drivers.audio_driver import AudioDriver
from Utils.logger import get_logger
from Utils.config_reader import load_config
config = load_config()
logger = get_logger("Fixture")



@pytest.fixture(scope="module")
def test_environment():
    logger.info("Creating test environment")

    return {
        "device_name": config["device"]["name"],
        "connection": config["device"]["connection"]
    }


@pytest.fixture(scope="module")
def test_config(test_environment):
    logger.info(
        f"Creating test config for {test_environment['device_name']}"
    )

    return {
        "volume": config["audio"]["volume"],
        "sample_rate": config["audio"]["sample_rate"],
        "device": test_environment["device_name"]
    }


@pytest.fixture(scope="module")
def audio_device(test_config):
    logger.info("Setting up audio device")

    device = AudioDriver(test_config["device"])
    device.set_volume(test_config["volume"])
    device.connect()

    yield device

    logger.info("Tearing down audio device")
    device.disconnect()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        if report.passed:
            logger.info(f"TEST PASSED: {item.name}")
        elif report.failed:
            logger.error(f"TEST FAILED: {item.name}")
        elif report.skipped:
            logger.warning(f"TEST SKIPPED: {item.name}")
