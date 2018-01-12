# MRP-Consumer
A ridiculously simple Flask app to consume MRPEasy API calls and format for Google Sheets import. Uses `pipenv` and `.env` for config.

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
- run `pipenv run python MRP_Consume.py`
- you're in business

## Bonus Hint
- Use [ngrok](https://ngrok.com/) if you want to temporarily tunnel from your local machine.
- [Here's a great tutorial](https://robots.thoughtbot.com/how-to-manage-your-python-projects-with-pipenv) for pipenv.