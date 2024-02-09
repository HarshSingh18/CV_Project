# Cricket Ball Tracking
### This repo is created to collect and showcase work on our Computer Vision project that is Cricket Ball Tracking.

## Table of contents
* [Overview](#overview)
* [Dependencies](#dependencies)
* [Process Flow](ProcessFlow)
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
1. The input video file has to be uploaded in the same folder as Ball_Tracking.py file.
2. The input videos should be of red ball and should not be too long and mainly the ball should be on the pitch or catches behind the wicket/slip.
3. The lighting in the video should be good enough. The weather conditions in the video should not be cloudy.
4. The frames folder is where all the frames from the video gets collected and are then processed.  
## Usage
1. Clone or download the repository
2. Run the python files BallTracker.py where the ball will be tracked using traditional computer vision and YOLOinference.py for seeing YOLO being run on mp4 video files.

## References
1. https://universe.roboflow.com/cricket-2rxrt/cricket-ball-detection/dataset/1
2. https://www.analyticsvidhya.com/blog/2020/03/ball-tracking-cricket-computer-vision/
3. https://stackoverflow.com/questions/73980387/opencv-hough-circles-transform-not-detecting-cricket-ball
4. https://imagecolorpicker.com/color-code/2596be
5. https://www.youtube.com/watch?v=Q0IPYlIK-4A


