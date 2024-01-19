import logging
import shutil

import pdf_struct
from fastapi import FastAPI, UploadFile, File, HTTPException
import uvicorn
from pathlib import Path
from fastapi.responses import JSONResponse
"""
path_to_pdf_file = r"pdf_npa_knd/1._______________19.04.2022___295.pdf"
pdf_struct.predict(
  format='paragraphs',
  in_path=path_to_pdf_file,
  model='PDFContractEnFeatureExtractor'

)
"""
app = FastAPI(title = "PDF_transform")


@app.post("/pdf")
async def process_pdf_file(file: UploadFile = File(...)):
    # Save file locally for processing
    contents = await file.read()
    with open(fr'pdf/{file.filename}', 'wb') as f:
      f.write(contents)

    # Process saved file
    return {"filename": file.filename}
if __name__ == "__main__":
  uvicorn.run("main:app", host = 'localhost', port = 8000, reload=True, workers=3)
