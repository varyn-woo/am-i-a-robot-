class ImageData:
    def __init__(self, img, bounds, objects):
        self.img = img
        self.bounds = bounds # dict of objects : a list of their bounding boxes
        self.objects = objects # dict of objects : their count
        assert self.bounds.keys() == self.objects.keys(), "Bounds do not correspond with objects."
        
    def get_img(self):
        return self.img
    
    def get_bounds(self):
        return self.bounds
    
    def get_objects(self):
        return self.objects
    
    # True if the x, y pixel point is within bounds for the given object type
    def in_bounds(self, x, y, object):
        if not object in self.bounds:
            return False
        for bound in self.bounds[object]:
            if (x <= bound['xmax']
                and x >= bound['xmin']
                and y <= bound['ymax']
                and y >= bound['ymin']):
                return True
        return False
    
    # True if the bounds given overlap with the bounds for the given object type
    def has_overlap(self, xmin, xmax, ymin, ymax, object):
        if not object in self.bounds:
            return False
        for bound in self.bounds[object]:
            if (xmin <= bound['xmax']
                and xmax >= bound['xmin']
                and ymin <= bound['ymax']
                and ymax >= bound['ymin']):
                return True
        return False
    
    # Get the number of a certain object
    def get_count(self, object):
        if not object in self.objects:
            return 0
        return self.objects[object]