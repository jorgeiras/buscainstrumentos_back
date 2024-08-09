# Buscainstrumentos Backend

![Backend Logo](path/to/logo.png)

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
7. [Contributing](#contributing)
8. [License](#license)
9. [Contact](#contact)

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
...

### Usage
...

### Development
...

### CI/CD
...

### Docker
...

### Contributing
...

### License
...

### Contact
...

![Backend Features](path/to/features.png)
