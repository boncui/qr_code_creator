#QR Code Generator
#Guided by FreeCodeCamp
#Programmed and Written by David Cui

#How to convert a txt or link to a QR Code

#List of Steps to complete project
    #1. install all the libraries needed
    #2. Create the function that collects a text and converts it to a QR Code
    #3. Save the QR Code as a image
    #4. Run the function
    
import qrcode

def generate_QR(text):
    
    qr = qrcode.QRCode(
        version = 1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )
    
    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("qrimg.png")
    
generate_QR("https://open.spotify.com/user/boncui")
