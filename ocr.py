from PIL import Image    
import pytesseract 
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# text = pytesseract.image_to_string(Image.open("./test1.png"),lang="ben")
# print(text)
print(pytesseract.image_to_string(Image.open('./test4.jpg'), lang='ben'))