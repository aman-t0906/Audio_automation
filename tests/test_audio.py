import pytest
from Utils.test_data_reader import load_audio_test_data
from Utils.audio_utils import AudioDevice
from unittest.mock import Mock

test_data = load_audio_test_data()


@pytest.mark.regression
@pytest.mark.parametrize("data", test_data, ids=[data["name"] for data in test_data])
def test_audio_signal(audio_device, data):

    frequency = data["frequency"]
    amplitude = data["amplitude"]
    expected_result = data["expected"]
    result = audio_device.generate_signal(frequency, amplitude) # Generate Signal through signal generator
    assert result == expected_result # compare expected and actual results


@pytest.mark.smoke
def test_audio_playback(audio_device):
    result = audio_device.play("test_audio.wav")
    assert result == "PASS"


def test_device_connection_failures():
    device = AudioDevice("Test_Amplifier")

    with pytest.raises(ConnectionError):
        device.connect()


def test_audio_device_mock():
    device = Mock() # just mock class
    device.connect.return_value = "PASS"
    result = device.connect() # it connect device
    assert result == "PASS"
    device.connect.assert_called_once()

def test_thd():
    device = Mock()
    device.connect.return_value = "PASS"
    thd = Mock.calculate_thd()
    assert thd<1

    device.connect.assert_called_once()

def test_SNR():
    RESULT = "Pass"
    assert RESULT.lower() == "pass"

# JSON
#   ↓
# Python
#   ↓
# Pytest parameterization
#   ↓
# Fixture
#   ↓
# Device class
#   ↓
# Test
#   ↓
# Assertion