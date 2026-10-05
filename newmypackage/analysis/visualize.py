#Imports
from PIL import Image
from PIL import ImageDraw
import numpy as np
import numpy.ma as ma
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
from matplotlib.patches import Rectangle

def plot_visualization(image, boxes, masks, classes, probabilty, output, seg=True): # Write the required arguments

  # The function should plot the predicted segmentation maps and the bounding boxes on the images and save them.
  # Tip: keep the dimensions of the output image less than 800 to avoid RAM crashes.
  
  # indices of the (up to) three most confident detections
  temp = sorted(probabilty)[-3:]
  maxthree = []
  for prob in temp:
    maxthree.append(probabilty.index(prob))
  plt.clf()
  plt.subplot(1,2,1)
  plt.imshow(image)

  ax = plt.subplot(1,2,2)

  if seg == True:
    if not maxthree:  # nothing detected: show an empty mask
      plt.imshow(np.zeros(image.shape[:2]), cmap = 'Greys')
      plt.savefig(output)
      return
    # combine the masks of the selected detections; each mask is (1, H, W)
    mask = masks[maxthree[0]]
    for m in maxthree[1:]:
      mask = mask + masks[m]

    plt.imshow((mask[0] * 255), cmap = 'Greys')
    plt.savefig(output)
  else:
    plt.imshow(image)
    for i,m in enumerate(maxthree):
      x = (boxes[m][0][0] + boxes[m][1][0])/2
      y = (boxes[m][0][1] + boxes[m][1][1])/2
      plt.text(x, y, classes[m], fontsize = 12, color = 'red')
      h = boxes[m][1][1] - boxes[m][0][1]
      w = boxes[m][1][0] - boxes[m][0][0]
      rect = Rectangle(boxes[m][0], w, h, linewidth = 2, edgecolor = 'green', facecolor = 'none')
      ax.add_patch(rect)
    plt.savefig(output)
  
  

  # img.save(output)
