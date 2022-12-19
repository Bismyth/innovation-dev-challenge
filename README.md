# Dev Challenge

The following is a simplified version of the stack that we use on a daily bases. It is as follows:

1. Vue.js (Nuxt)
2. FastAPI (Python)
3. Sqlalchemy (Pyhton ORM)
4. SQLITE

Typically we would use docker and postgres instead of sqlite, however to ensure ease of use in this case we have removed them.

## How to Run

The project has been designed to run in Windows.

The project has already been setup and several scripts have been provided to start up the backend and frontend. To ensure you can use the project, the following dependencies will need to be installed

1. Python 3.7 and PIP or greater https://www.python.org/downloads/
2. Nodejs and NPM https://nodejs.org/en/download/

After these are installed, you should be able to run the following script to initialise the backend:

Note: to run powershell scripts you may need to run powershell as an admin and enable scripts `Set-ExecutionPolicy unrestricted`. Please read through the scripts as standard practice to ensure for yourself that they are not malicious.

1. `init_backend.ps1`

After this script runs succesfully you should not run it again.

Finally run the following scripts to start the frontend and backend services:

1. `start_backend.ps1`
2. `start_frontend.ps1`

Ensure to run the frontend script in the frontend folder and the backend script in the backend folder.

## Project Structure

The project has been divided into a frontend and a backend, each section runs indepentently and communicates via HTTP Web Requests.

### Backend

The backend is made up of several folders each holding a part of the overall backend process

#### 1. Routes

Routes holds the fastapi implementation that defines the different endpoints available from the backend. These endpoints act as entrypoints to run logic and fetch and store data. When a JSON is sent to the endpoint, the functon has a parameter matching the data. This paramter is types using the validation model for this data. If the data does not match the validation model, the backend will return error 422.

The endpoint also defines a response validation model, this is used to validate data coming out of the app and to show or hide certain fields to the response. The backend will attempt to translate the object being returned into this format and will only include the listed fields.

#### 2. Models

This folder holds the validation models used in recieving and sending data to and from the backend. The python package Pydantic is used as a base of these models. Each class is a different validation object, each property has a type assigned to allow the validators to check type, i.e. `id : int`. If the property has the following notation `id : int = None` then the value is not required but will be used if present, properties without this notation are required by default and if they are not present in the web request, error 422 will be returned by the backend.

#### 3. Schemas

This folder holds the definitions for the various database tables used by SQLAlchemy. Each table is its own class and each column is defined as a class property.

When a new table definition is created, the developer can run the following commands to have the database migration tracked and to have the table automatically added to the database, no manual SQL should be required.

The commands should be run with the python virtual enviroment active.

`alembic revision --autogenerate -m "<Comment>"` This creates the new database revision. <br>
`alembic upgrade head` This updates the database to the latest revision.

#### Summary

Examples of each of these steps are included in the project so you can understand how they are used.

### Frontend

The frontend is based in Vue.js 2 https://v2.vuejs.org/.

The frontend follows the standard nuxt structure https://nuxtjs.org/docs/get-started/directory-structure.

Vuetify, a frontend component library, has been pre-installed into the project, feel free to use any of the components available https://vuetifyjs.com/en/.

An example of a basic frontend page and component, along with backend integrations has been included in the project.

## Task

The task is to add another database table to the project and have the data come through to the frontend.

This will include:

1. Database table design
2. Validation models
3. API endpoint creation
4. Frontend component or page to display the data
5. Frontend component or page to add the data
6. Some method of deleting data from the frontend

An example of this is alread included in the project, so feel free to use that as a starting point for the new table. The table can be anything you want, however it should be something that can be shown in a list or a table and for which multiple rows can be added and it should include a numerical value that can be totaled.

As a further extension of what is already present, the new table should have the following:

1. A method for modifying an existing item
2. A summary row that totals the included numerical column

Submissions will be considered on how well they demostrate the full stack development skills.

This task would typically take one of our experienced developers no more than 30 minutes, however familiarity with the stack and technologies will be a limiting factor. We ask you to keep your effort to a time below 4 Hours as we don't want to take up too much of your time and want to provide an accurate demonstartion of your abilities.

If you are unable to complete parts of the task, but know how to do it in another language or framework, you can include code snippets or files outlining how you do it in that in that framework. We understand that you may not be familiar with the languages or packages we use so we will not consider knowledge of the packages involved to seriously.

Please feel free to email me if you have any issues getting the project started or understanding the project structure, adam.bardsley@innovation-i.com.au.
