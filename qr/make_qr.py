import qrcode, qrcode.image.svg
URL = "https://github.com/riccardosch/cv/releases/latest/download/CV_Riccardo_Schiavo.pdf"
qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=4)
qr.add_data(URL); qr.make(fit=True)
qr.make_image(fill_color="#00A896", back_color="white").save("qr/cv_qr.png")
qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save("qr/cv_qr.svg")
print(URL)
