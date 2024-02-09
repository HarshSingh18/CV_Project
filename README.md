# Cricket Ball Tracking
### This repo is created to collect and showcase work on our Computer Vision project that is Cricket Ball Tracking.

## Table of contents
* [Overview](#overview)
* [Dependencies](#dependencies)
* [Process Flow](ProcessFlow)
* [Methodology](#Methodology)
* [Impact](#Impact)
* [Future Application](#Future Application)
* [Usage](#usage)
* [References](References)

## Overview
This repository contains the implementation of our cricket ball tracking software which is tracking a cricket ball in real time with video snippets from live cricket as input and outputting a video with bounding box on the ball. This README provides an overview of the dependencies, requirements and usage instructions.

## Dependencies

opencv

numpy

regex

imutils

os

matplotlib.pyplot

ultralytics

You can install all the above mentioned dependencies by running the following command
```
pip install -r requirements.txt
```


## Process Flow
1. Unzip the file CV_Project.zip and run Ball_Tracking.py file
2. The input video file has to be uploaded in the same folder as Ball_Tracking.py file.
3. Press q while the frames are getting stored if the video is taking too long to run.
4. The input videos should be of red ball and should not be too long and mainly the ball should be on the pitch or catches behind the wicket/slip.
5. The lighting in the video should be good enough.The weather conditions in the video should not be cloudy.
6. The Frame folder is where all the frames from the video gets collected and are then processed.
6. The Frame_b folder is where all the processed frames contaning bounding boxes are collected.
   
## Methodology
1. Coverting all the frames of a video uploaded to HSV Color Space.
2. Thresholding/Masking every frame to create a mask on the cricket ball. We want to separate the cricket ball from the image. We have converted our image from RGB    to HSV color space to enhance the process of masking. We have applied two masks on the ball and combined them to generate a better mask.
3. Contour detection on the masked image, approximating the contours to a circle and using contour properties like area, perimeter and circularity to filter the       noisy contours by using some thresholds. Used certain threshold values that are corresponding to a cricket ball area and circularity.
4. Circularity of the contour is taken as the contour that contains the ball should be circular.
5. Building bounding boxes around the ball in each frame using the contour coordinates.
6. Collecting all the processed images to form the output video.
   
## Impact 
The real-time tracking of a cricket ball's motion holds significant implications for sports analysis and player performance assessment. By accurately capturing the fast-moving ball, this project contributes to the enhancement of cricket match analytics. This project can become a template for doing object tracking of very fast moving objects with certain changes in the code like changing the threshold values corresponding to shape and size of the object and changing the lower range and upper range values in the HSV color space to create a mask on the ball depending on the colour of the ball. 

## Future Application
1. Enhancing the accuracy of the model to generalize it better to work on balls of any colour.
2. Capturing the ball in night time while incorporating change in lighting conditions.
3. Capturing the ball in cloudy conditions and incorporating the condition of the ball.
4. Predicting the trajectory of the cricket ball as it hits the pads.


## Usage
1. Clone or download the repository
2. Run the python files BallTracker.py where the ball will be tracked using traditional computer vision and YOLOinference.py for seeing YOLO being run on mp4 video files.

## References
1. https://universe.roboflow.com/cricket-2rxrt/cricket-ball-detection/dataset/1
2. https://www.analyticsvidhya.com/blog/2020/03/ball-tracking-cricket-computer-vision/
3. https://stackoverflow.com/questions/73980387/opencv-hough-circles-transform-not-detecting-cricket-ball
4. https://imagecolorpicker.com/color-code/2596be
5. https://www.youtube.com/watch?v=Q0IPYlIK-4A


