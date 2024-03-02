import PyPDF2

def replace_first_page(input_pdf_path, replacement_pdf_path, output_pdf_path):
    # Open the input PDFs
    with open(input_pdf_path, 'rb') as input_pdf_file, open(replacement_pdf_path, 'rb') as replacement_pdf_file:
        # Create PDF readers for both input PDFs
        input_pdf_reader = PyPDF2.PdfReader(input_pdf_file)
        replacement_pdf_reader = PyPDF2.PdfReader(replacement_pdf_file)

        # Create a PDF writer for the output PDF
        pdf_writer = PyPDF2.PdfWriter()

        # Add the first page from the replacement PDF to the output PDF
        replacement_page = replacement_pdf_reader.pages[0]
        pdf_writer.add_page(replacement_page)

        # Add the remaining pages from the input PDF to the output PDF
        for page_num in range(1, len(input_pdf_reader.pages)):
            page = input_pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        # Write the result to the output PDF file
        with open(output_pdf_path, 'wb') as output_pdf_file:
            pdf_writer.write(output_pdf_file)

if __name__ == "__main__":
    # Replace 'input.pdf' with the path to your original PDF
    input_pdf_path = r'C:\Users\HP\pracaDyplomowa\dokument_i_źródła\Praca Dyplomowa - Zabezpieczanie Raportów CDR_original.pdf'
    
    # Replace 'replacement.pdf' with the path to the PDF you want to replace the first page with
    replacement_pdf_path = r'C:\Users\HP\pracaDyplomowa\dokument_i_źródła\Dominik Kazana - karta pracy dyplomowej.pdf'
    
    # Replace 'output.pdf' with the desired output PDF file path
    output_pdf_path = r'C:\Users\HP\pracaDyplomowa\dokument_i_źródła\Praca Dyplomowa - Zabezpieczanie Raportów CDR.pdf'

    replace_first_page(input_pdf_path, replacement_pdf_path, output_pdf_path)
