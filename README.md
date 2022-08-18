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

Riboni, A; Ghioldi, N.; Candelieri, A; Borrotti, M. "Bayesian optimization and deep learning for steering wheel angle prediction." (2022) Sci. Rep., 12(1)

H. Zhou et al., "DeepBillboard: Systematic Physical-World Testing of Autonomous Driving Systems," 2020 IEEE/ACM 42nd International Conference on Software Engineering (ICSE), 2020, pp. 347-358.

Yu Shen, Laura Yu Zheng, Manli Shu, Weizi Li, Tom Goldstein, Ming Lin. "Gradient-Free Adversarial Training Against Image Corruption for Learning-based Steering." Advances in Neural Information Processing Systems 34 pre-proceedings (NeurIPS 2021).

M. K. Islam, M. N. Yeasmin, C. Kaushal, M. A. Amin, M. R. Islam and M. I. Hossain Showrov, "Comparative Analysis of Steering Angle Prediction for Automated Object using Deep Neural Network," 2021 9th International Conference on Reliability, Infocom Technologies and Optimization (Trends and Future Directions) (ICRITO), 2021, pp. 1-7

D. Qian et al., "End-to-End Learning Driver Policy using Moments Deep Neural Network," 2018 IEEE International Conference on Robotics and Biomimetics (ROBIO), Kuala Lumpur, Malaysia, 2018, pp. 1533-1538.

O’Kelly, M., Sinha, A., Namkoong, H., Duchi, J., & Tedrake, R. (2018). Scalable End-to-End Autonomous Vehicle Testing via Rare-event Simulation.

Pan, X., You, Y., Wang, Z., & Lu, C. (2017). Virtual to Real Reinforcement Learning for Autonomous Driving. The British Machine Vision Conference.

Xu, N., Tan, B., & Kong, B. (2018). Autonomous Driving in Reality with Reinforcement Learning and Image Translation.

Jiang J., Wang C., Chattopadhyay S., Zhang W. (2020) Road Context-Aware Intrusion Detection System for Autonomous Cars. In: Zhou J., Luo X., Shen Q., Xu Z. (eds) Information and Communications Security. ICICS 2019. Lecture Notes in Computer Science, vol 11999. Springer, Cham. 

Machiraju, H., Balasubramanian, V.N. (2020). A Little Fog for a Large Turn. [https://arxiv.org/abs/2001.05873](https://arxiv.org/abs/2001.05873)

Olmschenk, G. (2019). Semi-super Semi-supervised Regr vised Regression with Gener ession with Generative Adversarial Networks Using Minimal Labeled Data. The Graduate Center, City University of New York. [https://core.ac.uk/download/pdf/228318691.pdf](https://core.ac.uk/download/pdf/228318691.pdf).

Olmschenk, G., Zhu, Z., & Tang, H. (2019). Generalizing semi-supervised generative adversarial networks to regression using feature contrasting. Computer Vision and Image Understanding, 186, 1–12. 

https://medium.com/@maxdeutsch/how-to-build-a-self-driving-car-in-one-month-d52df48f5b07

https://mc.ai/self-driving-car-on-indian-roads/

http://on-demand.gputechconf.com/gtc/2018/presentation/s8748-simulate-and-validate-your-dnn-inference-with-catia-before-adas-industrial-deployment.pdf

https://www.ctolib.com/amp/cyanamous-Self-Driving-Car-.html

Message me if I've missed anything!
