# Compute Blade PWM Fan Control

This is a simple script to control your pwm fan on compute blade.

## Install GPIO Zero

### apt
GPIO Zero is packaged in the apt repositories of Raspberry Pi OS, Debian and Ubuntu. It is also available on [PyPI](https://pypi.org/project/gpiozero/).
```bash
sudo apt update
sudo apt install python3-gpiozero
```

### pip
If you’re using another operating system on your Raspberry Pi, you may need to use pip to install GPIO Zero instead. Install pip using [get-pip](https://pip.pypa.io/en/stable/installing/) and then type:
```bash
sudo pip3 install gpiozero
```