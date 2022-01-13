import glob
import os

import requests
from PIL import Image
from PyPDF2 import PdfFileMerger


def download_image(page):
    url = f"https://www.ilkokul1.com/wp-content/uploads/flipbook/62/files/mobile/{page}.jpg?210114234309"

    payload = {}
    headers = {
        'authority': 'www.ilkokul1.com',
        'sec-ch-ua': '"Chromium";v="96", " Not A;Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.137 Safari/537.36',
        'sec-ch-ua-platform': '"Windows"',
        'accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-dest': 'image',
        'referer': 'https://www.ilkokul1.com/wp-content/uploads/flipbook/61/book.html',
        'accept-language': 'en-US,en;q=0.5',
        'dnt': '1',
        'sec-gpc': '1'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        with open(f'{page}.jpg', 'wb') as f:
            f.write(response.content)
            f.close()

        open_image = Image.open(f'{page}.jpg')
        convert_image = open_image.convert('RGB')
        convert_image.save(f'{page}.pdf')
    else:
        print("Hatalı Link")


# for i in range(1, 117):
#     print(i)
#     download_image(i)


pdf_files = glob.glob("./*.pdf")
jpg_files = glob.glob("./*.jpg")
merger = PdfFileMerger()

for pdf in pdf_files:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()


for file in pdf_files:
    os.remove(file)

for file in jpg_files:
    os.remove(file)

print("Bitti")
