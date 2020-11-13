# SpaceX Preternship Project for Ryan Green
## Created by Gavin Uhran, Mike Prieto, & Tom Henry

The application is currently running on a Heroku server and can be accessed at [https://vendor-analysis-app.herokuapp.com/](https://vendor-analysis-app.herokuapp.com/)

### Disclaimer
This project is not for the company SpaceX, but for a specific employee and University of Notre Dame alum whom we are partnering with.
### Description
This repository will host our code as we develop a data visualization GUI for Ryan Green, a buyer/seller at SpaceX.

### Future Improvement
This application is currently under development and the README will be updated when development is complete.

### Running the Dashboard in development
To run the application, you simply need to use the virtual environment that we have provided in this GitHub repository. In the main directory of the app, you should run in the command line:

    $ source venv/bin/activate
    $ python src/app.py

and then access the application at [http://127.0.0.1:8050/](http://127.0.0.1:8050/) in your browser.

To run this program without the virtual environment, you must install the following libraries using `pip`:

    $ pip install Flask dash==1.17.0 pandas plotly

And then you can run the app from the main directory of the app with:

    $ python src/app.py

### Instructions for pushing to Heroku
In order to push to Heroku, you must do first login to Heroku on the command line if you have not already:

    $ heroku login

Then you must add the Heroku URL as a remote repository:

    $ git remote add heroku https://git.heroku.com/vendor-analysis-app.git

You can then push to the application using:

    $ git push heroku master
