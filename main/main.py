from PIL import Image


image_monro = Image.open('monro.jpg')
red, blue, green = image_monro.split()

coordinate_left = (50, 0, red.width, red.height)
coordinate_center = (25, 0, 671, 522)
red_left = red.crop(coordinate_left)
red_center = red.crop(coordinate_center)
red_image = Image.blend(red_left, red_center, 0.3)

coordinate_left = (0, 0, 646, 522)
coordinate_center = (25, 0, 671, 522)
blue_left = blue.crop(coordinate_left)
blue_center = blue.crop(coordinate_center)
blue_image = Image.blend(blue_left, blue_center, 0.3)

coordinate = (25, 0, 671, 522)
green_image = green.crop(coordinate)

new_image = Image.merge("RGB", (red_image, green_image, blue_image))
new_image.save("new_monro", format='JPEG')

profile_picture = Image.open('new_monro')
profile_picture.thumbnail((80, 80))
profile_picture.save("profile_picture", format="JPEG")




