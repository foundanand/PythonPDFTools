import PyPDF2

import fitz  # PyMuPDF

def insert_page(input_path, output_path, new_page_path, insert_index):
    # Open the input PDF file
    pdf_document = fitz.open(input_path)

    # Open the new page PDF file
    new_page_document = fitz.open(new_page_path)

    # Insert the new page at the specified index
    pdf_document.insertPDF(new_page_document, from_page=0, to_page=0, to_index=insert_index)

    # Save the modified PDF to the output file
    pdf_document.save(output_path)

    # Close the PDF documents
    pdf_document.close()
    new_page_document.close()




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
insert_index = 2  # Replace with the index where you want to insert the new page

insert_page(input_pdf, output_pdf_inserted, new_page, insert_index)

# Replace 'input.pdf' and 'output.pdf' with your actual file names
# remove_page(input_pdf, output_pdf_removed,3)

