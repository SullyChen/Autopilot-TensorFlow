# Autopilot-TensorFlow
A TensorFlow implementation of this [Nvidia paper](https://arxiv.org/pdf/1604.07316.pdf) with some changes. For a summary of the design process and FAQs, see [this medium article I wrote](https://medium.com/@sullyfchen/how-a-high-school-junior-made-a-self-driving-car-705fa9b6e860).

# IMPORTANT
Absolutely, under NO circumstance, should one ever pilot a car using computer vision software trained with this code (or any home made software for that matter). It is extremely dangerous to use your own self-driving software in a car, even if you think you know what you're doing, not to mention it is quite illegal in most places and any accidents will land you in huge lawsuits.

This code is purely for research and statistics, absolutley NOT for application or testing of any sort.

# How to Use
Download the [dataset](https://github.com/SullyChen/driving-datasets) and extract into the repository folder

Use `python train.py` to train the model

Use `python run.py` to run the model on a live webcam feed

Use `python run_dataset.py` to run the model on the dataset

To visualize training using Tensorboard use `tensorboard --logdir=./logs`, then open http://0.0.0.0:6006/ into your web browser.

# Acknowledged/Cited in
D. Qian et al., "End-to-End Learning Driver Policy using Moments Deep Neural Network," 2018 IEEE International Conference on Robotics and Biomimetics (ROBIO), Kuala Lumpur, Malaysia, 2018, pp. 1533-1538.

O’Kelly, M., Sinha, A., Namkoong, H., Duchi, J., & Tedrake, R. (2018). Scalable End-to-End Autonomous Vehicle Testing via Rare-event Simulation.

Pan, X., You, Y., Wang, Z., & Lu, C. (2017). Virtual to Real Reinforcement Learning for Autonomous Driving. [https://arxiv.org/abs/1704.03952](https://arxiv.org/pdf/1704.03952.pdf)

Xu, N., Tan, B., & Kong, B. (2018). Autonomous Driving in Reality with Reinforcement Learning and Image Translation.

https://medium.com/@maxdeutsch/how-to-build-a-self-driving-car-in-one-month-d52df48f5b07

https://mc.ai/self-driving-car-on-indian-roads/

http://on-demand.gputechconf.com/gtc/2018/presentation/s8748-simulate-and-validate-your-dnn-inference-with-catia-before-adas-industrial-deployment.pdf

https://www.ctolib.com/amp/cyanamous-Self-Driving-Car-.html

Message me if I've missed anything!
