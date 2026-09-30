from Utils.logger import get_logger


class AudioDevice:

    def __init__(self, device_name):
        self.device_name = device_name
        self.logger = get_logger("AudioDevice")

    def connect(self):
        try:
            self.logger.info("Connecting to audio device")
            connection_status = False

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
