# URL_Shortener(API)

The project aims to provide simple GET and POST request for Shortening any long URL.

The source code is writted in ✨MVC✨ pattern. Following tools are used to build the project.

-  Python
-  Flask
-  Docker Compose
-  flask_restx
-  MySQL

> The Url Shortener algorithm used in the project is a Base62 Conversion Algorithm that act as the core engine to provide short url and reverse engineering the url to get the actual url.

### Build Instruction:
- create .env.dev file
- see the .env-example file to get a glimpse of environment configuration
- copy the parameter from the example file to .env.dev file
- put the config values as your need
- In "MYSQL_HOST" parameter provide docker container name as the value
- Now from the terminal/cmd run: docker compose up

The project will be up and running
