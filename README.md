# raspberry-cam-system



:Author: Olivier Friard

The **Raspberry Cam System** is a framework for capturing images, running time-lapses, and starting or stopping video recordings during experiments using Raspberry Pi devices.


A desktop Raspberry Pi Coordinator GUI connects over TCP/IP to multiple Pis, allowing users to capture images, run time-lapses, control video recording or streaming, and download media archives.

Each Raspberry Pi runs a lightweight worker service built with Flask. The worker exposes status and camera control endpoints, executes rpicam-* commands, and manages scheduled captures as well as local media storage.

Requirements:

* One Raspberry Pi with a compatible camera module installed
* A laptop or desktop computer to run the Coordinator GUI

(The Coordinator can also run on another Raspberry Pi instead of a laptop or desktop.)
