import qrcode
from PIL import Image

user_input_url = input("Enter the url or link you want to create qr code: ")
destination_directory = input("Enter the destination path to save the QR code image: ") 
file_name = input("Enter the name for the QR code image: ")  #type the file name, in your terminal/output section, like this: "[Your file name].[Required Image format, such as .png, .jpg etc]""
fill_color_input = input("Enter the color name for filling the qr code: ")
back_color_input = input("Enter the background color name for the qr code: ")
border_thickness = int(input("Enter the thickness of the border for the qr code: "))
box_size = int(input("Enter the box size for the qr code: "))

destination_path = destination_directory.rstrip('/') + '/' + file_name
qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H, 
                   box_size = box_size, border = border_thickness)
qr.add_data(user_input_url)
qr.make(fit = True)
img = qr.make_image(fill_color = fill_color_input, back_color = back_color_input)
img.save(destination_path)