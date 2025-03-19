import fitz  # PyMuPDF
import os

def extract_text_and_images(pdf_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Dictionary to store text and images
    content_dict = {}

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Extract text and images
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        
        # Extract text and store in dictionary
        text = page.get_text()
        content_dict[f"page_{page_num + 1}_text"] = text
        
        # Extract images and store in dictionary
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_bytes = base_image["image"]
            image_ext = base_image["ext"]
            image_path = os.path.join(output_folder, f"page_{page_num + 1}_image_{img_index + 1}.{image_ext}")
            with open(image_path, "wb") as image_file:
                image_file.write(image_bytes)
            # Store image path in dictionary
            content_dict[f"page_{page_num + 1}_image_{img_index + 1}"] = image_path

    print(f"Extraction complete. Files saved in {output_folder}")
    return content_dict

# test
if __name__ == "__main__":
    pdf_path = "/Users/mostafaelgharib/Desktop/prep_sprint/project_1/the-economics-of-global-climate-change.pdf"
    output_folder = "images_out"
    content_dict = extract_text_and_images(pdf_path, output_folder)
    print(content_dict)
