import tensorflow as tf 
g = tf.GraphDef()
g.ParseFromString(open(“C:/Users/江淼/Desktop/2019train/converter/tensorflow_model/converted.pb”, “rb”).read())
[n for n in g.node if n.name.find(“input”) != -1] # same for output or any other node you want to make sure is ok