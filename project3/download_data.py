from roboflow import Roboflow

rf = Roboflow(api_key="Ba3vQgPDoUvoUmxzKGjp")
project = rf.workspace("roboflow-58fyf").project("rock-paper-scissors-sxsw")
version = project.version(11)
dataset = version.download("yolov11")
