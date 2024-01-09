import qrcode
import tkinter as tk
import cv2
from pyzbar.pyzbar import decode
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

qr_displayed = False

# Default QR Code
qr = qrcode.QRCode(
    version=None,  # version of qr code
    error_correction=qrcode.constants.ERROR_CORRECT_H,  # error correction (<=30% = H)
    box_size=10,  # size of box qr code displayed on
    border=4,  # white border
)


# Validates if input is a digit
def validate_input(P):
    if P == "" or P.isdigit():
        return True
    messagebox.showerror("Type Error", "Please input a number in the specified range!")
    return False


# Initialize the main window
root = tk.Tk()
root.title("QR Code Generator and Decoder")

# Input field for text or link
tk.Label(root, text="Input Text or Link:").pack()
text_input = tk.Text(root, height=2, width=50)
text_input.pack()

# Create a Scrollbar and set its command to the text widget's yview
scrollbar = tk.Scrollbar(root, command=text_input.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the text widget to update the scrollbar
text_input.config(yscrollcommand=scrollbar.set)

# Spinbox for version, box size, and border
version = tk.IntVar(value=0)
box_size = tk.IntVar(value=10)
border = tk.IntVar(value=4)

vcmd = (root.register(validate_input), '%P')

tk.Label(root, text="QR Version (1-40), or 0 for automatic:").pack()
version_spinbox = tk.Spinbox(root, from_=0, to=40, textvariable=version, validate="key", validatecommand=vcmd)
version_spinbox.pack()


tk.Label(root, text="Box Size (1-50):").pack()
box_size_spinbox = tk.Spinbox(root, from_=1, to=50, textvariable=box_size, validate="key", validatecommand=vcmd)
box_size_spinbox.pack()

tk.Label(root, text="Border Size (1-10):").pack()
border_spinbox = tk.Spinbox(root, from_=1, to=10, textvariable=border, validate="key", validatecommand=vcmd)
border_spinbox.pack()


# Function to update QR code specifications
def create_qr_specs(cust_version, cust_box_size, cust_border):
    global qr
    qr = qrcode.QRCode(
        version=cust_version,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=cust_box_size,
        border=cust_border,
    )


# Function to generate QR code
def generate_qr_code():
    # Validation for version, box size, and border
    version_val = version.get()
    box_size_val = box_size.get()
    border_val = border.get()

    if not (0 <= version_val <= 40):
        messagebox.showerror("Input Error", "Version must be a number between 0 and 40.")
        return
    if not (1 <= box_size_val <= 50):
        messagebox.showerror("Input Error", "Box Size must be a number between 1 and 50.")
        return
    if not (1 <= border_val <= 10):
        messagebox.showerror("Input Error", "Border must be a number between 1 and 10.")
        return

    link = text_input.get("1.0", "end-1c")  # Get input from text box, from line 1 char 1 to end - 1 char
    version_ref = version.get()
    if version_ref == 0:
        create_qr_specs(None, box_size.get(), border.get())  # Auto version Update QR specs from user input
    else:
        create_qr_specs(version.get(), box_size.get(), border.get())  # Update QR specs from user input
    qr.add_data(link)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white').convert('RGB')

    # Save the QR code to a file
    img.save("qrcode.png")

    # Resize the QR Code to fit the UI
    qr_image = Image.open("qrcode.png")
    qr_image = qr_image.resize((250, 250))
    qr_photo = ImageTk.PhotoImage(qr_image)

    # Update the UI with the QR code image
    qr_label.config(image=qr_photo)
    qr_label.image = qr_photo  # Keep a reference!
    qr_label.pack()
    global qr_displayed
    if qr_displayed is False:
        save_button.pack(before=decode_button)
    qr_displayed = True
    decode_qr(clear=1)


# Button to generate QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr_code)
generate_button.pack()


# Function to save the QR code image
def save_qr():
    file_path = filedialog.asksaveasfilename(defaultextension='.png',
                                             filetypes=[("PNG files", '*.png'), ("All Files", '*.*')],
                                             title="Save QR Code")
    if file_path:
        qr_image = Image.open("qrcode.png")
        qr_image.save(file_path)
        messagebox.showinfo("Save QR Code", "QR Code saved successfully!")


# Button to save the QR code image
save_button = tk.Button(root, text="Save QR Code", command=save_qr)

# Label to display the generated QR code
qr_label = tk.Label(root)
qr_label.pack()


# Function to decode QR code
def decode_qr(clear=0):
    if clear != 0:
        decode_label.config(text=f"Decoded Message: ")
    else:
        img = cv2.imread('qrcode.png')
        data = decode(img)
        qr_code_message = data[0].data.decode() if data else "No QR code found."
        decode_label.config(text=f"Decoded Message: {qr_code_message}")


# Button to decode QR code
decode_button = tk.Button(root, text="Decode QR Code", command=decode_qr)
decode_button.pack()

# Label to display the decoded message
decode_label = tk.Label(root, text="Decoded Message: ", wraplength=300)
decode_label.pack()


# Start the GUI event loop
root.mainloop()
