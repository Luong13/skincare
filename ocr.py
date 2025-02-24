from PIL import Image
import pytesseract  # Transforming image to string and printing it!
import nltk
import json 
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt_tab')
#troubleshoots issue where tesseract cannot be found in PATH
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"


def tokenize_img(img:str):
    img = Image.open(img)
    img_str = pytesseract.image_to_string(img)
    tokens = word_tokenize(img_str)

    print(tokens)

def initialize_ingredient_database():
    img = Image.open('initial list of ingredients.png')
    img_str = pytesseract.image_to_string(img)
    tokens = img_str.split('\n')
    ingredients = []
    purposes = []
    concerns = []
    lst = []
    for token in tokens:
        if not token:
            continue
        if 'Purpose' in token and not ingredients:
            ingredients.append(lst)
            lst = []
        if 'Skin Concerns' in token and not purposes:
            purposes.append(lst)
            lst = []
        lst.append(token)
    concerns.append(lst)
    
    ingredients = ingredients[0]
    purposes = purposes[0]
    concerns = concerns[0]
    
    ingr_db = {}
    for i in range(len(ingredients)):
        entry = {
            ingredients[i]: {
                "Purpose": purposes[i],
                "Concerns": concerns[i],
            },
        }
        ingr_db.update(entry)
        
    with open('ingredient_database.txt', 'w') as f: 
        f.write(json.dumps(ingr_db))

initialize_ingredient_database()