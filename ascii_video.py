import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageOps, ImageFont

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
cap = cv2.VideoCapture('pexels-tima-miroshnichenko-5586710.mp4')
fps = cap.get(cv2.CAP_PROP_FPS)
while(cap.isOpened()):
	ret, frame = cap.read()
	if ret == True:
		# image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# height, width = image.shape
		height, width, layers = frame.shape
		# layers=3 because of 3 dimensional matrix
		size = (width,height)

		cell_w = width/num_cols
		cell_h = scale*cell_w
		num_rows = int(height/cell_h)

		char_width, char_height = font.getsize("A")
		out_width = char_width*num_cols
		out_height = scale*char_height*num_rows

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

		frame_array.append(out_image)
		# cv2.imshow('Frame', out_image)
		# if cv2.waitKey(0):
		# 	break
	else:
		break

out = cv2.VideoWriter('output.mp4',cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
for i in range(len(frame_array)):
	out.write(frame_array[i])
out.release()

cap.release()
cv2.destroyAllWindows()
