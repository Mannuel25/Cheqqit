<div align="center">
<img src="static/images/img.png" alt="Picture" style="display: block; margin: 0 auto"/>
</div>

<div align="center">
<h1>Cheqqit</h1>
<p style="font-size:15px;">Cheqqit is a beautiful and easy-to-use online tool that helps you keep track of your tasks.</p>
</div>

# Preview 

![Image](homepage_screenshot.jpg)

Click on this [link](https://cheqqit.herokuapp.com/) to view Cheqqit.

# Guidelines on how to run locally

## Clone this repository

```
git clone https://github.com/Mannuel25/Cheqqit.git
```

## Change directory
Change your directory to where you cloned the repository

```
cd Cheqqit
```

## Create a virtual environment in the cheqqit directory
Ensure you are in the cheqqit directory, run this command to create a virtual environment:
```
python -m venv .\venv
```
## Activate the virtual environment
Activate the virtual environment using the following command: 
```
venv\scripts\activate
```
Note: Upon running the command **venv\scripts\activate**, if this error shows up:
```
venv\scripts\activate : File C:\Users\Training\Documents\New folder\venv\scripts\Activate.ps1 cannot be loaded because running scripts is 
disabled on this system. For more information, see about_Execution_Policies at http://go.microsoft.com/fwlink/?LinkID=135170.
```
Run this command: 
``` 
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted 
```
Then run the command to activate the virtual environment
## Install all necessary packages 

```
pip install -r requirements.txt
```
## Update the database 
Copy this snippet and replace it with the database configuration settings, or if you are familiar with Postgres, create a new database and connect it to the app.

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
## Generate a new secret key
Make use of [Djecrety](https://djecrety.ir/) to generate your secret key.

## Make migrations
Run the following commands separately to make migrations
```
python manage.py makemigrations
python manage.py migrate
```
## Create a new superuser
Run the following command to create a new superuser
```
python manage.py createsuperuser
```
## Update debug settings in the project folder

```
if os.environ.get('DEBUG')=='TRUE':
    DEBUG = True
elif os.environ.get('DEBUG') =='False':
    DEBUG = False
```
Comment out the above snippet and add this below it   **DEBUG = True**

## Run the project

```
python manage.py runserver
```
