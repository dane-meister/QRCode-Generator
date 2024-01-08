import qrcode
import image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
import cv2
import numpy as np
from pyzbar.pyzbar import decode


qr = qrcode.QRCode(
    version=None,  # version of qr code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # error correction (<=30% = H)
    box_size=10,  # size of box qr code displayed on
    border=4,  # white border
)


def main():
    print("Hello! Welcome to my QR Code generator. " +
          "Before using make sure you have run the 'pip install qrcode' command.")
    done = -1
    while done == -1:
        done = settings()
    generate_qr_code(input("Input link or text to generate QR Code: "))
    # Decodes qr code for error checking
    decode_qr()


def settings():
    settings_input = input("Would you like to enable default generation settings? (Y/N): ")
    settings_input.upper()
    if settings_input == 'Y':
        create_qr_specs(None, 10, 4)
        return 0
    elif settings_input == 'N':
        print("The version parameter is an integer from 1 to 40 that controls the size of the" +
              "QR Code (the smallest, version 1, is a 21x21 matrix). Set to 0 to determine this automatically.")
        try:
            version = int(input("Input version number [0-40]: "))
            if version > 40 or version < 0:
                print("Please input valid version number as specified.\n")
                return -1
        except ValueError:
            print("That's not a valid number. Please enter a numeric value.\n")
            return -1

        print("The box size parameter controls how many pixels each “box” of the QR code is.")
        try:
            box_size = int(input("Input desired box size (recommended 10): "))
            if box_size < 0 or box_size > 150:
                print("Please input valid box_size number as specified.\n")
                return -1
        except ValueError:
            print("That's not a valid number. Please enter a numeric value.\n")
            return -1

        print("The border parameter controls how many boxes thick the border should be" +
              " (the default is 4, which is the minimum according to the specs).")
        try:
            border = int(input("Input desired border size (>=4): "))
            if border < 4:
                print("Please input valid border size as specified.\n")
                return -1
        except ValueError:
            print("That's not a valid number. Please enter a numeric value.\n")
            return -1

        create_qr_specs(version, box_size, border)
        return 0
    else:
        print("Please input either Y or N.\n")
        return -1


def create_qr_specs(version, box_size, border):
    global qr
    qr = qrcode.QRCode(
        version=version,  # version of qr code
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # error correction (<=30% = H)
        box_size=box_size,  # size of box qr code displayed on
        border=border,  # white border
    )


def generate_qr_code(link):
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill="black", back_color="white")  # basic qr code image

    # experimental custom qr codes
    # img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    # img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
    # img = qr.make_image(image_factory=StyledPilImage, embeded_image_path="./meme.png")

    img.save("qrcode.png")
    print("\nQR Code generated in 'qrcode.png'!")


def decode_qr():
    # Load the image using OpenCV
    img = cv2.imread('./qrcode.png')

    # Decode the QR code
    data = decode(img)

    # Extract the message from the QR code if available
    qr_code_message = data[0].data.decode() if data else "\nNo QR code found.\n"
    print(f"QR Code Decoder -> The message encoded in this qr code is '{qr_code_message}'.")


if __name__ == '__main__':
    main()
