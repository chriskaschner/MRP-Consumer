# MRP-Consumer
A ridiculously simple Flask app to consume MRPEasy API calls and format for Google Sheets import. Uses `.env` for config and `pipenv`

## Install
- Clone repo
- Create a .env file file with the following lines

``` 
    API_KEY=YOUR_KEY
    ACCESS_KEY=YOUR_KEY
    BASE_URI=YOUR_BASE_URI
```
- navigate to project directory
- run `pipenv install`
    - install pipenv if you haven't already
- you're in business