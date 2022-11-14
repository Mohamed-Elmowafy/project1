read color rgb from image by using mouse function and display rgb on the image

library:-1- cv2   2- numpy

creat mouse callback function
1.event: the OpenCV mouse event that was detected and triggered the execution of the callback.           event == cv2.EVENT_MOUSEMOVE
2.x: the x coordinate, in the window, of the mouse event.
3.y: the y coordinate, in the window, of the mouse event.
4.flags: one of the flags defined here.
5.params: optional user defined data that can be passed to the callback. Needs to be defined when registering the callback if we want to use it, like mentioned before.

use putText method to write on the image
1.image: on which you can write the text.
2.text: you want to write on image.
3.position: distance along horizontal and vertical axis from top left corner of the image.
4.font: family           cv2.FONT_HERSHEY_SIMPLEX
5.font: size
6.font: color
7.font: stroke width
