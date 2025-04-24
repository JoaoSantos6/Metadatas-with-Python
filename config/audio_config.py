class AudioConfig:
    def __init__(self):
        self.audio_format = "wav"
        self.sample_rate = 44100
        self.channels = 2
        self.bit_depth = 16
        self.max_duration = 60  # in seconds
        self.min_duration = 1   # in seconds
    