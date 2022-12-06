# Am I a Robot?
## Abstract
Captchas are now ubiquitous. Every time you visit a website, you'll see a "click all images containing *[insert object here]*" prompt to prove that you aren't a robot.
However, vision technology has improved, and even robots can complete Captchas now! To prove this concept, I created a Captcha helper that takes an image, a type of
object, a point, and/or a bounding box, and tells you how many of the object is in the image, whether the point is within the bounding box of one of the specified
objects, and whether the bounding box overlaps with the bounding box of one of the specified objects. Using this tool, one can easily write a script to parse a Captcha
image and determine which squares contain the object of interest, as well as how many of the object are in the image. The existence of this tool proves that Captchas
are no longer necessarily capable of answering the question: are you a robot?
## How to Use
Example command:
```
python detect.py https://ultralytics.com/images/zidane.jpg person -x 10 -y 199 --xmin 0, --xmax 100, --ymin 1, --ymax 293 --image_name zidane
```
### Parameters
#### Positional Arguments

`image` - URL of the image you would like to analyze

`object` - which object you would like to check for

#### Flag Arguments

`-x`, `-y` - x and y coordinates of a point you would like to check

`--xmin`, `--xmax`, `--ymin`, `--ymax` - limits of a bounding box you would like to check

`--image_name` - a short name for the purpose of saving image files (highly recommended; defaults to the full URL if not provided)
