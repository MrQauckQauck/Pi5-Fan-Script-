**Raspberry Pi 5 Fan Control**

A simple Python script to automatically control the built-in fan on a Raspberry Pi 5.
Installation
Copy fan_control.py to /home/pi/Scripts/
Set up the systemd service for auto-start on boot:
```
sudo tee /etc/systemd/system/fan_control.service > /dev/null << 'EOF'
[Unit]
Description=Raspberry Pi 5 Fan Control
After=network.target

[Service]
Type=simple
User=root
ExecStart=/usr/bin/python3 /home/pi/Scripts/fan_control.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF
```
**Enable and start the service:**

```
sudo systemctl daemon-reload
sudo systemctl enable fan_control
sudo systemctl start fan_control
```

Usage

The script starts automatically on system boot via systemd service.
Check status:

```
sudo systemctl status fan_control

Stop the fan:

sudo systemctl stop fan_control

Start the fan:

sudo systemctl start fan_control
```

Configuration
The script controls the Raspberry Pi 5's built-in fan via the thermal cooling device at /sys/class/thermal/cooling_device0/cur_state.
