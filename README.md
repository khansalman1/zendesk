# zendesk

Installation Guide to install Ticket viewer app

We made the Directory in Terminal of folder name flask by mkdir command
sudo pip3 install virtualenv
mkdir flask
cd flask
virtualenv flask_app
cd flask_app
source bin/activate
pip install flask
Run server with flask_app python app.py

Structure:

Use flask as this is lightweight and easy to use.
We use MVC model in which app.py is our main file at which we defined our routes.
We have a template folder in which we have webpage structure such as Html and view file content
We used suggested python SDK Zenpy from Zendesk API to run the API.
For HTML, I used Bootstrap in order to build the Table form for Ticket.
