## Installing Botty on a Raspberry Pi Zero as a service

How to install Botty as a service on a Raspberry Pi zero so he starts up when the Raspberry Pi Zero boots 
1) Copy the botty.service file to your `/etc/systemd/system/` directory as root
2) Enable the botty.service 
3) Reboot the Raspberry Pi Zero to test

```
    sudo cp botty.service /etc/systemd/system/botty.service
    sudo systemctl enable botty.service
    sudo reboot
```