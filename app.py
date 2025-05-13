from flask import Flask, request, send_file
import tempfile
import os
from facturx.facturx import add_facturx_to_pdf

app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def generate():
    pdf_file = request.files['pdf']
    xml_file = request.files['xml']

    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_pdf, \
         tempfile.NamedTemporaryFile(delete=False, suffix='.xml') as temp_xml, \
         tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as temp_out:

        pdf_file.save(temp_pdf.name)
        xml_file.save(temp_xml.name)

        # Cette fonction ajoute le XML dans le PDF
        add_facturx_to_pdf(
            pdf_file_path=temp_pdf.name,
            facturx_xml_file_path=temp_xml.name,
            output_pdf_file_path=temp_out.name,
        )

        return send_file(temp_out.name, mimetype='application/pdf', as_attachment=True, download_name='facturx.pdf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
