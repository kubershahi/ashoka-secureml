import shutil, os

images = os.listdir('DVCData/test/')

for image in images:
	item = image.split('.')[0]
	print(item)
	if int(item) > 100 & int(item) < 201:
		shutil.move('DVCData/test/' + image, 'DVCData/random/')



	