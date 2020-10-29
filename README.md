# Facebook Organisation Scraper


### Prerequities 

- Selenium Chrome Driver[Here](https://chromedriver.chromium.org/downloads)


### Clone the Repository

```bash
git clone https://github.com/aosborne17/Facebook-Marketplace-Script.git
```

### Create and Activate Virtual Environment

```python
pip install virtualenv
virtualenv venv
venv\Scripts\activate
```

### Install the requirements

```python
pip install -r requirements.txt
```

### Adding Login Credentials

- In the secrets.py file, add in the email and password for the facebook account you wish to login with
- These will be automatically passed in to the script as arguements

 

### Running the Application

```python
python main.py
```

### Future Additions

- Append the organisations to one CSV as opposed to having one per organisation
- Add additional rows for the number of shares