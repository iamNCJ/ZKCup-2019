from keras.preprocessing.image import ImageDataGenerator  
from keras.applications.inception_v3 import InceptionV3,preprocess_input  
from keras.layers import GlobalAveragePooling2D,Dense  
from keras.models import Model  
from keras.utils.vis_utils import plot_model  
from keras.optimizers import Adagrad  
from keras.models import load_model  
import numpy  
import tensorflow as tf    
import os    

config = tf.ConfigProto(allow_soft_placement=True)  
#tf.GPUOptions(per_process_gpu_memory_fraction=0.9)  
config.gpu_options.allow_growth = True      #程序按需申请内存    
sess = tf.Session(config = config)    
# 数据准备  
train_datagen = ImageDataGenerator(  
    preprocessing_function=preprocess_input,# ((x/255)-0.5)*2  归一化到±1之间  
    rotation_range=30,  
    width_shift_range=0.2,  
    height_shift_range=0.2,  
    shear_range=0.2,  
    zoom_range=0.2,  
    horizontal_flip=True,  
)  
val_datagen = ImageDataGenerator(  
    preprocessing_function=preprocess_input,  
    rotation_range=30,  
    width_shift_range=0.2,  
    height_shift_range=0.2,  
    shear_range=0.2,  
    zoom_range=0.2,  
    horizontal_flip=True,  
)  
train_generator = train_datagen.flow_from_directory(directory='C:/Users/江淼/Desktop/2019train/data/train',  
                                  target_size=(299,299),#Inception V3规定大小  
                                  batch_size=8)  
val_generator = val_datagen.flow_from_directory(directory='C:/Users/江淼/Desktop/2019train/data/validation',  
                                target_size=(299,299),  
                                batch_size=8)  
# 构建基础模型  
base_model = InceptionV3(weights='imagenet',include_top=False)  
# base_model = load_model('F:/OpenCVLearn/inception_v3_weights_tf_dim_ordering_tf_kernels_notop.h5')  
  
# 增加新的输出层  
x = base_model.output  
x = GlobalAveragePooling2D()(x) # GlobalAveragePooling2D 将 MxNxC 的张量转换成 1xC 张量，C是通道数  
x = Dense(1024,activation='relu')(x)  
predictions = Dense(13,activation='softmax')(x)  
# predictions = Dense(12,activation='softmax')(x)  
model = Model(inputs=base_model.input,outputs=predictions)  
# plot_model(model,'tlmodel.png')  
def setup_to_transfer_learning(model,base_model):#base_model  
    for layer in base_model.layers:  
        layer.trainable = False  
    model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])  
  
def setup_to_fine_tune(model,base_model):  
    GAP_LAYER = 17 # max_pooling_2d_2  
    for layer in base_model.layers[:GAP_LAYER+1]:  
        layer.trainable = False  
    for layer in base_model.layers[GAP_LAYER+1:]:  
        layer.trainable = True  
    model.compile(optimizer=Adagrad(lr=0.0001),loss='categorical_crossentropy',metrics=['accuracy'])  
setup_to_transfer_learning(model,base_model)  
history_tl = model.fit_generator(generator=train_generator,  
                    steps_per_epoch=40,#800  
                    epochs=10,#2  
                    verbose=1,  
                    validation_data=val_generator,  
                    validation_steps=12,#12  
                    class_weight='auto'  
                    )  
# model.save('./zhongkong_tl_2.h5')  
model.save('C:/Users/江淼/Desktop/2019train/model/zhongkong_tl_2.h5')
setup_to_fine_tune(model,base_model)  
history_ft = model.fit_generator(generator=train_generator,  
                                 steps_per_epoch=40,  
                                 epochs=12,  
                                 verbose=1,  
                                 validation_data=val_generator,  
                                 validation_steps=12,  
                                 class_weight='auto')  
# model.save('./zhongkong_ft_2.h5')
model.save('C:/Users/江淼/Desktop/2019train/model/zhongkong_ft_2.h5')
