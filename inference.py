import requests
import tornado.escape

image_path = 'test.jpg'
image_bytes = open(image_path, 'rb').read()

response = requests.post('http://localhost:8888/yolo', files={'image': image_bytes})

# Decode the JSON data using the tornado.escape.json_decode() function
predictions = tornado.escape.json_decode(response.content)

print(predictions)