from fastapi import FastAPI, UploadFile
from model import transcribe
from db import save_text, get_history, init_db
import shutil

app = FastAPI()

init_db()

@app.post('/transcribe')
async def transcribe_audio(file: UploadFile):
    file_path = f'temp.wav'
    with open(file_path, 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = transcribe(file_path)
    save_text(text)

    return {'text': text}

@app.get('/history')
def history():
    return get_history()