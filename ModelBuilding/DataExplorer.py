import os
import matplotlib.pyplot as plt
import torch 
from ModelBuilding.DataLoad import OCRdataset, Collator
from ModelBuilding.TrainEvaluate import TransformList

# Choose the data to display
PATH_TO_TRAIN_IMGDIR = os.environ["PATH_TO_TRAIN_IMGDIR"]
PATH_TO_TRAIN_LABELS = os.environ["PATH_TO_TRAIN_LABELS"]
BATCH_SIZE = 8

# import the transform list used for building data loader for model training and testing from TrainEvaluate.py
transform_list = TransformList.transform_list

dataset = OCRdataset(PATH_TO_TRAIN_IMGDIR, PATH_TO_TRAIN_LABELS, transform_list = transform_list)
collator = Collator()
train_loader = torch.utils.data.DataLoader(dataset, batch_size = BATCH_SIZE, collate_fn = collator, shuffle = True)

examples = []
idx = 0

for batch in train_loader:

    img, true_label = batch['img'], batch['label']
    examples.append([img, true_label])
    idx += 1
    if idx == BATCH_SIZE:
        break

fig = plt.figure(figsize=(10, 10))
rows =  2
columns =  2

# Display some sampples of training/testing data

for j, exp in enumerate(examples):

    fig.add_subplot(rows, columns, j + 1)

    plt.imshow(exp[0][0].permute(2, 1, 0).permute(1, 0, 2))
    plt.title(exp[1][0])