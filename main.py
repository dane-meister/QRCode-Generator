import qrcode
import image

qr = qrcode.QRCode(
    version=None,  # version of qr code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # error correction (<=30% = H) 
    box_size=10,  # size of box qr code displayed on
    border=4,  # white border
)


def main():
    generate_qr_code(input("Input: "))


def generate_qr_code(link):
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")
    img.save("qrcode.png")
    print("QR Code generated in qrcode.png")


if __name__ == '__main__':
    main()
