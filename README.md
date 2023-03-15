# QR CODE GENERATOR

Simple QR code generator made with python.

## How to use

Type in the text you want to encode, click the generate button and if you want to locally save it, press the save button.

### Buttons

- **Generate**: Generates the QR code according to the text in the input box.

- **Save**: Saves the QR code to an image locally.

### Entry

Just type in the text you want to encode there.

### QR code image

When you generate the QR code, it appears there.

## Used libraries

- Tkinter

- QrCode

- PIL

## How to convert to an executable

- Download the source code as a zip folder and unzip it to a folder.

- Open that folder with the terminal.

- Run this command:
` pip install pyinstaller `

- And lastly, run this one:
` pyinstaller --onedir --noconsole --noconfirm --name "QR Code Generator" --icon "icon.ico" --add-data "icon.ico;." --add-data "README.md;." --hidden-import "qrcode" --paths="C:\Users\~\AppData\Local\Programs\Python\Python311\Lib\site-packages\qrcode" main.py `

- Open the dist folder and run "QR Code Generator.exe".

- Enjoy your QR codes :skull:
