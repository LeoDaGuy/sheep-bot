from flask import Flask
from threading import Thread

app = Flask('')
@app.route('/')
def main():
  return '<script>window.open("https://discord.com/api/oauth2/authorize?client_id=838291893078720573&permissions=0&scope=bot", "_self")</script>'
def run():
  app.run(host="0.0.0.0", port=8080)
def keep_alive():
  server = Thread(target=run)
  server.start()