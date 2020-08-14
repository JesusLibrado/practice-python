import os
import re
import shutil

name = 'downloads'

folders = os.listdir(f'{name}/')

years = {'2018', '2019', '2020'}


def moveFileToFolder(current_path, to_path, image):
    new_path = f'{to_path}/{image}'
    try:
        shutil.move(current_path, new_path)
    except FileNotFoundError:
        os.makedirs(to_path)
        moveFileToFolder(current_path, to_path, image)
    
for subfolder in folders:
    path = '{folder}/{subfolder}'.format(folder=name, subfolder=subfolder)
    print('Reading {}...'.format(subfolder))
    images = os.listdir(path)
    print('{} elements found'.format(len(images)))
    for image in images:
        for year in years:
            regex = f'{year}\d{{4}}'
            match = re.search(regex, image) 
            if match:
                new_path = f'{year}/{image}'
                print(f'moving {image} -------> {new_path}')
                moveFileToFolder(f'{path}/{image}', year, image)


            

        