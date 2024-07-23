import os
from docx import Document

def load_offers(data_dir):
    offers = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".docx"):  
            file_path = os.path.join(data_dir, filename)
            print(f"Loading file: {file_path}")
            document = Document(file_path)
            content = '\n'.join([para.text for para in document.paragraphs]).strip()
            if content:
                offers.append(content)
            else:
                print(f"Warning: {file_path} is empty.")
    return offers

def save_offers(offers, output_file):
    if not offers:
        print("Warning: No offers to save.")
        return

    with open(output_file, "w", encoding='utf-8') as f:
        for offer in offers:
            f.write(offer + "\n\n")

if __name__ == "__main__":
    data_dir = "arhiva/Oferte test"
    output_file = "training_data.txt"
    offers = load_offers(data_dir)
    if offers:
        print(f"Saving {len(offers)} offers to {output_file}.")
        save_offers(offers, output_file)
    else:
        print("No offers found in the directory.")
