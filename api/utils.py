from io import BytesIO
from pydub import AudioSegment, effects


def wav_byte_array_to_mp3_normalized(byte_array):
    wav_audio = AudioSegment.from_wav(BytesIO(byte_array))
    normalizedsound = effects.normalize(wav_audio)

    mp3_buffer = BytesIO()
    normalizedsound.export(mp3_buffer, format="mp3")
    mp3_byte_array = mp3_buffer.getvalue()

    return mp3_byte_array
