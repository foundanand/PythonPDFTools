import PyPDF2

def insert_page(input_pdf, output_pdf, page_to_insert, insert_index):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        pdf_writer = PyPDF2.PdfFileWriter()

        # Add pages before the insertion point
        for i in range(min(insert_index, pdf_reader.numPages)):
            pdf_writer.addPage(pdf_reader.getPage(i))

        # Add the new page
        with open(page_to_insert, 'rb') as page_file:
            page = PyPDF2.PdfFileReader(page_file).getPage(0)
            pdf_writer.addPage(page)

        # Add the remaining pages after the insertion point
        for i in range(insert_index, pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(i))

        # Write the result to the output file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

def remove_page(input_pdf, output_pdf, page_to_remove):
    with open(input_pdf, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        pdf_writer = PyPDF2.PdfFileWriter()

        for i in range(pdf_reader.numPages):
            if i + 1 != page_to_remove:
                pdf_writer.addPage(pdf_reader.getPage(i))

        # Write the result to the output file
        with open(output_pdf, 'wb') as output_file:
            pdf_writer.write(output_file)

# Example usage:
# Replace 'input.pdf', 'output.pdf', 'new_page.pdf' with your actual file names
insert_page('input.pdf', 'output.pdf', 'new_page.pdf', insert_index=2)

# Replace 'input.pdf' and 'output.pdf' with your actual file names
remove_page('input.pdf', 'output.pdf', page_to_remove=3)
