import pytesseract
from PIL import Image


pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def extraire_texte(image_path):
    image = Image.open(image_path)
    texte = pytesseract.image_to_string(image, lang='fra')
    return texte

def resoudre_enigme(texte_enigme):
    reponse = "Réponse simulée pour: " + texte_enigme
    return reponse

image_path = 'arbres/images/image-1.jpeg'

texte_enigme = extraire_texte(image_path)
reponse = resoudre_enigme(texte_enigme)

print("Énigme :", texte_enigme)
print("Réponse :", reponse)
