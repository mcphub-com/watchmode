markdown
# Watchmode MCP Server

## Overview

Watchmode MCP Server is a powerful tool designed to provide comprehensive data on the availability of movies and TV shows across various OTT streaming services. It indexes all major and many smaller streaming services, rental services, free video apps, and TV channel apps to deliver accurate and up-to-date information on where content can be streamed. This service is ideal for developers looking to integrate streaming availability data into their applications seamlessly.

### Key Features

- **Universal Streaming Availability**: Access data from over 200 streaming services, including major platforms like Netflix, Amazon Prime Video, HBO Max, Hulu, Disney+, and more. Additionally, it covers free streaming sources and TV channel apps.

- **Global Coverage**: Filter streaming sources by country to discover what's available to watch in regions such as the USA, Canada, Great Britain, Australia, and Brazil.

- **Simple REST API**: The service is built around a RESTful architecture, ensuring easy integration and interaction with your applications. All data is exchanged in JSON format over SSL for security and reliability.

- **Lightning Fast and Accurate**: Designed for speed, Watchmode ensures quick retrieval of streaming sources for titles. It offers high accuracy, avoiding gaps or incorrect data, and includes episode-level links and deeplinks for comprehensive coverage.

- **Comprehensive Data**: The server offers universal title and person IDs, ensuring no collisions. You can retrieve Watchmode IDs for titles and people, and map them to external IDs like IMDB or TMDB.

### Tools and Functionalities

Watchmode MCP Server provides an array of tools to manage and access streaming data efficiently:

- **List Titles**: Retrieve a list of titles that match specific parameters such as genres, types, and regions. This tool allows for complex queries, enabling searches like "Horror Movies Streaming on Netflix in the USA."

- **Person Details**: Access detailed information about specific individuals, including actors and directors.

- **Search**: Perform searches using external IDs or names to find titles or people, returning results with Watchmode IDs.

- **Autocomplete Search**: Build an autocomplete feature for titles and/or people, returning results with image URLs for titles and headshots for people.

- **Streaming Release Dates**: Get information on recent or upcoming releases on major streaming services, including whether a title is an original on that service.

- **New Titles and Changes (Premium Only)**: Track new titles added to Watchmode, or changes in streaming sources, episodes, or title details within specified date ranges.

- **Configuration**: Access mappings of genre names and IDs, lists of supported streaming sources, networks, and regions.

With these tools, Watchmode MCP Server provides a robust solution for managing and integrating streaming availability data into various applications, enhancing the user experience by providing comprehensive streaming information.