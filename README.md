# QR CODE GENERATOR AND DECODER

## PROJECT OVERVIEW 
This project is a Python application that allows users to generate and decode QR codes. It provides a simple graphical user interface (GUI) where users can input text or links to generate QR codes. Additionally, the application can decode QR codes and display the encoded information. This tool is useful for creating QR codes for websites, Wi-Fi passwords, contact information, and other text-based data (AKA super top-secret messages shhh).

### Features
- Generate QR codes from text or URL input.
- Set custom parameters for QR codes such as version, box size, and border size.
- Display generated QR codes within the application window.
- Save generated QR codes as PNG files.
- Decode and display information from QR codes.

### Technologies Used
- Python: The main programming language used for developing the application.
- Tkinter: A standard Python library for creating GUI applications.
- OpenCV (cv2): Used for decoding QR codes from saved images.
- qrcode: A Python library for generating QR codes.
- Pillow (PIL): A Python Imaging Library used for handling and manipulating image files.

## Installation 

#### Prerequisites 
- Python 3.x
- pip (Python package installer)
## Steps:
### 1: Clone the Repository
$ git clone https://github.com/dane-meister/QRCode-Generator.git <br>
$ cd QRCode-Generator
### 2: Install Required Python Libraries
$ pip install qrcode[pil] <br>
$ pip install opencv-python <br>
$ pip install pillow

## Running the Application
To run the application, navigate to the cloned directory and execute the main Python script: <br>
$ python main.py

#### License 
This project is licensed under the MIT License.


