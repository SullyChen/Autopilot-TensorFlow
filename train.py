import tensorflow as tf
import driving_data
import model

sess = tf.InteractiveSession()

loss = tf.reduce_mean(tf.square(tf.sub(model.y_, model.y)))
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(loss)
sess.run(tf.initialize_all_variables())

saver = tf.train.Saver()

#train over the dataset about 30 times
for i in range(int(driving_data.num_images * 0.3)):
  xs, ys = driving_data.LoadBatch(100)
  train_step.run(feed_dict={model.x: xs, model.y_: ys, model.keep_prob: 0.8})
  if i % 10 == 0:
    print("step %d, train loss %g"%(i, loss.eval(feed_dict={
         model.x:xs, model.y_: ys, model.keep_prob: 1.0})))
  if i % 100 == 0:
    save_path = saver.save(sess, "save/model.ckpt")
    print("Model saved in file: %s" % save_path)
