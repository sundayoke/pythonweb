from convertdocx2pdf import convert

def convert_word_to_pdf(input_docx, output_pdf):
       """
       Converts a Word document (.docx) to a PDF file.

       :param input_docx: Path to the input .docx file.
       :param output_pdf: Path to save the output .pdf file.
       """
       try:
           # Convert the Word document to PDF
           convert(input_docx, output_pdf)
           print(f"Conversion successful! PDF saved as {output_pdf}")
       except Exception as e:
           print(f"An error occurred during conversion: {e}")

   # Example usage
input_docx = "letter.docx"  # Replace with your input .docx file path
output_pdf = "letter.pdf"  # Replace with your desired output .pdf file path

convert_word_to_pdf(input_docx, output_pdf)
