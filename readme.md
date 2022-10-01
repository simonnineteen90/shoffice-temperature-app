#### Starting the app
docker build . --tag "shoffice-temperature-app"
docker run -d -p 5001:5000 shoffice-temperature-app