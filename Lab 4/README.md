# Ph-UI!!!
 
**\*\*\*Sketch 5 designs for how you would physically position your display and any buttons or knobs needed to interact with it.\*\*\***

https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/bb16a69f38b85cbdf0a54d1e8dd5943f70b8f481/Lab%204/sensor-ideation.pdf

**\*\*\*What are some things these sketches raise as questions? What do you need to physically prototype to understand how to anwer those questions?\*\*\***
Sensor placement and display are kind of tricky for gesture recognition. For the light and proximity use cases I've created, having it either be a set-it-and-forget-it type object works well, as well as having it be mobile (although I'm just now realizing the implications of the power source), but for gestures you want to have a clean base, and see the display. Perhaps its not as confusing as I thought though, placing the proximity sensor and the display on the same, top-most side, and having them be far apart might resolve the issues I'm imagining.

**\*\*\*Pick one of these display designs to integrate into your prototype.\*\*\***

Virtual pet plant.

**\*\*\*Explain the rationale for the design.\*\*\*** (e.g. Does it need to be a certain size or form or need to be able to be seen from a certain distance?)

I originally imagined the virtual pet plant to be a handheld, ala Tamagotchi, but the reliance on the power source ruins that idea. Otherwise, it's a fairly simple design, with the display in the center of the box, and the proximity sensor on the top of the box. Having the sensor on the top gives you (hopefully) maximum sunlight while having a head-on view of the display.

Build a cardbord prototype of your design.

**\*\*\*Document your rough prototype.\*\*\***
https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/0bc072f091a128fd80155b9a928cd6e24deea3dd/Lab%204/IMG_1091.jpeg
https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/0bc072f091a128fd80155b9a928cd6e24deea3dd/Lab%204/IMG_1092.jpeg

A basic cover for the Pi. Really shifts around in there, don't know how to mount it without it properly. Cut a small hole up top so the light sensor can work properly.


LAB PART 2

### Part 2

My initial prototyping and brainstorming was about a Tamagotchi-like game that would use the APDS-9960 sensor to detect light, and use that to evolve the little character into a nice big houseplant! It would look like a handheld device, it would work like a virtual pet that responses to light, and it would act like a virtual pet that responses to light and can be restarted when the pet reached its maximum evolution state.

Brainstorm:

https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%204/media/game-brainstorm.pdf

First physical device:

https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/0bc072f091a128fd80155b9a928cd6e24deea3dd/Lab%204/IMG_1091.jpeg

https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/0bc072f091a128fd80155b9a928cd6e24deea3dd/Lab%204/IMG_1092.jpeg

After I finished this though, I realized that this could be extended beyond a virtual pet: It would be an attachment to a flower pot that could help find the right lighting situation in a house for a given plant. It would look like a normal pot for a plant, it would work by getting light from the sensor and displaying that information to the screen, and it would act like a basic way to give a user information about their plants position in relation to the light, and it would respond to where the user positioned the plant.

Unfortunately, I did not have the time to change the code in a satisfactory way from the virtual pet, but I was able to do a quick mock up with images, and then create a cardboard "shell" for the virtual pet. This idea was for it to feel like a normal pot for a plant, but provide the user with helpful information, and then the user could move the plant around to find the ideal lighting situation:

Potted Plant Design:

https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%204/media/no-game.pdf

Potted Plant Prototype:

https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%204/media/IMG_1129.jpeg

https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%204/media/IMG_1130.jpeg

User Testing:

I was able to get my girlfriend to agree to doing a test of the physical plant prototype, although it still had the virtual pet interface. Unfortunately, the lighting in our kitch was too good, and the pet evolved very quickly, although she quickly understood that the number indicated the status of the plant once she noticed it:

https://github.com/BrandonKyleNewman/Interactive-Lab-Hub/blob/Fall2021/Lab%204/media/IMG_1132.MOV

The Future:

I really wish I had more time to create a suitable attachment to an actual plant pot, and modified the interface to not be a game. I can imagine a way you could select what plant you had in the pot, and it would help you find the right level of light in your house for that particular plant.
