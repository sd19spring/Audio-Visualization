Below is the project's UML Diagram.  This diagram provides a high level architectual overview of our code.

*Prepare to have your mind BLOWN*

![UML_Diagram](https://github.com/sd19spring/Audio-Visualization/blob/master/docs/UML%20V1.jpg)

The visualizations are populated by two different classes of shapes: Rectangle and Circle.  

For Rectangles, their width and heights are determined by the energy of the song being played.  High energy songs lead to the creation of bigger shapes and vice versa with low energy songs.  Similarly, the speed at which a Rectangle moves is determined by how danceable a song is deemed by Spotify.  The more danceable a song the faster it moves.  Circle's sizes (i.e. their radii) are determined by bow danceable the song playing is as is their movement speed.  The rate at which a Circle expands is determined by how loud a song is (the louder a song the faster the circle expands).

There are two different movement methods that determine how the rectangles move: floaty and fly.  An interesting element of this code is the part that ensures the ractangles do not dissappear off the screen.  Rather, if the x or y coordinates of a rectangle exceeds that of the screen then the rectangle is put back into the screen.  The Circle class has the floaty and fly movement methods and two more movement methods as well: bubbles and popcorn.  The bubbles method causes the circles to expand and shrink while the popcorn method causes the circles to 'pop' up the screen in a manner that is supposed to resemble popcorn kernels jumping up the microwavable bag.

Note that this program utilizes Pygame extensively.  For more information regarding how Pygame works please see here: https://www.pygame.org/docs/.

An important aspect of our program is the way in which it interacts with Spotify's API.  Spotify's API is how our program data it needs to create the synchronized visualizations.  The following paragraph explains how our program interacts with Spotify's API.

Each class has multiple methods to determine how the shapes moves throughout the visualization.  To ensure the shapes do not simply disappear from the frame, each class has a method that says if a shapes x or y coordinates exceed that of the screen then the coordinates should be reset.

Click [here](index.md) if you miss our amazing homepage
