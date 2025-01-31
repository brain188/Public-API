# Public API  

This project is a publicly accessible RESTful API built using Python and Flask. It is designed to provide basic information dynamically via a simple GET request. The API returns the following information in JSON format:

1. Email Address: A predefined email address representing the API owner.
2. Current Datetime: The current date and time dynamically generated in ISO 8601 format (in UTC timezone).
3. GitHub Repository URL: A link to the public GitHub repository containing the codebase for this project.



## SetUp Instructions

1. Clone the repository
  * git clone https://github.com/brain188/Public-API.git
  * cd public-api

2. Create a virtual environment
  * python -m venv venv
  * source venv/bin/activate  # macOS/Linux  
  * venv\Scripts\activate     # Windows

3. install Dependencies
  * pip install -r requirements.txt

4. Run the project locally
  * python app.py


## API Documentation

1. URL Endpoint : it is publicly accessible at https://public-api-qvrh.onrender.com

2. Response/Request Format :
{
    "email": "your-email@hng.com",
    "current_datetime": "2025-01-30T09:30:00Z",
    "github_url": "https://github.com/yourusername/repositoryname.git"
}

## Additional Resource

 https://hng.tech/hire/python-developers



