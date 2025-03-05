import qrcode

# Data to encode in the QR code
data = "https://drive.google.com/file/d/1vmZldpOrc-vAbdrV9urkBrbsKwZLaS8Y/view?usp=drive_link"  # Replace with your link or text

# Generate QR code
img = qrcode.make(data)

# Save the QR code
img.save("qrcode.png")

# Show the QR code
img.show()
