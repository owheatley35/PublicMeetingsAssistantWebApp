# Welcome to Meetings Assistant!
This package is a Flask Web Application to help manage Meetings. Meetings assistant handles the management of your administrative meeting work so you can focus on the outcome of the meeting.

## Tech Stack:
### Frontend:
The frontend is built through the React Framework in Typescript. It contains all UI and calls to the backend API.
The frontend is served through the base endpoint of the backend '/'. All routing is managed in the front end by the React Router Library. 

Login is managed through Auth0, a 3rd party authentication and authorisation service.

### Backend:
The backend is a Flask python app. It consists of many endpoints being utilised as APIs.

Data moving through the backend is stored in a MySQL database hosed via AWS' RDS. 

# DEVELOPMENT GETTING STARTED
To start the application you first need to install all npm dependencies and build the frontend locally to compile the React. You can do this by running the following command in the '/ui' directory. 

    npm install && npm run build

The build command needs to be repeated each time a change is made in the '/ui' directory unless it's a style change.

Then you need to install python dependencies using the following command in the root directory:

    pip install -r requirements.txt

Finally, you can run the main app locally on a server using the PyCharm Professional Flask app configuration.  