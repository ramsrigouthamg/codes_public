
###Tools
It is assumed that OpenCV is already installed.

###The goal:
To make a perspective transformation on an image using homography and overlay it onto the other image.  

###Input :
Two image files - "main image" and "logo image". 
![alt tag](https://github.com/ramsrigouthamg/codes_public/raw/master/opencv/homography/main.jpg)
![alt tag](https://github.com/ramsrigouthamg/codes_public/raw/master/opencv/homography/logo.jpg)

###Output
Overlayed image.
![alt tag](https://github.com/ramsrigouthamg/codes_public/raw/master/opencv/homography/sample_out.jpg)

###Algorithm
The "logo image" is overlayed onto the main image. We need a homography matrix to transform the image points of "logo image" before it is overlayed. To calculate a homography matrix we need 4 correspomding pair of points from "logo image" and "main image". The 4 points for "logo image" are taken as the four corners of the image where as the 4 points for "main image" are chosen by the user. Remember each of the 4 points in each image is of the form (x,y). 

Once homography matrix is calculated the "logo image" is perspectively projected onto the "main image". In this implementation the pixels of "logo image" replace the pixels of "main image". Users can change this to do any other kind of blending.

###Running the code:
Assume that the executable generated is "homography". The images files(main.jpg,logo.jpg) are passed as two arguments. Note that the image files are present in this repository.

     ```
      $ ./homography main.jpg logo.jpg 
      
     ``
###The video link with demo :
https://www.youtube.com/watch?v=R9mvvylyUY0
