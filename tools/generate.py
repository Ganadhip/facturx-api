from PyPDF2 import PdfReader, PdfWriter

def generate_facturx_pdf(pdf_file_path, facturx_xml_file_path, output_pdf_file_path):
    with open(pdf_file_path, "rb") as f_pdf:
        reader = PdfReader(f_pdf)
        writer = PdfWriter()

        for page in reader.pages:
            writer.add_page(page)

        with open(facturx_xml_file_path, "rb") as f_xml:
            writer.add_attachment("factur-x.xml", f_xml.read())

        with open(output_pdf_file_path, "wb") as f_out:
            writer.write(f_out)
