import os
from shutil import copyfile

# Dataset Download Path 
download_path = 'C:/Users/vkost/OneDrive/Desktop/Market-1501-v15.09.15'

# Save path of the files
save_path = download_path + '/pytorch'

# Make the /pytorch path
if not os.path.isdir(save_path):
    os.mkdir(save_path)


#-----------------------------------------

# query files from the dataset
query_path = download_path + '/query'
# path where processed query files are to be saved
query_save_path = download_path + '/pytorch/query'

# query path initialized if doesn't exist
if not os.path.isdir(query_save_path):
    os.mkdir(query_save_path)

# iterate over query files 
for root, dirs, files in os.walk(query_path, topdown=True):
    for name in files:
        # keep going until you find a .jpg file (a picture)
        if not name[-3:]=='jpg':
            continue

        # split by  _ (files follow an ID naming convention)
        ID  = name.split('_')

        # put all files with same IDs in one folder
        src_path = query_path + '/' + name
        dst_path = query_save_path + '/' + ID[0] 

        # if destination doesn't exist, create it
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)

        # copy file from the source path to the destinatino
        copyfile(src_path, dst_path + '/' + name)

#-----------------------------------------
#multi-query
query_path = download_path + '/gt_bbox'
# for dukemtmc-reid, we do not need multi-query
if os.path.isdir(query_path):
    query_save_path = download_path + '/pytorch/multi-query'
    if not os.path.isdir(query_save_path):
        os.mkdir(query_save_path)

    for root, dirs, files in os.walk(query_path, topdown=True):
        for name in files:
            if not name[-3:]=='jpg':
                continue
            ID  = name.split('_')
            src_path = query_path + '/' + name
            dst_path = query_save_path + '/' + ID[0]
            if not os.path.isdir(dst_path):
                os.mkdir(dst_path)
            copyfile(src_path, dst_path + '/' + name)

#-----------------------------------------
#gallery
gallery_path = download_path + '/bounding_box_test'
gallery_save_path = download_path + '/pytorch/gallery'
if not os.path.isdir(gallery_save_path):
    os.mkdir(gallery_save_path)

for root, dirs, files in os.walk(gallery_path, topdown=True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID  = name.split('_')
        src_path = gallery_path + '/' + name
        dst_path = gallery_save_path + '/' + ID[0]
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)
        copyfile(src_path, dst_path + '/' + name)

#---------------------------------------
# train_all
train_path = download_path + '/bounding_box_train'
train_save_path = download_path + '/pytorch/train_all'
# making the train_save_path
if not os.path.isdir(train_save_path):
    os.mkdir(train_save_path)


for root, dirs, files in os.walk(train_path, topdown=True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID  = name.split('_')
        src_path = train_path + '/' + name
        dst_path = train_save_path + '/' + ID[0]
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)
        copyfile(src_path, dst_path + '/' + name)


#---------------------------------------
#train_val
train_path = download_path + '/bounding_box_train'
train_save_path = download_path + '/pytorch/train'
val_save_path = download_path + '/pytorch/val'
if not os.path.isdir(train_save_path):
    os.mkdir(train_save_path)
    os.mkdir(val_save_path)

for root, dirs, files in os.walk(train_path, topdown=True):
    for name in files:
        if not name[-3:]=='jpg':
            continue
        ID  = name.split('_')
        src_path = train_path + '/' + name
        dst_path = train_save_path + '/' + ID[0]
        if not os.path.isdir(dst_path):
            os.mkdir(dst_path)
            dst_path = val_save_path + '/' + ID[0]  #first image is used as val image
            os.mkdir(dst_path)
        copyfile(src_path, dst_path + '/' + name)
