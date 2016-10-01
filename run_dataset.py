import tensorflow as tf
import scipy.misc
import model
import cv2
from subprocess import call

sess = tf.InteractiveSession()
saver = tf.train.Saver()
saver.restore(sess, "save/model.ckpt")

i = 0
while(cv2.waitKey(10) != ord('q')):
    image = scipy.misc.imresize(scipy.misc.imread("driving_dataset/" + str(i) + ".jpg")[-150:], [66, 200]) / 255.0
    degrees = model.y.eval(feed_dict={model.x: [image], model.keep_prob: 1.0})[0][0] * 180.0 / scipy.pi
    call("clear")
    print("Predicted steering angle: " + str(degrees) + " degrees")
    cv2.imshow("frame", image)
    i += 1

cv2.destroyAllWindows()
