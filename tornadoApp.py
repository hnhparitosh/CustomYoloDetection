import tornado.web
import tornado.ioloop
import tornado.web
import torch
import cv2
import numpy as np
from ultralytics import YOLO

class InferenceHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

        # Load the custom Ultralytics YOLOv8 model
        self.model = YOLO('model2.pt')

    def get(self):
        print('GET request received')
        self.write('Server is up and running!')

    def post(self):
        print('POST request received')
        # Read the image from the request body
        image = np.asarray(bytearray(self.request.body))
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)

        # Make inference
        results = self.model.predict(image, device='cpu', save=False, conf=0.25)
        
        self.write_json(results)

        # Send the results back to the client
        self.set_header('Content-Type', 'application/json')
        self.write(results.pandas().to_json())

application = tornado.web.Application([
    (r'/', InferenceHandler),
])

if __name__ == '__main__':
    application.listen(8888)
    tornado.ioloop.IOLoop.current().start()
