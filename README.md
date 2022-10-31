# DeepGTAV - PreSIL
## Precise Synthetic Image and LiDAR Dataset for Autonomous Vehicle Perception

*A plugin for GTAV that transforms it into a vision-based self-driving car research environment. This repo outputs HD images, LiDAR, depth, stencil, and labels in KITTI and augmented formats. Please cite our work, the PreSIL dataset for autonomous vehicle perception (https://arxiv.org/abs/1905.00160) if using this repo.*

To download pre-generated data see: https://uwaterloo.ca/waterloo-intelligent-systems-engineering-lab/presil-dataset-downloader

Visualization and tools to work with the data can be found here: https://github.com/bradenhurl/PreSIL-tools

Visualizations from the PreSIL Dataset:

Image with 2D Boxes
<img src="https://github.com/bradenhurl/DeepGTAV-PreSIL/blob/master/samples/342-image.png" alt="Image with 2D boxes" width="900px">
Pointcloud with 3D Boxes
<img src="https://github.com/bradenhurl/DeepGTAV-PreSIL/blob/master/samples/342-pc.png" alt="Pointcloud with 3D boxes" width="900px">
Linearized Depth Buffer
<img src="https://github.com/bradenhurl/DeepGTAV-PreSIL/blob/master/samples/342-depth.png" alt="Linearized Depth Buffer" width="900px">
Linearized Depth Buffer shown in color
<img src="https://github.com/bradenhurl/DeepGTAV-PreSIL/blob/master/samples/342-depth-color.png" alt="Linearized Depth Buffer with Color" width="900px">
Instance Level Object Segmentation
<img src="https://github.com/bradenhurl/DeepGTAV-PreSIL/blob/master/samples/342-segImg.png" alt="Object instance level segmentation" width="900px">
Stencil Buffer
<img src="https://github.com/bradenhurl/DeepGTAV-PreSIL/blob/master/samples/342-stencil.png" alt="Stencil Buffer" width="900px">


## Synthetic automotive LiDAR dataset with radial velocity additional feature - (x,y,z,v)
The synthetic dataset generated is accessible in https://doi.org/10.5281/zenodo.7184990. It is comprised by 15000 frames with KITTI-like format, with the following point clouds:
- Point cloud 1: (x,y,z, (Bool)Is_Object): In this point cloud, the best performance of the Deep Learning model is expected as ground truth information is provided as the additional feature of each point.
  - Point cloud 1A: (x,y,z, (Bool)Is_Car): the additional feature of each point that belongs to an object of the ’Car’ type has a Boolean 1.0 value; contrariwise, the 0.0 value was used. File: velodyne_1A_isCar;
  - Point cloud 1B: (x,y,z, (Bool)Is_Ped): the additional feature of each point that belongs to an object of the ’Pedestrian’ type has a Boolean 1.0 value; contrariwise, the value 0.0 was used.  File: velodyne_1A_isPed.
- Point cloud 2: (x,y,z, (Float)Radial_Velocity): this point cloud has the relative radial velocity as an additional feature for each point. File: velodyne_2_radial_velocity;
- Point cloud 3: (x,y,z,(Float)Abs_Speed): in this point cloud, every point has the absolute speed of the object as the additional feature. File: velodyne_3_absolute_speed;
- Point cloud 4: (x,y,z,(Bool)Is_Moving): the additional feature of each point is a Boolean value that is set to 1.0 if the object is moving, contrariwise is set to 0.0 if the object is static. File: velodyne_4_is_moving;
- Point cloud 5: (x,y,z,0): no additional feature information. If desired, requires post-processing to convert to (x,y,z) or changing the toolbox point cloud configuration to not consider the additional feature. File: velodyne_5_xyz;



## Modifications to the default PreSIL dataset generation source code
Sensor specifications:
1. Point cloud range changed to 69.12 m (default distance at OpenPCDet toolbox for annotations, PC is not used past that distance). File: Constants.h;
2. Point cloud annotations changed to 69.12 m (default distance at OpenPCDet toolbox for KITTI like annotations). File: Constants.h;
3. Frame rate changed to 0.2 Hz for more scenario diversity. File: VPilot/veldrive.

KITTI annotations:
1. The PreSIL occlusion value is converted to a KITTI level. Since no threshold is available by KITTI, a visual inspection was made.
  1.1 [0.0,0.2[ are assigned level 0 occlusion -> fully visible;
  1.2 [0.2,0.6[ are assigned level 1 occlusion -> partly occluded;
  1.3 [0.6,1] are assigned level 2 occlusion -> largely occluded.
  File: ObjectDetection.cpp.
  
2. To improve PreSIL object type consistency, the vehicle model to object type was reviewed with object reclassified according to their dimensions.
  File: ObjectDet/vehicle_labels.csv.


## Added features to PreSIL dataset generation source code
1. The following 6 point clouds were included to the dataset generation source code:
  - Point cloud 1A: (x,y,z, (Bool)Is_Car): the additional feature of each point that belongs to an object of the ’Car’ type has a Boolean 1.0 value; contrariwise, the 0.0 value was used. Output file name: velodyne_1A_isCar;

  <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/000981.png" alt="Frame from the dataset" width="900px">
  <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/isCarPC.png" alt="Car GT additional feature" width="900px">
  
   - Point cloud 1B: (x,y,z, (Bool)Is_Ped): the additional feature of each point that belongs to an object of the ’Pedestrian’ type has a Boolean 1.0 value; contrariwise, the value 0.0 was used.  Output file name: velodyne_1A_isPed.
   
     <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/000981.png" alt="Frame from the dataset" width="900px">
  <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/isPedPC.png" alt="Pedestrian GT additional feature" width="900px">

   - Point cloud 2: (x,y,z, (Float)Radial_Velocity): this point cloud has the relative radial velocity as an additional feature for each point. File: velodyne_2_radial_velocity;
   
  <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/000981.png" alt="Frame from the dataset" width="900px">
  <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/radial_velocityPC.png" alt="Radial velocity additional feature" width="900px">
    
   - Point cloud 3: (x,y,z,(Float)Abs_Speed): in this point cloud, every point has the absolute speed of the object as the additional feature. Output file name: velodyne_3_absolute_speed;

  <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/000981.png" alt="Frame from the dataset" width="900px">
  <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/abs_speedPC.png" alt="Car absolute speed additional feature" width="900px">

   - Point cloud 4: (x,y,z,(Bool)Is_Moving): the additional feature of an object is a Boolean value that is set to 1.0 if the object is moving, contrariwise is set to 0.0. Output file name: velodyne_4__is_moving;
  
  <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/000981.png" alt="Frame from the dataset" width="900px">
  <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/isMovingPC.png" alt="Car is moving additional feature" width="900px">
   
  
   - Point cloud 5: (x,y,z,0): no additional feature information. If desired, requires post-processing to convert to (x,y,z) or changing the toolbox point cloud configuration to not consider the additional feature. Output file name: velodyne_5_xyz;
   
  <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/000981.png" alt="Frame from the dataset" width="900px">
  <img src="https://github.com/leandroalexandrino1995/DeepGTAV-PreSIL/blob/master/samples/xyzPC.png" alt="No additional additional feature" width="900px">

File with the point clouds data acquisition: ObjectDet/LiDAR.cpp.

2. Frame rate is changed if the vehicle is stopped to improve scenario diversity. File: Scenario.cpp.

## Installation
1. Make sure GTAV is on version 1.0.1180.2 or below
2. Copy-paste the contents of *bin/Release* under your GTAV installation directory
3. Replace your saved game data in *Documents/Rockstar Games/GTA V/Profiles/* with the contents of *bin/SaveGame*
4. Download *[paths.xml](https://drive.google.com/file/d/0B6pR5O2YrmHnNU9EMDBSSFpMV00/view?usp=sharing)* and store it also in the GTAV installation directory. 
5. Download Eigen (http://eigen.tuxfamily.org/index.php?title=Main_Page) and create an environment variable (EIGEN_DIR) pointing to its directory.
6. Obtain the VisionNative-Depth Extractor repo (https://github.com/bradenhurl/GTAVisionExport-DepthExtractor). Follow instructions to build the native repository.
7. Create an environment variable (GTAVisionLib) pointing to the build path of GTAVisionNative.lib (from the previous step).
8. Create an environment variable (GTAV_INSTALL_DIR) pointing to the GTAV installation directory.
9. Create an environment variable (DEEPGTAV_DIR) pointing to the directory of this repository.
10. Create an environment variable (DEEPGTAV_LOG_FILE) pointing to the file for logging (debugging purposes).
11. Create an environment variable (DEEPGTAV_EXPORT_DIR) pointing to the export location.
12. Download and install opencv (https://opencv.org/releases/). Place opencv_world343.dll in the GTAV installation directory.

## Recommendations

1. Under your game settings, set your screen to windowed mode
2. Bypass the menu screen by configuring GTAV to start directly into Story Mode
3. To avoid the Rockstar updates, start the game using GTA5.exe, otherwise use GTAVLauncher.exe or PlayGTAV.exe

## Running Data Collection

1. Start the game, walk outside of building if player is in one (game can crash if inside a building)
2. Open a terminal to the VPilot subdirectory in this repository
3. Start collection by running the dataset script in python i.e. 'python dataset'
4. Press Ctrl + c with focus on the terminal to terminate the script

## How it works

If installation was successful, GTAV will automatically load the DeepGTAV plugin. Once the game starts DeepGTAV will wait for TCP clients to connect on port 8000.

Clients connected to DeepGTAV are allowed to send messages to GTAV to start and configure the research environment (*Start* and *Config* messages), send driving commands to control the vehicle (*Commands* message) and to stop the environment to fallback to normal gameplay (*Stop* message).

When the environment has been started with the *Start* message, DeepGTAV will start sending the data gathered from the game back to the client in JSON format, so the client can use it to store a dataset, run it through a self-driving agent...

The data sent back to the client and intitial conditions will depend on the parameters sent by the client with the *Start* or *Config* messages. Things that can be controlled for instance are: rate of transmission, frame width and height, weather, time, type of vehicle, driving style, wether to get surrounding vehicles or peds, type of reward function and a large etc...

[VPilot](https://github.com/ai-tor/VPilot) provides a nice interface and examples written in Python to use DeepGTAV for your self-driving car research.

The following chapters describe the purpose and contents of each message.

## Messages from the client to DeepGTAV

Messages must be always be sent in two steps: First send the JSON message length in bytes and then send the message itself, this is done so DeepGTAV knows when to stop reading a message.

### Start

This is the message that needs to be sent to start DeepGTAV, any other message sent prior to this won't make any effect. Along with this message, several fields can be set to start DeepGTAV with the desired initial conditions and requested *Data* transmission. 

When this message is sent the environment starts, the game camera is set to the front center of the vehicle and *Data* starts being sent back to the client until the client is disconnected or an *Stop* message is received

Here follows an example of the *Start* message:
```json
{"start": {
  "scenario": {
    "location": [1015.6, 736.8],
    "time": [22, null],
    "weather": "RAIN",
    "vehicle": null,
    "drivingMode": [1074528293, 15.0]
  },
  "dataset": {
    "rate": 20,
    "frame": [227, 227],
    "vehicles": true,
    "peds": false,
    "trafficSigns": null,
    "direction": [1234.8, 354.3, 0],
    "reward": [15.0, 0.5],
    "throttle": true,
    "brake": true,
    "steering": true,
    "speed": null,
    "yawRate": false,
    "drivingMode": null,
    "location": null,
    "time": false    
  }
}}
```
The scenario field specifies the desired intitial conditions for the environment. If any of its fields or itself is null or invalid the relevant configuration will be randomly set.

The dataset field specifies the data we want back from the game. If any of its fields or itself is null or invalid, the relevant *Data* field will be deactivated, except for the frame rate and dimensions, which will be set to 10 Hz and 320x160 by default.

### Config

This message allows to change at any moment during DeepGTAV's execution, the initial configuration set by the *Start* message.

Here follows an example of the *Config* message (identical to the *Start* message):
```json
{"start": {
  "scenario": {
    "location": [1015.6, 736.8],
    "time": null,
    "weather": "SUNNY",
    "vehicle": "voltic",
    "drivingMode": -1
  },
  "dataset": {
    "rate": null,
    "frame": null,
    "vehicles": false,
    "peds": true,
    "trafficSigns": null,
    "direction": null,
    "reward": null,
    "throttle": null,
    "brake": false,
    "steering": false,
    "speed": true,
    "yawRate": null,
    "drivingMode": null,
    "location": null,
    "time": true   
  }
}}
```
In this case, if any field is null or invalid, the previous configuration is kept. Otherwise the configuration is overrided.

### Commands

As simple as it seems, this message can be sent at any moment during DeepGTAV's execution to control the vehicle. Note that you will only be able to control the vehicle if *drivingMode* is set to manual.

Here follows an example of the *Commands* message:
```json
{"commands": {
  "throttle": 1.0,
  "brake": 0.0,
  "steering": -0.5
}}
```

### Stop

Stops the environment and allows the user to go back to the normal gameplay. Simply disconnecting the client produces the same effect.

Here follows an example of the *Stop* message:
```json
{"stop": {}}
```
## Messages from DeepGTAV to the client

DeepGTAV will always send the messages in two steps: First it will send the message length in bytes and then it will send the message itself, so the client can know when to stop reading it.

The messages rate and content will depend on the configuration set by the *Start* or *Config* messages, and are always sent consecutively (Frame, Data).

### Frame

This is a byte array containing the RGB values of the current GTAV screen (resized to the specified width and length). Make sure the window is not minimized, otherwise the values will be all zeroes (black).

### Data

## Reporting issues and TODOs

DeepGTAV generates a useful log file named *deepgtav.log* in GTAV's installation directory. Please attach it in your issue when reporting any bug.

__TODO:__
* Improve code quality (a lot!)
* Add support for traffic signs detection
* Add support for driving mode override
* General bug fixing
* Config file
* Improved logging

Repo was originally cloned from: https://github.com/aitorzip/DeepGTAV
