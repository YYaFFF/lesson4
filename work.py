from PIL import Image
monro=Image.open('monro.jpg')
red, green, blue = monro.split()

coordinates_left_red=(100, 0, 696, 522)
red_crop_left=red.crop(coordinates_left_red)
coordinates_left_right_red=(50, 0, 646, 522)
red_crop_left_right=red.crop(coordinates_left_right_red)
connected_monro_red=Image.blend(red_crop_left, red_crop_left_right,0.5)

coordinates_right_blue=(0, 0, 596, 522)
blue_crop_right=blue.crop(coordinates_right_blue)
coordinates_left_right_blue=(50, 0, 646, 522)
blue_crop_left_right=blue.crop(coordinates_left_right_blue)
connected_monro_blue=Image.blend(blue_crop_right, blue_crop_left_right,0.5)

coordinates_green=(50, 0, 646, 522)
green_crop=green.crop(coordinates_green)

avatar=Image.merge("RGB", (connected_monro_red, green_crop, connected_monro_blue))
avatar.save('avatar.jpg')
avatar=Image.open('avatar.jpg')
avatar_size=(80, 80)
avatar.thumbnail(avatar_size)

