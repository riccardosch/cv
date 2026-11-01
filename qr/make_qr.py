"""Generate the QR codes used in the README (PNG + SVG)."""
import qrcode
import qrcode.image.svg

TARGETS = {
    "cv_qr": "https://github.com/riccardosch/cv/releases/latest/download/CV_Riccardo_Schiavo.pdf",
    "repo_qr": "https://github.com/riccardosch/cv",
}

for name, url in TARGETS.items():
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, box_size=20, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    qr.make_image(fill_color="#00A896", back_color="white").save(f"qr/{name}.png")
    qr.make_image(image_factory=qrcode.image.svg.SvgPathImage).save(f"qr/{name}.svg")
    print(f"{name}: {url}")
