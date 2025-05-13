from fastapi import FastAPI, UploadFile, File
from fastapi.responses import FileResponse
import tempfile, os
from tools.generate import generate_facturx_pdf

app = FastAPI()

@app.post("/generate")
async def generate_facturx(pdf: UploadFile = File(...), xml: UploadFile = File(...)):
    with tempfile.TemporaryDirectory() as temp_dir:
        pdf_path = os.path.join(temp_dir, "input.pdf")
        xml_path = os.path.join(temp_dir, "meta.xml")
        output_path = os.path.join(temp_dir, "output_facturx.pdf")

        with open(pdf_path, "wb") as f:
            f.write(await pdf.read())
        with open(xml_path, "wb") as f:
            f.write(await xml.read())

        generate_facturx_pdf(pdf_path, xml_path, output_path)

        return FileResponse(output_path, media_type="application/pdf", filename="facturx.pdf")
