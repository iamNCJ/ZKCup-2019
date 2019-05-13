from keras.models import Model
from keras.layers import *
import os
import tensorflow as tf
 
 
def keras_to_tensorflow(keras_model, output_dir, model_name,out_prefix="output_", log_tensorboard=True):
 
    if os.path.exists(output_dir) == False:
        os.mkdir(output_dir)
 
    out_nodes = []
 
    for i in range(len(keras_model.outputs)):
        out_nodes.append(out_prefix + str(i + 1))
        tf.identity(keras_model.output[i], out_prefix + str(i + 1))
 
    sess = K.get_session()
 
    from tensorflow.python.framework import graph_util, graph_io
 
    init_graph = sess.graph.as_graph_def()
 
    main_graph = graph_util.convert_variables_to_constants(sess, init_graph, out_nodes)
 
    graph_io.write_graph(main_graph, output_dir, name=model_name, as_text=False)
 
    if log_tensorboard:
        from tensorflow.python.tools import import_pb_to_tensorboard
 
        import_pb_to_tensorboard.import_to_tensorboard(
            os.path.join(output_dir, model_name),
            output_dir)
 
 
"""
We explicitly redefine the Squeezent architecture since Keras has no predefined Squeezenet
"""
 
def squeezenet_fire_module(input, input_channel_small=16, input_channel_large=64):
 
    channel_axis = 3
 
    input = Conv2D(input_channel_small, (1,1), padding="valid" )(input)
    input = Activation("relu")(input)
 
    input_branch_1 = Conv2D(input_channel_large, (1,1), padding="valid" )(input)
    input_branch_1 = Activation("relu")(input_branch_1)
 
    input_branch_2 = Conv2D(input_channel_large, (3, 3), padding="same")(input)
    input_branch_2 = Activation("relu")(input_branch_2)
 
    input = concatenate([input_branch_1, input_branch_2], axis=channel_axis)
 
    return input
 
 
def SqueezeNet(input_shape=(224,224,3)):
 
 
 
    image_input = Input(shape=input_shape)
 
 
    network = Conv2D(64, (3,3), strides=(2,2), padding="valid")(image_input)
    network = Activation("relu")(network)
    network = MaxPool2D( pool_size=(3,3) , strides=(2,2))(network)
 
    network = squeezenet_fire_module(input=network, input_channel_small=16, input_channel_large=64)
    network = squeezenet_fire_module(input=network, input_channel_small=16, input_channel_large=64)
    network = MaxPool2D(pool_size=(3,3), strides=(2,2))(network)
 
    network = squeezenet_fire_module(input=network, input_channel_small=32, input_channel_large=128)
    network = squeezenet_fire_module(input=network, input_channel_small=32, input_channel_large=128)
    network = MaxPool2D(pool_size=(3, 3), strides=(2, 2))(network)
 
    network = squeezenet_fire_module(input=network, input_channel_small=48, input_channel_large=192)
    network = squeezenet_fire_module(input=network, input_channel_small=48, input_channel_large=192)
    network = squeezenet_fire_module(input=network, input_channel_small=64, input_channel_large=256)
    network = squeezenet_fire_module(input=network, input_channel_small=64, input_channel_large=256)
 
    #Remove layers like Dropout and BatchNormalization, they are only needed in training
    #network = Dropout(0.5)(network)
 
    network = Conv2D(1000, kernel_size=(1,1), padding="valid", name="last_conv")(network)
    network = Activation("relu")(network)
 
    network = GlobalAvgPool2D()(network)
    network = Activation("softmax",name="output")(network)
 
 
    input_image = image_input
    model = Model(inputs=input_image, outputs=network)
 
    return model
 
 
keras_model = SqueezeNet()
 
keras_model.load_weights(r"C:/Users/江淼/Desktop/2019train/model/zhongkong_ft_2.h5")
 
 
output_dir = os.path.join(os.getcwd(),"checkpoint")
 
keras_to_tensorflow(keras_model,output_dir=output_dir,model_name="squeezenet.pb")
 
print("MODEL SAVED")