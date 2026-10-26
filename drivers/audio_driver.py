from Utils.audio_utils import AudioDevice


class AudioDriver:

    def __init__(self, device_name):
        self.device = AudioDevice(device_name)

    def connect(self):
        return self.device.connect()

    def disconnect(self):
        return self.device.disconnect()

    def play(self,audio_file):
        return self.device.play(audio_file)

    def set_volume(self, volume):
        return self.device.set_volume(volume)

    def generate_signal(self, frequency, amplitude):
        return self.device.generate_signal(frequency, amplitude)