import argparse
import json

import numpy as np
import requests
from keras.preprocessing import image

# Argument parser for giving input image_path from command line
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path of the image")
args = vars(ap.parse_args())

image_path = args['image']
# Preprocessing our input image
img = image.img_to_array(image.load_img(image_path, target_size=(224, 224))) / 255.

# this line is added because of a bug in tf_serving(1.10.0-dev)
img = img.astype('float16')

payload = {
    "instances": [{'input_image': img.tolist()}]
}

# sending post request to TensorFlow Serving server
r = requests.post('http://localhost:1234/v1/models/ImageClassifier:predict', json=payload)
pred = json.loads(r.content.decode('utf-8'))

dict['Sleeveless'] = pred['predictions'][0][0]
dict['FullSleeve'] = pred['predictions'][0][1]
dict['HalfSleeve'] = pred['predictions'][0][2]
dict['3/4 Sleeve'] = pred['predictions'][0][3]
y = json.dumps(dict)

print (y)

# Decoding the response
# decode_predictions(preds, top=5) by default gives top 5 results
# You can pass "top=10" to get top 10 predicitons
# print(json.dumps(model.decode_predictions(np.array(pred['predictions']))[0]))
