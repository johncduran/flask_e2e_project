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
I was able to deploy my app using the following docker command:

__docker-compose up --build__
With this command I was able to create a docker instance. I used this command to tell docker what port to host the app on which was 8080. The 8005 is the port that I will be hosting docker on. Therefore, if I try to access the app through the 8080 port it won't work, only if I switch to 8005 locally will it work. 

I initally did take a different route of deploying my app using regular docker, however I ran into a multitude of issues. Therefore, in the end I decided to use docker-compose. I explain further my process of using regular docker in the section below talking about errors.

##### -Docker Errors
I did run into an error when I first tried to create the docker image and it said that it failed to load in the requirements.txt file. I was able to fix this issue once I got rid of the 'mysqlclient' line in the requirements.txt file. 

Another error I ran into was trying to deploy using just docker. Each time I kept running the following command it just wouldn't want to deploy 'docker run -d -p 8005:8080 final'. It was saying that it couldn't find the modules authlib and so I figured out that I needed to put that into my requirements.txt file. However, after this I still wasn't able to run it and this time there was no clear error message to guide me.
![Unsuccessful deployment](screenshots/unsuccessful%20deployment.png)


To solve this I used docker-compose to try and get around deploying the app. I was able to create the docker instance this way. However, I still ran into the issue of it not deploying due to it not finding the requests module. I did a pip install of the module, but it was already satisfied according to the terminal. I changed the ports to make sure if that was the issue, but still it didn't seem to fix things. 
![Successful docker-compose up --build](screenshots/Successful%20docker-compose%20up%20--build.png)
![Requests module error](screenshots/requests%20module%20error.png)

After almost giving up on this I thought back to before on how it couldn't find the authlib module and so assumed that I needed to do the same with requests. And so I added requests to the requirements.txt file and that actually did fix the issue. Now it is running using 'docker run -p 8005:8080 flask_e2e_project_flask-app' 
![Successful docker run](screenshots/Successful%20docker%20run.png)

#### On the cloud

To deploy this app on the cloud I used Azure App Services to get the job done. 

## __.env template__

For the .env file, I made sure to include the variables that I needed in my Python code that would allow me to connect to my database and API keys. Within my .env file, I put in my
DB_URL and SQLALCHEMY_DATABASE_URI to allow me to have a connection from my flask application to my database hosted on Google's Cloud Platform. The reason I chose to go with Google to host the MySQL database was because I was running into connection issues on the Azure platform and so I ran into fewer ones with Google.


I also ensured that my .env file would not be pushed to my GitHub repository by adding it to my _.gitignore_ file. That way it keeps my username and password of my database secure and hidden.


My Python app then uses the dotenv package to load in the .env values using the code
"load_dotenv()". After that, I use the os package to pull the specific value I want to use and create a variable from that using the code "os.getenv("SQLALCHEMY_DATABASE_URI")". This allowed me to use my important login credentials all over my app without risking its security.


## __Database setup__

For the database as mentioned before I orignally used Azure to create a flexible MySQL server, however I ran into many connectivity issues when trying to run it and so decided to go with Google's services instead. To connect to the database I originally was using the SQLAlchemy package along with its fucntions like declarative base and engine. With this path I found that it was difficult to try and integrate it with my flask app as I was able to see in the terminal that I had created a new database called 'john' and a table called 'FitnessEntries'. However, I coudln't find an easy way to connect it to the flask app. 
![Database Tables](screenshots/Database%20tables.png)
![Database Names](screenshots/Database%20names.png)
After a lot of trial and error I was decided to go for a different route and used the flask_sqlalchemy package instead. This compared to the regular sqlalchemy package is built to be a more concise and an easy to use way to connnect a database to a flask app. I found out that I didn't need to create an engine like I did before using the code 

"engine = create_engine(SQLALCHEMY_DATABASE_URI,
                         connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         ) "   

Instead the code "app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("SQLALCHEMY_DATABASE_URI")" does this for me in the background. It was much easier creating an instance this way. 

As for structuring my repository to make the database I kept my _app.py_ file contianing only the flask portions of the app. While the db_shema.py file had the database schema layed out in it. I then allowed my _app.py_ file to import variables from the _db_schema.py_ file by making that file be percieved as a package using "from db_schema import db, FitnessEntry". 

## __Oauth__

When users first get into the fitness website they are greated with a login menu. I was able to get my app to be given persmission to use Google's API service for authentification. Once a user is logged in they will then be redirected to the fitness app's homepage. 
![Sign In](screenshots/Sign%20in.png)
I first set up the Oauth credentials and was able to get the Client ID and Secret from there. I added my local host and my azure website to be supported to use the google service. 
![Google Secret Setup](screenshots/Google%20Secret%20Setup.png)
