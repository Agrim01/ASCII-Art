import cv2
import numpy as np
# import ffmpeg
# import colorsys
from PIL import Image, ImageDraw, ImageOps, ImageFont

# class Level(object):

#     def __init__(self, minv, maxv, gamma):
#         self.minv= minv/255.0
#         self.maxv= maxv/255.0
#         self._interval= self.maxv - self.minv
#         self._invgamma= 1.0/gamma

#     def new_level(self, value):
#         if value <= self.minv: return 0.0
#         if value >= self.maxv: return 1.0
#         return ((value - self.minv)/self._interval)**self._invgamma

#     def convert_and_level(self, band_values):
#         h, s, v= colorsys.rgb_to_hsv(*(i/255.0 for i in band_values))
#         new_v= self.new_level(v)
#         return tuple(int(255*i)
#                 for i
#                 in colorsys.hsv_to_rgb(h, s, new_v))

# def level_image(image, minv=0, maxv=255, gamma=1.0):
#     """Level the brightness of image (a PIL.Image instance)
#     All values ≤ minv will become 0
#     All values ≥ maxv will become 255
#     gamma controls the curve for all values between minv and maxv"""

#     if image.mode != "RGB":
#         raise ValueError("this works with RGB images only")

#     new_image= image.copy()

#     leveller= Level(minv, maxv, gamma)
#     levelled_data= [
#         leveller.convert_and_level(data)
#         for data in image.getdata()]
#     new_image.putdata(levelled_data)
#     return new_image

Character = {
    "standard": "@%#*+=-:. ",
    "complex": "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
}

def get_data(mode):
    font = ImageFont.truetype("DejaVuSansMono.ttf", size=20)
    scale = 2
    char_list = Character[mode]
    return char_list, font, scale

bg = "black"
if bg == "white":
  bg_code = (255, 255, 255)
elif bg == "black":
  bg_code = (0, 0, 0)

char_list, font, scale = get_data("complex")
num_chars = len(char_list)
num_cols = 300

frame_array = []
cap = cv2.VideoCapture('video.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
# count = 0
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		# count += 1
		# image = cv2.imread(frame)
		# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# height, width = image.shape
		height, width, layers = frame.shape
		# layers=3 because of 3 dimensional matrix
		size = (width,height)
		# print(width)
		# print(height)

		cell_w = width/num_cols
		cell_h = scale*cell_w
		num_rows = int(height/cell_h)

		char_width, char_height = font.getsize("A")
		out_width = char_width*num_cols
		out_height = scale*char_height*num_rows
		# print(out_height)

		#out_image = Image.new("L", (out_width, out_height), bg_code)
		out_image = Image.new("RGB", (out_width, out_height), bg_code)
		draw = ImageDraw.Draw(out_image)

		#mapping characters for black and white
		# for i in range(num_rows):
		#   min_h = min(int((i+1)*cell_h), height)
		#   row_pix = int(i*cell_h)
		#   line = "".join([char_list[
		#       min(int(
		#           np.mean(image[row_pix:min_h, int(j*cell_w)
		#                   :min(int((j+1)*cell_w),width)])/255*num_chars
		#       ), num_chars-1)]
		#       for j in range(num_cols)]) + "\n"
		#   draw.text((0, i*char_height), line, fill=255-bg_code, font=font)

		#mapping characters for rgb
		for i in range(num_rows):
		  for j in range(num_cols):
		      partial_image = frame[int(i*cell_h):min(int((i+1)*cell_h),height), int(j*cell_w):min(int((j+1)*cell_w), width), :]
		      partial_avg_color = np.sum(np.sum(partial_image, axis=0), axis=0)/(cell_h*cell_w)
		      partial_avg_color = tuple(partial_avg_color.astype(np.int32).tolist())
		      c = char_list[min(int(np.mean(partial_image)*num_chars/255), num_chars-1)]
		      draw.text((j*char_width, i*char_height), c, fill = partial_avg_color, font = font) 

		if bg=="white":
		  cropped_image = ImageOps.invert(out_image).getbbox()
		elif bg=="black":
		  cropped_image = out_image.getbbox()

		out_image = out_image.crop(cropped_image)
		# out_image.save("output1.jpg")
		output_image = np.asarray(out_image)
		r, g, b = cv2.split(output_image)
		output_image = cv2.merge([b, g, r])

		frame_array.append(output_image)
		# if count == 30:
		# 	break
		# cv2.imshow('Frame', output_image)
		# if cv2.waitKey(40):
		# if cv2.waitKey(40) & 0xFF == ord('q'):
			# continue
			# break
	else:
		break

# # fourcc = cv2.FOURCC('m', 'p', '4', 'v')
# out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
# # out = cv2.VideoWriter('output.avi',fourcc, fps, size)
# for i in range(len(frame_array)):
# # for i in range(1):
# 	out.write(frame_array[i])
# 	# cv2.imshow('Frame', frame_array[i])
# # out.release()

delay = int(1000/fps)

for i in range(len(frame_array)):
	cv2.imshow('Frame', frame_array[i])
	if cv2.waitKey(delay):
		continue

cap.release()
# out.release()
cv2.destroyAllWindows()

# cap = cv2.VideoCapture('output.mp4')
# while(cap.isOpened()):
# 	ret, frame = cap.read()
# 	if ret == True:
# 		cv2.imshow('Frame', frame)
# 		if cv2.waitKey(0):
# 			break
# 	else:
# 		break

# cap.release()
# cv2.destroyAllWindows()
