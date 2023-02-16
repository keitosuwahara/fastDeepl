import sys
import pyocr
import pyocr.builders
from PIL import Image
import glob
import os
import deepl
#環境変数「PATH」にTesseract-OCRのパスを設定。
#Windowsの環境変数に設定している場合は不要。
path='C:\\Program Files\\Tesseract-OCR\\'
os.environ['PATH'] = os.environ['PATH'] + path

pngs = sorted(glob.glob("ocr_images/*.png"),reverse=False)

tools = pyocr.get_available_tools()
if len(tools) == 0:
    print("No Ocr Tools")
    sys.exit(1)
tool = tools[0]
print("Will use tool")

langs = tool.get_available_languages()

#ここで翻訳するためのワードリスト作成
translate_text = []

#tkinterで切り取った画像を順々にOCRを実行していく
for i in pngs:
    print(i[-1:-5])
    txt = tool.image_to_string(Image.open(i),lang="eng+jpn",builder=pyocr.builders.TextBuilder())
    translate_text.append(txt)


API_KEY = '05499d30-2ff5-d313-87f7-e431dd43042a:fx' # 自身の API キーを指定

#text = ['コミュニケーションをとることは重要である。', '特にテレワークが主流となった昨今においては、コミュニケーション不足による弊害が多く報告されている。']
source_lang = 'EN'
target_lang = 'JA'

# イニシャライズ
translator = deepl.Translator(API_KEY)

# 翻訳を実行
results = translator.translate_text(translate_text, source_lang=source_lang, target_lang=target_lang)


print("翻訳前\n")
print("".join(translate_text))

print('-'*30)
print("翻訳後\n")

for result in results :
    # print すると翻訳後の文章が出力される
    print(result)
    # 翻訳後の文章にアクセスする場合は .text で可能
    # print(result.text)