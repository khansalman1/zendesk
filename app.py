from flask import Flask
from flask import render_template

# Import the Zenpy Class
from zenpy import Zenpy

app = Flask(__name__)

# We gave the provided credentials for once just to keep it DRY!
creds = {
  'email' : 'msk.khan11@gmail.com',
  'password' : 'salman1234',
  'subdomain': 'muhammadkhan87'
  }
# we created routes for index page.
@app.route("/") # This Expose URL or what url is going to hit on browser.
def index():
  try: # We use try method to keep running if there is no API available.
    # Default
    zenpy_client = Zenpy(**creds)
    ticket_generator = zenpy_client.tickets()
    return render_template('index.html', tickets=ticket_generator)
  except:
    print("Sorry, API isn't currently available")

@app.route("/view/<ticketId>", methods= ['GET']) #to show that this to use only for Get Method but not for POST method
def view(ticketId):
  # Default
  zenpy_client = Zenpy(**creds)
  ticket = zenpy_client.tickets(id=ticketId)
  return render_template('view.html', ticket=ticket)

if __name__ == "__main__":
    app.run(debug=True)


