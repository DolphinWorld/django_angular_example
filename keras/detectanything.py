from keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from keras.preprocessing import image
import numpy as np
from keras.models import Model

model = ResNet50(weights='imagenet')
print("initialized")


size = 224
img_path = 'a1.png'

img = image.load_img(img_path, target_size=(size, size))
x = image.img_to_array(img)
x = np.expand_dims(x, axis=0)
x = preprocess_input(x)


preds = model.predict(x) 


print('Predicted:', decode_predictions(preds, top=3)[0])


