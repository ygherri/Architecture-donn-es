import easyocr
import sys

def extract_text(image_path):
    reader = easyocr.Reader(['fr']) 
    result = reader.readtext(image_path)
    return result

def main():
    if len(sys.argv) <= 1:
        print("Veuillez fournir un chemin d'image comme argument.")
        sys.exit(1)

    image_path = sys.argv[1]
    results = extract_text(image_path)

    print("Texte extrait :")
    for (bbox, text, prob) in results:
        print(f"Confiance : {prob:.2f}, Texte : {text}")

if __name__ == "__main__":
    main()
