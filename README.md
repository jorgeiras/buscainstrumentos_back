# Buscainstrumentos Backend

<div align="center">
  <img src="https://github.com/jorgeiras/buscainstrumentos_back/blob/master/images/buscainstrumentoslogo.png" alt="Backend Logo">
</div>

### Description
This is the backend service of the project Buscainstrumentos, implemented using Django REST Framework and hosted in digital ocean using droplet service (IaaS).
The project uses CI/CD for updating the backend service automatically after any change in the repo via github actions, Docker and Docker Compose.   

### Table of Contents
1. [Features](#features)
2. [Infrastructure and Hosting](#infrastructure-and-hosting)
3. [Usage](#usage)
4. [Development](#development)
5. [CI/CD](#cicd)
6. [Docker](#docker)
7. [License](#license)
8. [Contact](#contact)

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
  
<div align="center">
  <img src="https://github.com/jorgeiras/buscainstrumentos_back/blob/master/images/backend_db.png" alt="Backend hosting">
</div>
  
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


### Usage
...

### Development
...

### CI/CD
  
<div align="center">
  <img src="https://github.com/jorgeiras/buscainstrumentos_back/blob/master/images/backend_cicd.png" alt="Backend CICD">
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
...

### License
...

### Contact
...

