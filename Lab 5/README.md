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
1. When does it what it is supposed to do?

If my hand is close to my face with an e-cigarette close to my face

2. When does it fail? 

If I bring my hand close to my face.

3. When it fails, why does it fail? 

Not enough testing data around what type of object is close to my face.

4. Based on the behavior you have seen, what other scenarios could cause problems? 

I wonder if I train too much with my right hand with different objects, if that orientation specificity would affect e-cigarette detection.

**\*\*\*Think about someone using the system. Describe how you think this will work.\*\*\***
1. Are they aware of the uncertainties in the system? 

I don't think initially. There's nothing to suggest that bringing any item close to your face would cause an issue.

2. How bad would they be impacted by a miss classification? 

It depends on the individual's health levels, but one puff of an e-cigarette is likely not going to cause significant harm. However, if an individual used this all the time, or the individual had pre-existing respritory issues, there is definitely a chance for harmful impact.

3. How could change your interactive system to address this?

Warnings on startup, occasional popups that say the application is still running. 

4. Are there optimizations you can try to do on your sense-making algorithm. 

More test data.

### Part D
### Characterize your own Observant system

Now that you have experimented with one or more of these sense-making systems **characterize their behavior**.
During the lecture, we mentioned questions to help characterize a material:
* What can you use X for? 

Detecting if an e-cigarette is on or close to one's mouth.

* What is a good environment for X?

At a desk.

* What is a bad environment for X?

Anywhere without a direct headon view (bed, lounging). 

* When will X break?

If a similarly colored/shaped object is moved close to the mouth. For example, a yellow candy bar might trigger the light to go off.

* When it breaks how will X break?

It will not be a precise indicator of e-cigarette usage.

* What are other properties/behaviors of X?

Can detect a background, or just using something close to your face that isn't small and yellow.

* How does X feel?

Cumbersome. Not exactly a nature fit for a standalone device, would be better to use as an application on someones computer already in use.

### Part 2.

Prototyping and Design Exploration:

![Alt Text](https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%205/media/lab_5_designs.pdf)

Experimentation Round 2:

I decided to try out the MediaPipe piece to see if I could get it to recognize my hand. Unfortunately, I found that while it was robust enough to find my fingers if splayed out, it still wasn't up to snuff to show the indicator points if my hand was curled up and around my e-cigarette. I decided to still go with the TeachableMachine, and try a greater variety of poses with objects that weren't e-cigarettes, such as headphones and an energy drink. 

![Alt Text](https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/6279fd1e39d5cefd4a2ab0df5154f678e772e2a0/Lab%205/media/Screen%20Shot%202021-11-08%20at%208.35.45%20AM.png)

It worked out really well on the TeachableMachine demo side! You can see my state of shock when after trying on headphones, drinking from a can, and just existing, I put the e-cigarette up to my mouth and it nailed it on its first try. 

![Alt Text](https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/c6c508699f04fd4f8f133eada015d95917772048/Lab%205/media/Screen%20Shot%202021-11-08%20at%208.38.17%20AM.png)

For the device itself, I wasn't able to come up with a costume that I thought made a lot of sense (I believe this would work better as an application on a computer a user is already using, but it was fun to explore devices anyways). Inititally I thought that using the speaker would be the best option for user feedback, but I then decided it would be best to use the LED light. The light is less intrusive than a speaker, as the user could be in a meeting. The device with the camera would need to be in view of the user anyways, so the light just provides some nice contextual feedback.

User Test (Note, unfortunately, no one wanted to be seen on camera with an e-cigarette device for a graded assignment (fair). So in this video I just demonstrate how it works, and some frustrations I have with it in its current state):

https://drive.google.com/file/d/1bjWbPD8Hj7L5seWX22PYzY2LkIPzMa3K/view?usp=sharing

Conclusion:

The user test wasn't as hopeful as I would have liked. It's frustrating, because using the TeachableMachine website was almost always perfectly accurate; I could try any number of things close to my face and I would get the desired result, but once I put the e-cigarette close to my face, it would indicate that. It was exciting! But once I put it on the pi, as you can see in the video, it took a lot of positioning to get the red indicator to show. Perhaps my original hypothesis that a teachable machine isn't the perfect way to go for this usecase is valid here, but the descrepency is definitely annoying. I also wish I had more time to explore my concept of using the device in bed, however, I think this would have yielded even more wild results. Overall, I had a good time desigining a device that is somewhat useful, as well as exploring the different technologies; I used OpenCV in undergrad and its cool to see all these things built in!
