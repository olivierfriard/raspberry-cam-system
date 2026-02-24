# raspberry-cam-system

A desktop “Raspberry Pi coordinator” GUI connects over TCP/IP to multiple Pis to take pictures, run time‑lapses, start/stop video recording/streaming, and download archives. Each Pi runs a lightweight “worker” Flask service that exposes status and camera endpoints, executes rpicam-* commands, and manages scheduled captures and media storage.

