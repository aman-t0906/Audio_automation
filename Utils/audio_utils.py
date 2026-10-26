from Utils.logger import get_logger
import numpy as np
from scipy.io.wavfile import read


class AudioDevice:

    def __init__(self, device_name):
        self.device_name = device_name
        self.logger = get_logger("AudioDevice")

    def connect(self):
        try:
            self.logger.info("Connecting to audio device")
            connection_status = True

            if not connection_status:
                raise ConnectionError("Device not responding")
            self.logger.info("Audio device connected")

        except ConnectionError as e:
            self.logger.error(f"Connection failed: {e}")
            raise

    def disconnect(self):
        self.logger.info("Audio device disconnected")

    def play(self, audio_file):
        self.logger.info(f"Playing audio file: {audio_file}")
        return "PASS"

    def generate_signal(self, frequency, amplitude):
        self.logger.info(
            f"Generating signal:"
            f"{frequency} Hz"
            f"{amplitude} v"
        )
        return "PASS"

    def set_volume(self, volume):
        self.logger.info(f"Setting volume to {volume}%")


def analyze_audio(audio_file):
    """
    Analyze a WAV file and return basic audio QA measurements.
    """

    sample_rate, audio = read(audio_file)

    # Normalize integer PCM audio to approximately -1.0 to +1.0
    if np.issubdtype(audio.dtype, np.integer):
        info = np.iinfo(audio.dtype)
        scale = max(abs(info.min), info.max)
        audio = audio.astype(np.float64) / scale
    else:
        audio = audio.astype(np.float64)

    # Convert stereo to mono for these basic measurements
    if audio.ndim == 2:
        audio = audio.mean(axis=1)

    if audio.size == 0:
        raise ValueError("Audio file contains no samples")

    if not np.all(np.isfinite(audio)):
        raise ValueError("Audio contains invalid sample values")

    duration = len(audio) / sample_rate
    peak = float(np.max(np.abs(audio)))
    rms = float(np.sqrt(np.mean(audio ** 2)))

    # Detect samples at or extremely close to digital full scale
    clipped_samples = int(np.sum(np.abs(audio) >= 0.999))

    return {
        "sample_rate": sample_rate,
        "duration": duration,
        "peak_amplitude": peak,
        "rms_amplitude": rms,
        "clipped_samples": clipped_samples
    }

