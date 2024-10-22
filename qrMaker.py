import qrcode
from PIL import Image

url = 'https://it.linkedin.com/company/mulmopro'

logoPath = 'mulmoLogo.png'
logo = Image.open(logoPath).convert('RGBA')

basewidth = 600

wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
whiteBg = Image.new("RGBA", logo.size, "WHITE")
whiteBg.alpha_composite(logo)
logo = whiteBg
qrCode = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=50)

qrCode.add_data(url)

qrCode.make()

qrColor = 'black'

qrImg = qrCode.make_image(fill_color=qrColor, back_color='white').convert('RGBA')

pos = ((qrImg.size[0] - logo.size[0]) // 2, (qrImg.size[1] - logo.size[1]) // 2)
qrImg.paste(logo, pos)

qrImg.save('mulmo_qr.png')
