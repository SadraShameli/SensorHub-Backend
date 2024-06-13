from io import BytesIO
from pydub import AudioSegment, effects


def applyEffects(byte_array):
    wav_audio = AudioSegment.from_wav(BytesIO(byte_array))
    normalizedsound = effects.normalize(wav_audio)

    buffer = BytesIO()
    normalizedsound.export(buffer, format="wav")
    byte_array = buffer.getvalue()

    return byte_array
