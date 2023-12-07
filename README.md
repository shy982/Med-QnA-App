# Med-QnA-App

Cross-Platform seamless chat application that performs CDQA + RAG tailored towards Medical Q&amp;A, Carried out as part
of MED 277, UCSD Fall '23

# Overview

## Setup:

1. Have ``git`` installed on your system. In a terminal navigate to a directory to save this project.
2. Do ``git clone git@github.com:shy982/Med-QnA-App.git``.
3. Do ``cd ./Med-QnA-App`` to enter root directory of project.

## Requirements:

1. Running the app on your machine (No dev): Have Docker installed on your Mac/PC: The application is now containerized
   in a docker environment and the deployment file is added in the source directory under `docker-compose.yml`.

2. Developing/testing purposes: If you want to have a development environment you'll need to
   install ``npm``, ``node``, ``Python 3.6+`` and follow the README's of the respective
   directories. ``src/main/marshaller`` has the backend code. ``src/main/ui/web/medi-mate`` has the frontend.

## Running the application:

To run the application (Production build deployment for demo purpose only, not a dev environment):

1. Navigate to the project root directory in your terminal.
2. Run ``docker-compose up``.
3. Wait a while for frontend and backend containers to spawn.
4. Go to http://localhost:3000/ to start chatting

# Notes:

1. Raise PR for Code updates (Anything to src directory)
2. Push to main directly for MOM, References, Presentations, etc
3. Read env.example to create .env for API tokens
4. Mark TODO's as issues