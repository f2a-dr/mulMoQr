import qrcode
from PIL import Image

# Data to encode
url = 'https://github.com/f2a-dr/mulMoQr'

# Path of the logo
logoPath = 'mulmoLogo.png'
logo = Image.open(logoPath).convert('RGBA')

# Resize the logo and apply a white background
basewidth = 600
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
whiteBg = Image.new("RGBA", logo.size, "WHITE")
whiteBg.alpha_composite(logo)
logo = whiteBg

# Generate the QR Code
qrCode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=50)
qrCode.add_data(url)
qrCode.make()
qrColor = 'black'
qrImg = qrCode.make_image(fill_color=qrColor, back_color='white').convert('RGBA')

# Copy the logo on the QR Code
pos = ((qrImg.size[0] - logo.size[0]) // 2, (qrImg.size[1] - logo.size[1]) // 2)
qrImg.paste(logo, pos)

# Save the QR Code
qrImg.save('mulmo_qr.png')
