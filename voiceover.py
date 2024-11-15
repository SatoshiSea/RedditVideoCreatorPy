from TTS.api import TTS

voiceoverDir = "Voiceovers"

tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True, gpu=False)

def create_voice_over(fileName, text):
    filePath = f"{voiceoverDir}/{fileName}.wav"  # Usamos .wav para asegurar compatibilidad
    tts.tts_to_file(text=text, file_path=filePath)  # Genera el audio con Coqui TTS
    return filePath
