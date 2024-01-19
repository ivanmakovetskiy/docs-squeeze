
import pdf_struct
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import uvicorn
from datetime import datetime

app = FastAPI(title = "PDF_transform")

@app.post("/pdf")
async def process_pdf_file(file: UploadFile = File(...)):
    contents = await file.read()
    with open(fr'pdf/{file.filename}', 'wb') as f:
      f.write(contents)
    path_to_pdf_file = fr"pdf/{file.filename}"
    out = pdf_struct.predict(
        format='tree',
        in_path=path_to_pdf_file,
        model='PDFContractEnFeatureExtractor'
    )
    out_str = str(out)
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    file_path = f'out/result_{current_datetime}.txt'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(out_str)
    return FileResponse(file_path, media_type="application/text", filename=f"result_{current_datetime}.txt")
if __name__ == "__main__":
  uvicorn.run("main:app", host = 'localhost', port = 8000, reload=True, workers=3)
