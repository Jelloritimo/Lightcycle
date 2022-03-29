import pyray


class AudioService:


    def start_sound(self):
        pyray.init_audio_device()

    def play_sound(self,filepath):
        sound=pyray.load_sound(filepath)
        pyray.play_sound(sound)