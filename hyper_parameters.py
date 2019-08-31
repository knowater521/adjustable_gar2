data_dir = 's3://adjustable-gar/train_data/'
train_dir = 's3://adjustable-gar/trainset/'
test_dir = 's3://adjustable-gar/testset/'
log_dir = 's3://adjustable-gar/log/'
save_trained_net = 's3://adjustable-gar/save/trained_net.pkl'
save_trained_net_params = 's3://adjustable-gar/save/trained_net_params.pkl'

model_num = 101
epochs = 10
lr_coefficient = 5
weight_decay = 1e-8
batch_size=64
init_lr=0.001

dividing = 1
datadivision_ragne = 19000

model_dir = 's3://adjustable-gar/mod/'

#数据增广参数
img_size = 224
cro_size = 224
angle = 45
brightness=0.05
contrast=0.1 
saturation=0.3 
hue=0.2


