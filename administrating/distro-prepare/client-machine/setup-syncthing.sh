#!/bin/bash

echo "noway" | sudo -S systemctl enable syncthing@pioner.service
echo "noway" | sudo -S systemctl start syncthing@pioner.service
