# Observant Systems


For lab this week, we focus on creating interactive systems that can detect and respond to events or stimuli in the environment of the Pi, like the Boat Detector we mentioned in lecture. 
Your **observant device** could, for example, count items, find objects, recognize an event or continuously monitor a room.

This lab will help you think through the design of observant systems, particularly corner cases that the algorithms needs to be aware of.

## Prep

1.  Pull the new Github Repo.
2.  Install VNC on your laptop if you have not yet done so. This lab will actually require you to run script on your Pi through VNC so that you can see the video stream. Please refer to the [prep for Lab 2](https://github.com/FAR-Lab/Interactive-Lab-Hub/blob/Fall2021/Lab%202/prep.md), we offered the instruction at the bottom.
3.  Read about [OpenCV](https://opencv.org/about/), [MediaPipe](https://mediapipe.dev/), and [TeachableMachines](https://teachablemachine.withgoogle.com/).
4.  Read Belloti, et al.'s [Making Sense of Sensing Systems: Five Questions for Designers and Researchers](https://www.cc.gatech.edu/~keith/pubs/chi2002-sensing.pdf).

### For the lab, you will need:

1. Raspberry Pi
1. Webcam 
1. Microphone (if you want to have speech or sound input for your design)

### Deliverables for this lab are:
1. Show pictures, videos of the "sense-making" algorithms you tried.
1. Show a video of how you embed one of these algorithms into your observant system.
1. Test, characterize your interactive device. Show faults in the detection and how the system handled it.

## Overview
Building upon the paper-airplane metaphor (we're understanding the material of machine learning for design), here are the four sections of the lab activity:

A) [Play](#part-a)

B) [Fold](#part-b)

C) [Flight test](#part-c)

D) [Reflect](#part-d)

---

### Part A
### Play with different sense-making algorithms.

#### OpenCV

**\*\*\*Try each of the following four examples in the `openCV-examples`, include screenshots of your use and write about one design for each example that might work based on the individual benefits to each algorithm.\*\*\***

Contour detection:
![Alt Text](https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%205/media/contour.png)

Face detection:
![Alt Text](https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%205/media/face.png)

Flow detection:
![Alt Text](https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%205/media/flow.png)

Object detection:
![Alt Text](https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%205/media/objects.png)

#### MediaPipe

**\*\*\*Consider how you might use this position based approach to create an interaction, and write how you might use it on either face, hand or body pose tracking.\*\*\***
I actually did this part after I already did the teachable machine part, and that could be a good usecase for a position based approach. By focusing on the hands instead of the structure of an image, it might better detect what is actually happening with the vaping device.

#### Teachable Machines

(**Optionally**: You can train your own model, too. First, visit [TeachableMachines](https://teachablemachine.withgoogle.com/train), select Image Project and Standard model. Second, use the webcam on your computer to train a model. For each class try to have over 50 samples, and consider adding a background class where you have nothing in view so the model is trained to know that this is the background. Then create classes based on what you want the model to classify. Lastly, preview and iterate, or export your model as a 'Tensorflow' model, and select 'Keras'. You will find an '.h5' file and a 'labels.txt' file. These are included in this labs 'teachable_machines' folder, to make the PPE model you used earlier. You can make your own folder or replace these to make your own classifier.)

**\*\*\*Whether you make your own model or not, include screenshots of your use of Teachable Machines, and write how you might use this to create your own classifier. Include what different affordances this method brings, compared to the OpenCV or MediaPipe options.\*\*\***
![Alt Text](https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%205/media/Screen%20Recording%202021-11-01%20at%208.48.18%20PM.mov)
Using my own model, I wanted to create an interaction that could detect if a vaping device was being put up to my mouth. While I think my particular usecase might not be the best use for a teachable machine (it seemed to get confused any time any object was brought close to my head, so more testing data needs to be introduced), the ability to add new data of your own choice is a powerful feature over the other two options.

### Part B
### Construct a simple interaction.

Pick one of the models you have tried, pick a class of objects, and experiment with prototyping an interaction.
This can be as simple as the boat detector earlier.
Try out different interaction outputs and inputs.

**\*\*\*Describe and detail the interaction, as well as your experimentation here.\*\*\***
![Alt Text](https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%205/media/Screen%20Recording%202021-11-01%20at%208.48.18%20PM.mov)
Over the pandemic I developed the a habit of e-cigarette usage. While e-cigarettes currently show promise in being a better altnernative to a traditional cigarette, my goal is to quit nicotine usage before the year ends. This prompted me to create an interaction that can detect if I'm bringing an e-cigarette up to my mouth, and would alert me if I was.

At first, I thought this would be a very natural fit for a teachable machine: is there an e-cigarette in my hand or not. My first round of trials, my 1st clasifier I recorded my face being very static, my 2nd classifier I simulated me bringing an e-cigarette to my face with plastic lighter (no e-cigarettes in the house!). My trial, unfortunately almost always classified me as 2, presumably because I wasn't looking head on into the camera.

I was able to fine tune a bit, and had my head be more flexible for the first classifier. This helped a lot. I did not test for different objects, such as drinking from a coffee cup.

### Part C
### Test the interaction prototype

Now flight test your interactive prototype and **note down your observations**:
For example:
1. When does it what it is supposed to do? If my hand is close to my face with an e-cigarette close to my face
1. When does it fail? If I bring my hand close to my face.
1. When it fails, why does it fail? Not enough testing data around what type of object is close to my face.
1. Based on the behavior you have seen, what other scenarios could cause problems? I wonder if I train too much with my right hand with different objects, if that orientation specificity would affect e-cigarette detection.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system? I don't think initially. There's nothing to suggest that bringing any item close to your face would cause an issue.
1. How bad would they be impacted by a miss classification? It depends on the individual's health levels, but one puff of an e-cigarette is likely not going to cause significant harm. However, if an individual used this all the time, or the individual had pre-existing respritory issues, there is definitely a chance for harmful impact.
1. How could change your interactive system to address this? Warnings on startup, occasional popups that say the application is still running. 
1. Are there optimizations you can try to do on your sense-making algorithm. 

More test data

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for?
* What is a good environment for X?
* What is a bad environment for X?
* When will X break?
* When it breaks how will X break?
* What are other properties/behaviors of X?
* How does X feel?

**\*\*\*Include a short video demonstrating the answers to these questions.\*\*\***

### Part 2.

Following exploration and reflection from Part 1, finish building your interactive system, and demonstrate it in use with a video.

**\*\*\*Include a short video demonstrating the finished result.\*\*\***
