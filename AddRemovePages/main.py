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

def remove_page(input_path, output_path, page_number):
    # Open the input PDF file
    with open(input_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()

        # Add all pages to the writer except the specified page number
        for current_page_number in range(len(pdf_reader.pages)):
            if current_page_number + 1 != page_number:
                page = pdf_reader.pages[current_page_number]
                pdf_writer.add_page(page)

        # Open the output PDF file and write the modified content
        with open(output_path, 'wb') as output_file:
            pdf_writer.write(output_file)

# Example usage:
# Replace 'input.pdf', 'output.pdf', 'new_page.pdf' with your actual file names
# insert_page('input.pdf', 'output.pdf', 'new_page.pdf', insert_index=2)


input_pdf = "/Users/anand/Developer/Python/PythonPDFTools/AddRemovePages/GAISOHB.pdf"
output_pdf_inserted = "/Users/anand/Developer/Python/PythonPDFTools/AddRemovePages/GAISOHB_modified.pdf"  # Update the output file path after insertion
output_pdf_removed = "/Users/anand/Developer/Python/PythonPDFTools/AddRemovePages/GAISOHB_removed.pdf"  # Specify a new output file path for the final result

# Replace 'new_page.pdf' with the actual file name you want to insert
new_page = "AddRemovePages/new_page.pdf"

# Replace 'input.pdf' and 'output.pdf' with your actual file names
# insert_page(input_pdf, output_pdf, new_page, insert_index=2)

# Replace 'input.pdf' and 'output.pdf' with your actual file names
remove_page(input_pdf, output_pdf_removed,3)

