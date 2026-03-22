from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import torch
import librosa

processor = Wav2Vec2Processor.from_pretrained('facebook/wav2vec2-base-960h')
model = Wav2Vec2ForCTC.from_pretrained('facebook/wav2vec2-base-960h')

def transcribe(audio_path):
    speech, _ = librosa.load(audio_path, sr=16000)

    input_values = processor(speech, return_tensors='pt', sampling_rate=16000).input_values

    with torch.no_grad():
        logits = model(input_values).logits

    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.decode(predicted_ids[0])

    return transcription.lower()