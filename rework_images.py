import os
import PIL
from PIL import Image
path = '/home/dmirty/Downloads/stylegan2/dataset/dark-fantasy'
path2 = '/home/dmirty/Downloads/stylegan2/dataset/images'
images = sorted(os.listdir(path))
i = 0
if not os.path.exists(path2):
	os.mkdir(path2)

for img in images:	
	i += 1
	strr = str(path + '/' + img)
	image = Image.open(strr)
	image = image.convert("RGB")
	size = 256, 256
	image = image.resize(size)
	image.save(path2 + '/' + img + '.jpg')
	if i % 100 == 0:
		print(i)
		print('\r', end='')

#python3 Downloads/stylegan2/run_training.py  --num-gpus=1 --data-dir=/home/dmirty/Downloads/test --config=config-f \--dataset=testdataset --mirror-augment=true --total-kimg=450

#python dataset_tool.py create_from_images /home/dmirty/Downloads/dataset/mydataset /home/dmirty/Downloads/pins2/PinDown__samsdimko__pins2
#python run_training.py --num-gpus=1 --data-dir=/home/dmirty/Downloads/dataset --config=config-f \--dataset=mydataset --mirror-augment=true --total-kimg=2220
#python run_generator.py generate-images --seeds=0-999 --truncation-psi=1.0 \ --network=results/00046-stylegan2-mydataset-1gpu-config-f/network-snapshot-000080.pkl