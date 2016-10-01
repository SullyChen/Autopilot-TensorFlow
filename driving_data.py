import scipy.misc
import random

xs = []
ys = []

#points to the end of the last batch
batch_pointer = 0

#read data.txt
with open("driving_dataset/data.txt") as f:
    for line in f:
        xs.append("driving_dataset/" + line.split()[0])
        #the paper by Nvidia uses the inverse of the turning radius,
        #but steering wheel angle is proportional to the inverse of turning radius
        #so the steering wheel angle in radians is used as the output
        ys.append(float(line.split()[1]) * scipy.pi / 180)

#get number of images
num_images = len(xs)

#shuffle list of images
c = list(zip(xs, ys))
random.shuffle(c)
xs, ys = zip(*c)

def LoadBatch(batch_size):
    global batch_pointer
    x_out = []
    y_out = []
    for i in range(0, batch_size):
        x_out.append(scipy.misc.imresize(scipy.misc.imread(xs[(batch_pointer + i) % num_images])[-150:], [66, 200]) / 255.0)
        y_out.append([ys[(batch_pointer + i) % num_images]])
    batch_pointer += batch_size
    return x_out, y_out
