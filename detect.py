import model
import image_data
import urllib.request
import drawing_util
import argparse
from PIL import Image

# COLORS
GREEN = (0, 255, 0, 255)
RED = (255, 0, 0, 255)

parser = argparse.ArgumentParser(
                    prog = 'CaptchaDetector',
                    description = 'Uses AI to detect information required to correctly do a CAPTCHA')

parser.add_argument("image", help="the link to the image to be processed")
parser.add_argument("object", help="the type of object you care about")
parser.add_argument("-x", type=int, help="x coordinate")
parser.add_argument("-y", type=int, help="y coordinate")
parser.add_argument("--xmin", type=int, help="xmin of the bounding box")
parser.add_argument("--xmax", type=int, help="xmax of the bounding box")
parser.add_argument("--ymin", type=int, help="ymin of the bounding box")
parser.add_argument("--ymax", type=int, help="ymax of the bounding box")
parser.add_argument("--image_name", type=str, help="name for the image (defaults to link if not given)")

args = parser.parse_args()
detector = model.Detector()
if args.image_name is None:
    img_name = args.image
else:
    img_name = args.image_name
    
urllib.request.urlretrieve(args.image, f'./images/{img_name}.png')
data = detector.classify(args.image, img_name=img_name)
with Image.open(f'./images/{img_name}.png') as img:
    all_bounds = data.get_bounds()
    for obj in all_bounds:
        if obj == args.object:
            for box in all_bounds[obj]:
                img = drawing_util.draw_bounding_box(img, box, GREEN)
    print("\n\nRESULTS\n-------------------")
    print(f'{args.object} count: {data.get_count(args.object)}')
    if (args.x is not None
        and args.y is not None):
        print(f'{(args.x, args.y)} is within bounding box of a(n) {args.object}: '
            + f'{data.in_bounds(args.x, args.y, args.object)}')
        img = drawing_util.draw_point(img, args.x, args.y, RED)
        
    if (args.xmin is not None
        and args.xmax is not None
        and args.ymin is not None
        and args.ymax is not None):
        print(f'{(args.xmin, args.xmax, args.ymin, args.ymax)} overlaps with '
            + f'bounding box of a(n) {args.object}: '
            + f'{data.has_overlap(args.xmin, args.xmax, args.ymin, args.ymax, args.object)}')
        img = drawing_util.draw_bounding_box(img, 
                                             {
                                                'xmin': args.xmin, 
                                                'xmax': args.xmax, 
                                                'ymin': args.ymin, 
                                                'ymax': args.ymax
                                             }, 
                                             RED)
        
    print(f'The marked up image (saved as images/{img_name}_marked.png) has your provided point and '
          + f'bounding box in red, and the bounding boxes of {args.object} objects in green.')
    img.save(f'./images/{img_name}_marked.png')