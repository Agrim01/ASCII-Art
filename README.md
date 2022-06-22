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
- __summarizer.py__: This script contains all the necessary functions to summarize the text obtained from the pdf.

## Usage

### From scratch
After the requirements have been installed, the process from training to testing is fairly easy. The commands to run:
1. Upload the pdf which is required to be summarised in the main directory.
2. Update the path of the pdf in the main.py script.
3. Update all the paths in the caption.py script from line 40 to 44 accordingly.
4. Run the main.py script.

Hurrah!! You have got yourself some notes compiled from provided pdf along with captioned images! 
