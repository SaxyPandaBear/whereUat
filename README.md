whereUat
========

Takes logged geographical coordinates from IPs that access an HTTP file server and places markers on a map to visualize where it's coming from.

## Setup

- Backend and Server-side code:

    1. Install [Python 2.7.*](https://www.python.org/)
    2. Use pip to install flask and flask_cors for backend: `pip install flask` and `pip install flask_cors`
	3. Import pyipinfo for the server: `pip install pyipinfo`
		- This wrapper to the IPInfo API requires the use of `curl` so this code doesn't work on any system that 
		  doesn't have access to the `curl` command
    4. Run app.py and httpfileserver.py: `python app.py`, `python httpfileserver.py`
		- You can run either or both scripts in the background using `nohup` or `&`
		- `python app.py & python httpfileserver.py &` runs both scripts in the background
    5. The backend runs at `localhost:5000` in your browser.

- Frontend:
	
	1. Install [Node.js which has NPM prepackaged with it](https://nodejs.org/en/) - This project uses Node.js version 9.2.0
	2. Use npm to install [Angular CLI](https://cli.angular.io/)
		- `npm install -g @angular/cli`
	3. In the root directory of the project, run `npm install` to get all of the required dependencies, and run `ng serve` to start the frontend.
	4. The frontend runs at `localhost:4200` in your browser.

### Starting up the full application

```bash
python httpfileserver.py & python app.py & ng serve
```
