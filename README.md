# ASCII-Art
The ASCII-Art project can convert B&W and RGB images to ascii characters along with asciifying colored videos as well.

## Requirements
- Python 3.6
- tensorflow
- matplotlib
- keras
- numpy
- pandas
- sklearn
- opencv-python

These requirements can be easily installed by:
  `pip install -r requirements.txt`

## Scripts and Files

- __ascii_color_photo.py__: This is the script which converts an image into ascii characters. By default, the script converts images into colored ascii characters but with some small changes, it can be modified to output B&W ascii characters as well.
- __ascii_video.py__: This script converts videos into colored ascii characters video.
- __DejaVuSansMono.ttf__: True Type Font file
- __input1, input2__: Input images
- __output1, output2__: Output colored images with black background
- __video.mp4__: Input video

## Usage

### From scratch
After the requirements have been installed, do the following in the corresponding ascii conversion file (image or video):
1. Specify the input image or input video file path.
3. Specify the output file path.
4. Specify the true type font file path.
5. Run the required script according to your need of asciifying images or videos.

## Internal Working
The script takes video as input and divides it into multiples frames. These frames become the basis of image to ascii conversion. There are two list of characters, one is standard and other is complex, which contains characters in decreasing order of brightness per pixel. In this project, complex one is used. Based on the input and output image total pixels count, average color of a group of pixels in input image defines the color for pixel in output image. So, according to the luminosity and color required, the corresponding ascii character is choosen and placed in the output. This process occurs for all the frames in a video and combining all the output frames gives a final asciified output video.

### Learning Takeaways
I really learned a lot of things through this project. They include opencv library, image processing, luminosity sorting in ascii characters, general image related concepts like resolution, etc, and many other things. Overall it was a really great learning experience!!

## References
- https://www.geeksforgeeks.org/python-play-a-video-using-opencv/
- https://learnopencv.com/how-to-find-frame-rate-or-frames-per-second-fps-in-opencv-python-cpp/
