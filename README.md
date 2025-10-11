# Development of a Stereoscopic Vision System, for a Student Mars Rover


<img width="272" height="361" alt="image" src="https://github.com/user-attachments/assets/0e143eba-f622-4e7f-b3d2-db842f18a9dd" />


## Summary
The aim of this project was to integrate a binocular stereoscopic vision system, into a 2 Degree-of-Freedom robotic head, allowing the operator of the rover remote operation and depth estimation, achieving 64%.

## Mechatronic Design
After research to determine the appropriate method to percieve depth, and into available mechatronics, a binocular stereo vision set up was selected. This featured two high-definition cameras and a raspberry pi to process depth imaging, additional another microcontroller was used to control the 2-DOF dynamics. Torque calculations were taken for servo motor selection, and the housing was optimised for mass and material cost.

## Software
The concept behind stereoscopic vision, required two identical cameras, which are identically constrained with the exception of their lateral placement, or their baseline. This baseline is core to the estimation, as this results in a difference in pixel coordinates of particular objects within the frame, this is the disparity. Disparity is inversely proportional to depth, with baseline and camera focal lengths as constants.


<img width="630" height="247" alt="image" src="https://github.com/user-attachments/assets/4e45f7ec-f3d7-4b31-8e17-7ae17187fa4e" />

I used this idea to develop this process in python, with the help of the OpenCV library, to limited effect.

[`create-depth-map.py`](https://github.com/seb-philo/vision-system/blob/main/create-depth-map.py)

Firstly, the cameras require calibration to remove distortion using grid corner detection, and rectification to ensure the imaging is epipolar (vertically constrained), some samples I practiced with are below: 


<img width="612" height="178" alt="image" src="https://github.com/user-attachments/assets/5200687a-8915-4f50-a3fa-6ffa16a874a2" />


<img width="532" height="220" alt="image" src="https://github.com/user-attachments/assets/0be5d57e-db0a-4575-9758-3d0432b2783f" />


Once complete, the corrected images can then be matches to determine disparity: 


<img width="418" height="316" alt="image" src="https://github.com/user-attachments/assets/7fd06114-f707-46be-95f4-8ce4b0d756bb" />


In practice, however, the cameras I had utilised featured too poor of manufacturing tolerances to be corrected, meaning poor disparity detection.
