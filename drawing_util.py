from PIL import ImageDraw

def draw_bounding_box(img, bounds, color):
    draw = ImageDraw.Draw(img)
    draw.line([(bounds["xmin"], bounds["ymin"]), 
                (bounds["xmax"], bounds["ymin"]), 
                (bounds["xmax"], bounds["ymax"]), 
                (bounds["xmin"], bounds["ymax"]), 
                (bounds["xmin"], bounds["ymin"])], 
              fill=color,
              width=3)
    return img

def draw_point(img, x, y, color):
    draw = ImageDraw.Draw(img)
    draw.ellipse([(x-3, y-3), (x+3, y+3)], fill=color, width=3)
    return img