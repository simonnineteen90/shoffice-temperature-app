from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    def get_temperature():
        with open('temperature.txt') as file:
            content = file.readlines()
            return content
    temperature = get_temperature()
    return f'<h1>Shoffice Temperature App {temperature}</h1>'


if __name__ == "__main__":
    app.run(debug=True)