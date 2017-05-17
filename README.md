# Autopilot-TensorFlow
A TensorFlow implementation of this [Nvidia paper](https://arxiv.org/pdf/1604.07316.pdf) with some changes.

# How to Use
Download the [dataset](https://drive.google.com/file/d/0B-KJCaaF7elleG1RbzVPZWV4Tlk/view?usp=sharing) and extract into the repository folder

Use `python train.py` to train the model

Use `python run.py` to run the model on a live webcam feed

Use `python run_dataset.py 'driving_dataset'` to run the model on the sample driving dataset.

Use `ffmpeg -i youtube_dataset.mp4 -r 25 youtube_dataset/%0d.jpg` followed by `python run_dataset.py 'youtube_dataset'` to test the model on an existing dashcam footage [downloaded from YouTube](https://www.onlinevideoconverter.com/video-converter).

To visualize training using Tensorboard use `tensorboard --logdir=./logs`, then open http://0.0.0.0:6006/ into your web browser.
