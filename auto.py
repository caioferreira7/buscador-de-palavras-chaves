import pytesseract
from PIL import Image
import pyautogui
import time

pytesseract.pytesseract.tesseract_cmd = r'"C:\Users\caio4\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"'

keywords = ['monitor', 'computador', 'máquina', 'não liga', 'impressora']

def capture_and_search():

    screeenshot = pyautogui.screenshot()
    screeenshot.save("screenshot.png")

    text = pytesseract.image_to_string(screeenshot, lang="por")
    print("Texto encontrado na tela:", text)

    for keyword in keywords:
        if keyword.lower() in text.lower():
            print(f"Palavra-chave encontrada: {keyword}")
            notify_user(keyword)

def notify_user(keyword):
    print(f"🔔 Aviso: A palavra '{keyword}' foi encontrada na tela!")

if __name__ == "__main__":
    print("Monitorando a tela... Pressione Ctrl+C para sair.")
    try:
        while True:
            capture_and_search()
            time.sleep(5)
    except KeyboardInterrupt:
        print("Monitoramento encerrado.")
