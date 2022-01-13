import glob
import os

import requests
from PIL import Image
from PyPDF2 import PdfFileMerger


def download_image(book, page):
    if "anyflip" in book:
        url = f"http://online.anyflip.com/uwmxs/bwxh/files/mobile/{page}.jpg"
    else:
        url = f"https://www.ilkokul1.com/wp-content/uploads/flipbook/{book}/files/mobile/{page}.jpg"

    payload = {}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.137 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        with open(f'{page}.jpg', 'wb') as f:
            f.write(response.content)
            f.close()

        open_image = Image.open(f'{page}.jpg')
        convert_image = open_image.convert('RGB')
        convert_image.save(f'{page}.pdf')
        return True
    else:
        return False


book_no = input("Kitap no giriniz = ")

page = 1
while True:
    print(page)
    result = download_image(book_no, page)
    if not result:
        break

    page += 1


pdf_files = glob.glob("./*.pdf")
jpg_files = glob.glob("./*.jpg")
merger = PdfFileMerger()

for pdf in pdf_files:
    merger.append(pdf)

merger.write(f"export.pdf")
merger.close()


for file in pdf_files:
    if not book_no in file:
        os.remove(file)

for file in jpg_files:
    os.remove(file)

print("Bitti")
