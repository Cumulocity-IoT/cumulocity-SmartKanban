#sudo systemctl stop MAC2C8Y.service
sudo cp MAC2C8Y.service /lib/systemd/system/MAC2C8Y.service
sudo systemctl daemon-reload
sudo systemctl start MAC2C8Y.service
