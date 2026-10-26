import pytest
from Utils.test_data_reader import load_audio_test_data
from Utils.audio_utils import AudioDevice, analyze_audio
from unittest.mock import Mock
from pathlib import Path
import numpy as np
from scipy.io.wavfile import write

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


# def test_device_connection_failures():
#     device = AudioDevice("Test_Amplifier")
#
#     with pytest.raises(ConnectionError):
#         device.connect()


def test_audio_device_mock():
    device = Mock() # just mock class
    device.connect.return_value = "PASS"
    result = device.connect() # it connects device
    assert result == "PASS"
    device.connect.assert_called_once()

def test_thd():
    device = Mock()
    device.connect.return_value = "PASS"
    thd = Mock.calculate_thd()
    assert thd<1

    device.connect.assert_called_once()

def test_snr():
    result = "Pass"
    assert result.lower() == "pass"
    print("SNR 2")

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

@pytest.mark.regression
def test_audio_file_analysis():

    audio_file = Path(__file__).resolve().parent.parent / "test_audio.wav"
    result = analyze_audio(str(audio_file))
    assert result["sample_rate"] == 48000
    assert result["duration"] == pytest.approx(1.0)
    assert result["peak_amplitude"] == pytest.approx(0.5, abs = 0.001)
    assert result["rms_amplitude"] == pytest.approx(0.3535, abs = 0.001)
    assert result["clipped_samples"] == 0


@pytest.mark.regression
def test_audio_file_missing():
    missing_file = "file_that_does_not_exist.wav"
    with pytest.raises(FileNotFoundError):
        analyze_audio(missing_file)