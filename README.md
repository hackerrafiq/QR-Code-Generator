# 📱 QR Code Generator using Python

This is a simple QR Code generator script written in Python. It generates QR codes for your coding profiles (LeetCode and GeeksforGeeks) and saves them as image files on your system. The script uses the `qrcode` library along with `Pillow` for optional color customization.

## 🛠️ Prerequisites
Make sure you have Python 3 installed. Then, install the required libraries by running:
pip install qrcode[pil] Pillow

## 🚀 How to Use
1) Clone or download the project files to your local system.
2) Open a terminal or command prompt in the project folder.
3) Run the Python script:
     python main.py
4) Two QR code images will be saved in the same directory:
   i) leetcode.png — a green QR code linking to your LeetCode profile
  ii) geekforgeeks.png — a black-and-white QR code linking to your GeeksforGeeks profile
## 🧠 How It Works
🔹 LeetCode QR Code
    Custom green foreground and white background
    High error correction
    Saved as leetcode.png
    
🔹 GeeksforGeeks QR Code
    Default black and white style
    Simpler method using qrcode.make()
    Saved as geekforgeeks.png
    
##  📁 Output Files
## File Name And Description
**leetcode.png** : QR code for **LeetCode** profile (green theme)
**geekforgeeks.png** : QR code for **GeeksforGeeks** profile

## ✨ Customize It
1) You can easily change the URLs to your own links or any other text by modifying this line in the script:
    qr.add_data("your-link-here")
2) To change color or size, modify:
    make_image(fill_color="green", back_color="white")

##  📚 Future Improvements
    1) Add terminal-based user input to enter custom text or links
    2) Add a GUI using Tkinter for user-friendly QR code creation
    3) Support for batch QR generation from multiple links




