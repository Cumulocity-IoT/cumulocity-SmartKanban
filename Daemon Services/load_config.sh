#sudo systemctl stop MAC2C8Y.service
sudo cp SmartKanban.service /lib/systemd/system/SmartKanban.service
sudo systemctl daemon-reload
sudo systemctl start SmartKanban.service
