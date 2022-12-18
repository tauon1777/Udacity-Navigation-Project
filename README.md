
# Udacity Navigation Project

### Environment Description
This project used a deep Q-network to teach an agent how to navigate its environment collecting yellow bananas while avoiding blue ones.

A reward of +1 is provided for collecting a yellow banana, and a reward of -1 is provided for collecting a blue banana. Thus, the goal of your agent is to collect as many yellow bananas as possible while avoiding blue bananas.

The state space has 37 dimensions and contains the agent's velocity, along with ray-based perception of objects around the agent's forward direction. Given this information, the agent has to learn how to best select actions. Four discrete actions are available, corresponding to:

<ul>
  <li> 0 - move forward </li>
  <li> 1 - move backward </li>
  <li> 2 - turn left </li>
  <li> 3 - turn right </li>
</ul>

The task is episodic, and in order to solve the environment, your agent must get an average score of +13 over 100 consecutive episodes.

<p align="center">
  <img src="./assets/banana.gif" />
</p>

<p align="center">
Video of agent navigating the Unity Banana Collector environment.
</p>

### Setting up the Repository

##### List of Dependencies

Below is the list of requirements.
<ul>
<li> python==3.6.3 </li>
<li> numpy==1.12.1 </li>
<li> matplotlib==2.1.0 </li>
<li> torch==0.4.0 </li>
<li> unityagents==0.4.0 </li>
</ul>

unityagents has been replaced by ml-agents

Can be installed with:
python -m pip install mlagents==0.30.0

##### Installation Procedure
Download the environment from one of the links below. You need only select the environment that matches your operating system:

<ul>
  <li> Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip) </li>
  <li> Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip) </li>
  <li> Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip) </li>
  <li> Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip) </li>
</ul>

(For Windows users) Check out this link if you need help with determining if your computer is running a 32-bit version or 64-bit version of the Windows operating system.

(For AWS) If you'd like to train the agent on AWS (and have not enabled a virtual screen), then please use this link to obtain the environment.

Place the file in the DRLND GitHub repository, in the p1_navigation/ folder, and unzip (or decompress) the file.



If needed, additional instructions are located at:

[Udacity Project 1: Navigation](https://github.com/udacity/deep-reinforcement-learning/tree/master/p1_navigation).

[Udacity Deep Reinforcement Learning Repository](https://github.com/udacity/deep-reinforcement-learning#dependencies).

### Training an Agent





