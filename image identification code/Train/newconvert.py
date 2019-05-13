from keras.models import Model
from keras.layers import *
import os
import tensorflow as tf

def keras_to_tensorflow(keras_model, output_dir, model_name,out_prefix="output_", log_tensorboard=True):
	if os.path.exists(output_dir) == False:
		os.mkdir(output_dir)