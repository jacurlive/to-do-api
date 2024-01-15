# TO-DO-API

#### A to-do-app build with django api for backend

## Requirements

- Python
- Django

## Usage without docker-compose

- Clone the repo
    ```
    git clone https://github.com/jacurlive/to-do-api.git
    ```

- Go to directory
    ```
    cd to-do-api
    ```

- Create virtualenv and activate
    ```
    python -m venv venv
    ```
    ###### windows cmd
    ```
    venv\Scrips\activate
    ```
    ###### linux terminal
    ```
    . venv\bin\activate
    ```

- Install requirements
    ```
    pip install -r requirements.txt
    ```

- Migrate
    ```
    python manage.py makemigrations && python manage.py migrate
    ```

- Run
    ```
    python manage.py runserver
    ```

## Usage with docker-compose
- Clone the repo
    ```
    git clone https://github.com/jacurlive/to-do-api.git
    ```

- Go to directory
    ```
    cd to-do-api
    ```

- Run docker-compose
    ```
    docker-compose up
    ```