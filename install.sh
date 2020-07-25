#!/bin/bash

sudo cp nanosound_lirc.service /lib/systemd/system/
sudo /bin/systemctl daemon-reload
sudo /bin/systemctl enable nanosound_lirc
