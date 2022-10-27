## Starting the app
Setup a venv first with python3 -m venv venv  
then install requirements with pip3 install -r requirements.txt

#### Docker
docker build . --tag "shoffice-temperature-app"  
docker run -d -p 5001:5000 shoffice-temperature-app

#### Alternative
python3 app.py

#### Viewing from raspberry pi
Webpage will be available to other devices on same local network as the raspberry pi's IP address.