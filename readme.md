# Final Fitness Tracking Website
Link: https://fitness-tracker.azurewebsites.net/

### __Intro__

For this final, I created a fitness tracking website that allows a user to keep track of various variables that they might be interested in such as their weight, blood pressure, workout routine, and more. On this website, I will have it display the data using a table to keep track of the data in one place for the user using a dedicated endpoint.


I used a variety of technologies in order to create this service. In terms of coding, I used Python, HTML, and CSS. The Python libraries used were Flask, SQLAlchemy, gunicorn and python-dotenv. These can all be found in the requirements.txt file which was necessary to have in order to launch the app on the cloud. In terms of cloud technologies, I used Google Shell Editor, Azure, and Google Cloud Platform (GCP). I used Google Shell Editor for all of the coding involved in this project. Azure was used to support and run the Flask app by using App Services. GCP was used to run and support the MySQL database to store the user's responses.


### __Steps for deployment__

#### Locally without Docker
To run this application locally all you would need is the following.
1. Download the GitHub repository containing all the files to run this app. This can be run in any IDE of your choice whether that be Google Cloud Editor, VS Code, or others. The repository can also be cloned into those IDEs as well if that is easier. For cloning all you need to do is go into the GitHub repository and copy the link provided in the code dropdown menu.![Repository Cloning](screenshots/Repository%20Cloning%20.png)
Once the repository has been cloned, you can use the command 'git clone https://github.com/johncduran/flask_e2e_project.git'. 
2. Once in the IDE and the repo copied you would type into the terminal 'python app.py' This will then run the app locally on two different IPs. The terminal should say the following with slight variations:

* Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:8080
 * Running on http://10.88.0.3:8080
![Local Deployment No Docker](screenshots/Local%20Deployment%20No%20Docker.png)
 
You would then choose either link that will then launch the app in a new tab.

3. Once there you can use the URL to go through the different endpoints that are set up in the app.py file.

![URL Endpoint Demonstration](screenshots/URL%20Endpoint%20Demonstration.png)

#### Locally with Docker

#### On the cloud

## __.env template__

For the .env file, I made sure to include the variables that I needed in my Python code that would allow me to connect to my database and API keys. Within my .env file, I put in my
DB_URL and SQLALCHEMY_DATABASE_URI to allow me to have a connection from my flask application to my database hosted on Google's Cloud Platform. The reason I chose to go with Google to host the MySQL database was because I was running into connection issues on the Azure platform and so I ran into fewer ones with Google.


I also ensured that my .env file would not be pushed to my GitHub repository by adding it to my _.gitignore_ file. That way it keeps my username and password of my database secure and hidden.


My Python app then uses the dotenv package to load in the .env values using the code
"load_dotenv()". After that, I use the os package to pull the specific value I want to use and create a variable from that using the code "os.getenv("SQLALCHEMY_DATABASE_URI")". This allowed me to use my important login credentials all over my app without risking its security.


## Database setup

For the database as mentioned before I orignally used Azure to create a flexible MySQL server, however I ran into many connectivity issues when trying to run it and so decided to go with Google's services instead. To connect to the database I originally was using the SQLAlchemy package along with its fucntions like declarative base and engine. With this path I found that it was difficult to try and integrate it with my flask app as I was able to see in the terminal that I had created a new database called 'john' and a table called 'FitnessEntries'. However, I coudln't find an easy way to connect it to the flask app. 
![Database Tables](screenshots/Database%20tables.png)
![Database Names](screenshots/Database%20names.png)
After a lot of trial and error I was decided to go for a different route and used the flask_sqlalchemy package instead. This compared to the regular sqlalchemy package is built to be a more concise and an easy to use way to connnect a database to a flask app. I found out that I didn't need to create an engine like I did before using the code 

"engine = create_engine(SQLALCHEMY_DATABASE_URI,
                         connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         ) "   

Instead the code "app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")" does this for me in the background. It was much easier creating an instance this way. 

As for structuring my repository to make the database I kept my _app.py_ file contianing only the flask portions of the app. While the db_shema.py file had the database schema layed out in it. I then allowed my _app.py_ file to import variables from the _db_schema.py_ file by making that file be percieved as a package using "from db_schema import db, FitnessEntry". 

