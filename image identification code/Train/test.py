import sys  
import argparse  
import numpy as np  
from PIL import Image  
from io import BytesIO  
import matplotlib.pyplot as plt  
  
from keras.preprocessing import image  
from keras.models import load_model  
from keras.applications.inception_v3 import preprocess_input, decode_predictions  
	  
# model = load_model(r"C:\Users\zbh11\zhongkong_ft.h5")  
model = load_model(r"C:/Users/江淼/Desktop/2019train/model/zhongkong_ft_2.h5")   
  
def predic(i):  
    img_path = "C:/Users/江淼/Desktop/2019train/data/test/class" + str(i) + ".jpg"  
    # img_path = "C:/Users/江淼/Desktop/2019train/data/test/class2.jpg"  
    # img_path = "F:\\SuperMarket\\SuperMarker2.0\\" + str(i) +".jpg"  
    img = image.load_img(img_path, target_size=(299, 299))  
    x = image.img_to_array(img)  
    x = np.expand_dims(x, axis=0)  
    x = preprocess_input(x)  
    print(x)
    preds = model.predict(x)  
    preds=preds.tolist()  
    ans=[]  
    ans.extend(preds[0])  
    print(ans)  
    result=ans.index(max(ans))  
    print(result)  
    return result

for i in range(2,13):
	print('case ' + str(i))
	predic(i)
	print(' ')
	
# predic(2)