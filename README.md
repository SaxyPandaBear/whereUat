whereUat
========

Takes logged geographical coordinates from IPs that access an HTTP file server and places markers on a map to visualize where it's coming from.

## Setup

- Backend:

    1. Install [Python 2.7.*](https://www.python.org/)
    2. Use pip to install flask and flask_cors: `pip install flask` and `pip install flask_cors`
    3. Run app.py: `python app.py`
    4. The backend runs at `localhost:5000` in your browser.

- Frontend:
	
	1. Install [Node.js which has NPM prepackaged with it](https://nodejs.org/en/) - This project uses Node.js version 9.2.0
	2. Use npm to install [Angular CLI](https://cli.angular.io/)
		- `npm install -g @angular/cli`
	3. In the root directory of the project, run `npm install` to get all of the required dependencies, and run `ng serve` to start the frontend.
	4. The frontend runs at `localhost:4200` in your browser.
