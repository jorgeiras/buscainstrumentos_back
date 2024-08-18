# Buscainstrumentos Backend

<div align="center">
  <img src="https://github.com/jorgeiras/buscainstrumentos_back/blob/master/images/buscainstrumentoslogo.png" alt="Backend Logo">
</div>

### Description
This is the backend service of the project Buscainstrumentos, implemented using Django REST Framework and hosted in digital ocean using droplet service (IaaS).
The project uses CI/CD for updating the backend service automatically after any change in the repo via github actions, Docker and Docker Compose.   

### Table of Contents
1. [Technical Stack](#technical-stack)
2. [Features](#features)
3. [Infrastructure and Hosting](#infrastructure-and-hosting)
4. [CI/CD](#cicd)
5. [Docker](#docker)
6. [Contact](#contact)


### Technical Stack

This project uses a variety of technologies and tools to build, deploy, and manage the backend service. Below is an overview of the key components of the technical stack:

- **Backend Framework**: 
  - **Django REST Framework**: Used to build the backend API, providing a powerful and flexible toolkit for creating RESTful web services in Python.

- **Programming Language**:
  - **Python**: The primary language used for the backend development, chosen for its simplicity, readability, and extensive ecosystem.

- **Database**:
  - **PostgreSQL**: A powerful, open-source relational database used to store and manage the backend data, particularly the musical instruments' information.

- **Web Server**:
  - **Nginx**: Serves as a reverse proxy, handling incoming HTTP and HTTPS requests, forwarding them to the Django application, and managing SSL/TLS certificates for secure communication.

- **Containerization**:
  - **Docker**: Used to containerize the backend application, ensuring that it runs consistently across different environments.
  - **Docker Compose**: Manages multi-container Docker applications, coordinating the different services (Django, Nginx, Certbot) required by the backend.

- **Continuous Integration/Continuous Deployment (CI/CD)**:
  - **GitHub Actions**: Automates the CI/CD pipeline, ensuring that every change to the codebase is tested, built, and deployed efficiently.

- **Cloud Platform**:
  - **DigitalOcean**: The backend service is hosted on DigitalOcean droplets (virtual private servers), providing a scalable and cost-effective cloud infrastructure.

- **SSL/TLS Management**:
  - **Certbot**: Automatically manages SSL/TLS certificates, ensuring that all communications with the backend are encrypted and secure.


### Features
The backend serves as the component that provides the the items to the front end, contributing the following functionalities:

- **RESTful API**: Provides endpoints for accessing and managing musical instruments data.
  - **GET /listInstrument**: Retrieve a list of all musical instruments.
     - **Query Parameters**:
      - `page` (integer, optional): The page number for pagination. Defaults to 1.
      - `category` (string, optional): The category of the instruments to filter by.
      - `minPrice` (string, optional): The minPrice of the instruments to filter by.
      - `maxPrice` (string, optional): The maxPrice of the instruments to filter by.
  - **GET /searchInstrument**: Search for instruments based on query parameters.
    - **Query Parameters**:
      - `name` (string, required): The name of the instrument to search for.
      - `page` (integer, optional): The page number for pagination. Defaults to 1.
      - `category` (string, optional): The category of the instruments to filter by.
      - `minPrice` (string, optional): The minPrice of the instruments to filter by.
      - `maxPrice` (string, optional): The maxPrice of the instruments to filter by.

- **Database Integration**: Connects to a PostgreSQL database where the instruments data are stored.
  - **Models**: Defines the structure of the data with Django models. For this case the Model created is Instrument, which represents the table Instrument of the database that constains all the data from the scraped instruments.  
    **Instrument Fields**:
    - `id` (`AutoField`, primary key): This is an automatically incremented primary key for the model.
    - `name` (`CharField`): This field stores the name of the instrument. It can have a maximum length of 500 characters.
    - `price` (`DecimalField`): This field stores the price of the instrument. It can handle values up to 10 digits long, including 2 decimal places. This field is optional and defaults to `None`.
    - `link` (`CharField`): This field stores a URL link to the instrument on the website. It can have a maximum length of 1000 characters and must be unique.
    - `website` (`CharField`): This field stores the name of the website where the instrument is listed. It can have a maximum length of 500 characters.
    - `image` (`CharField`): This field stores a URL to an image of the instrument. It can have a maximum length of 1000 characters and is optional with a default value of `None`.
    - `location` (`CharField`): This field stores the location of the instrument. It can have a maximum length of 500 characters and is optional with a default value of `None`.
    - `category` (`CharField`): This field stores the category of the instrument, such as "string" or "percussion". It can have a maximum length of 200 characters and is optional with a default value of `None`.
    - `expiration` (`DateField`): This field stores the expiration date of the instrument's listing. It is optional and defaults to `None`.
    - `publish` (`DateField`): This field stores the publish date of the instrument's listing. It is optional and defaults to `None`.
      



### Infrastructure and Hosting  

<br><br>  
<div align="center">
  <img src="https://github.com/jorgeiras/buscainstrumentos_back/blob/master/images/backend_db.png" alt="Backend hosting" style="margin-top: 20px; margin-bottom: 20px;">
</div>
<br><br>  
    
This diagram above represents the deployment architecture for the backend using Django REST Framework, Nginx, certbot,  Docker, and a PostgreSQL database, hosted on DigitalOcean droplets (virtual private servers).  
This setup is common for scalable, secure, and modular web applications. By separating the components into Docker containers and using droplets, it allows for easy scaling, maintenance, and security management. Each component has a specific role, contributing to a robust backend architecture.  
Here's a breakdown of the components and their interactions:

#### 1. Backend Droplet:

- **Docker Containers**:
  - **Django REST Framework**: This component is responsible for handling the backend logic of the application, particularly the API requests. It's encapsulated within a Docker container, which allows it to run in an isolated environment.
  - **Nginx**: Nginx serves as a reverse proxy server in this setup. It receives incoming requests from the frontend and forwards them to the Django REST Framework container. It is also configured to use the SSL certificate created by certbot.
  - **Certbot**: Certbot is used for managing SSL/TLS certificates, ensuring that the communication between the client and server is encrypted. This container automatically obtains and renews certificates, integrating them with Nginx.

#### 2. Database Droplet:

- **PostgreSQL Database**: This droplet hosts a PostgreSQL database. The Django REST Framework communicates with this database to store and retrieve data. Requests are sent from the backend droplet to this database droplet, and responses are sent back accordingly.

#### 3. Interaction Flow:

- **Frontend Request**: The frontend sends a request to the backend droplet. This request is received by Nginx.
- **Backend Processing**: Nginx forwards the request to the Django REST Framework container, which processes it. If the request involves data retrieval or storage, the Django application will query the PostgreSQL database.
- **Database Interaction**: The Django application sends a request to the PostgreSQL database hosted on a separate droplet, and the database processes this request and sends a response back.
- **Response to Frontend**: Once the Django application has the necessary data (or has completed the required processing), it sends the response back to Nginx, which then forwards it to the frontend.

#### 4. Security:

- **Certbot**: The Certbot container ensures that SSL certificates are properly configured and maintained, providing secure HTTPS communication between the client and the backend server.



### CI/CD

    
<div align="center">
  <img src="https://github.com/jorgeiras/buscainstrumentos_back/blob/master/images/backend_cicd.png" alt="Backend CICD" style="margin-top: 20px; margin-bottom: 20px;">
</div>

      
This diagram illustrates the CI/CD (Continuous Integration/Continuous Deployment) pipeline for deploying the project using Docker and Docker Compose on the backend droplet (a virtual server instance), hosted on DigitalOcean.  
The pipeline is divided into two main jobs, as indicated by the color coding (green for the 1st job and orange for the 2nd job). This pipeline ensures that every time new code is pushed into the repository, the application is automatically rebuilt, the latest images are pulled, and the application is redeployed on the backend server, all while maintaining a clean environment by removing outdated images.  
Here's a step-by-step explanation:

##### 1st Job (Green): Building and Pushing Docker Image

- **Developer Pushes Code to GitHub Repository**:
  - The process begins when a developer pushes new code to a GitHub repository.

- **Workflow Gets Triggered**:
  - The push event triggers a CI/CD GitHub Actions workflow.

- **Build Docker Image**:
  - The workflow builds a Docker image of the project based on the Dockerfile in the repository. This image encapsulates the application, its dependencies, and the environment configuration.

- **Push Image to Docker Hub**:
  - Once the Docker image is built, it is pushed to Docker Hub where Docker images are stored. This makes the image available for deployment on the server that can pull from Docker Hub.

##### 2nd Job (Orange): Deploying the Application

- **Connect to the Droplet via SSH**:
  - The second job in the pipeline involves connecting to the backend droplet via SSH. This is where the deployment takes place.

- **Clone the Repository**:
  - The deployment script written in the workflow clones the GitHub repository into the droplet. This step ensures that the latest version of the application code is available on the server (for files that would be needed for deployment like dockerCompose file).

- **Copy Necessary Variables into .env**:
  - The script copies environment variables into a `.env` file within the droplet. This file contains sensitive information like database credentials and other configuration settings needed by the application.

- **Docker Compose Pull**:
  - The script runs `docker compose pull` to pull the latest versions of the Docker images from Docker Hub. This ensures that the most recent image (built in the 1st job) and other service images are available on the droplet.

- **Docker Compose Up**:
  - The next step is to run `docker compose up`, which creates and starts the containers for the application and its associated services (Django REST Framework, Nginx, Certbot). This command uses the Docker images pulled in the previous step.

- **Remove Old Images**:
  - After the new containers are up and running, the script removes any old Docker images that are no longer needed. This helps free up disk space on the droplet and prevents the storage from being filled up by unnecessary files.


### Docker
The Docker setup for this project is designed to encapsulate the application, its dependencies, and the environment configurations within Docker containers. This ensures consistency across different environments (development, testing, and production) and simplifies the deployment process.  
It also makes it easy to change the hosting cloud provider if necessary.

#### Dockerfile

The `Dockerfile` defines the environment in which the Django application runs. Below is a breakdown of its contents:

- **Base Image**:
  - `FROM python:3.11`: Uses the official Python 3.11 image as the base image.

- **Environment Variables**:
  - `ENV PYTHONDONTWRITEBYTECODE 1`: Prevents Python from writing `.pyc` files to disk.
  - `ENV PYTHONUNBUFFERED 1`: Ensures that Python output is not buffered, which is helpful for logging.

- **Working Directory**:
  - `WORKDIR /app`: Sets the working directory inside the container to `/app`.

- **Installing Dependencies**:
  - `COPY requirements.txt /app/`: Copies the `requirements.txt` file to the container.
  - `RUN pip install --upgrade pip && pip install -r requirements.txt`: Installs the dependencies listed in `requirements.txt`.

- **Copying Application Code**:
  - `COPY . /app/`: Copies the current directory contents into the container at `/app/`.

- **Collect Static Files**:
  - `RUN python manage.py collectstatic --noinput`: Collects static files into the `static` directory for production use.

- **Expose Port**:
  - `EXPOSE 8000`: Makes port 8000 available to the outside world.

- **Command to Run the Application**:
  - `CMD ["gunicorn", "--workers=3", "--timeout=120", "--bind", "0.0.0.0:8000", "buscainstrumentos_back.wsgi:application"]`: Starts the application using Gunicorn with 3 worker processes and a 120-second timeout.

#### Docker Compose

The `docker-compose.yml` file orchestrates the multi-container Docker application. It defines three services: `web`, `nginx`, and `certbot`.

##### Services

1. **Web Service**:
   - **Image**: Uses the Docker image built from the `Dockerfile`.
   - **Environment Variables**: The application’s sensitive configurations, like database credentials are passed via environment variable.
   - **Command**: Runs Gunicorn to serve the Django application.
   - **Volumes**: l
     - `static_volume:/app/static`: Mounts the volume for static files.

2. **Nginx Service**:
   - **Image**: Uses the official Nginx Alpine image for lightweight, secure web serving.
   - **Ports**: 
     - `80:80`: Maps HTTP traffic to port 80.
     - `443:443`: Maps HTTPS traffic to port 443.
   - **Volumes**: 
     - `./config/nginx:/etc/nginx/conf.d/:ro`: Mounts the Nginx configuration files.
     - `static_volume:/home/djangouser/buscainstrumentos_back`: Mounts the static files directory.
     - `/home/djangouser/certbot/www/:/var/www/certbot/:ro`: Mounts the directory for Certbot web root challenges.
     - `/home/djangouser/certbot/conf/:/etc/nginx/ssl/:ro`: Mounts the directory for SSL certificates.
   - **Depends On**: 
     - `web`: Ensures that the Nginx service starts only after the web service is up.

3. **Certbot Service**:
   - **Image**: Uses the official Certbot image for SSL/TLS certificate management.
   - **Volumes**: 
     - `/home/djangouser/certbot/www/:/var/www/certbot/:rw`: Mounts the directory for Certbot web root challenges.
     - `/home/djangouser/certbot/conf/:/etc/letsencrypt/:rw`: Mounts the directory for storing and renewing SSL certificates.

##### Volumes

- **static_volume**: Used for storing the application's static files.


### Contact
...

