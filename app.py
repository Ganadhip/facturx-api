from flask import Flask, request, send_file
import tempfile
import os
import shutil
from facturx.facturx_tools import add_facturx_to_pdf

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    pdf_file = request.files['pdf']
    xml_file = request.files['xml']

    with tempfile.TemporaryDirectory() as temp_dir:
        pdf_path = os.path.join(temp_dir, "source.pdf")
        xml_path = os.path.join(temp_dir, "meta.xml")
        output_path = os.path.join(temp_dir, "facturx_final.pdf")

        pdf_file.save(pdf_path)
        xml_file.save(xml_path)

        add_facturx_to_pdf(pdf_path, xml_path, output_path)

        return send_file(output_path, mimetype='application/pdf', as_attachment=True, download_name='facturx.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
