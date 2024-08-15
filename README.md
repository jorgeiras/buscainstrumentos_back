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
...
<div align="center">
  <img src="https://github.com/jorgeiras/buscainstrumentos_back/blob/master/images/backend_cicd.png" alt="Backend CICD">
</div>

### Docker
...

### License
...

### Contact
...

