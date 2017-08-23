# Mentored Project Week 3 Homework - Backend Intro

## Instructions

### Installing the Homework Code

1. Clone this repository to your computer with `git clone --`, and cd into the directory with `cd --`.

2. Set up a [virtual environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) with the command `python3 -m venv env`
   (Linux and Mac) or `virtualenv env` if you're on Windows.

3. Activate your virtual environment with `source env/bin/activate` (Linux and Mac) or `env\scripts\activate` (Windows). Your
   terminal's command prompt should now have a little `(env)` in front of it, so it goes from
   ```
   user@MY-COMPUTER:~$
   ```
   to
   ```
   (env) user@MY-COMPUTER:~$
   ```
   Note that from here on out we'll assume that you've activated your virtual environment - if you need to deactivate your virtual
   environment (for example, if you need to work on another project that uses Python) just type in the command `deactivate` (works on
   both Linux/Mac and Windows). You can always activate it again when you work on this code.

4. Once you've activated your virtual environment, install all of the project dependencies with the command
   ```
   pip install -r requirements.txt
   ```

### Running the Server

You'll need to run the server to see the website in action and check if your code works.

1. CD into the Django project directory with `cd bloggo`, then do `python manage.py runserver`.
2. View your website by opening up a web browser and going to `localhost:8000`.

### Submitting the Homework

Your submissions will be done through git. We'll automatically run tests against each git commit - you can see the results
of the tests by clicking on the checkmarks in your GitHub commit list. To commit and push your work to GitHub, do
`git commit -am "<YOUR COMMIT MESSAGE HERE>"` and then `git push`.

If you don't want to wait for the autograder to see if your code works, you can run the tests manually with `python manage.py test`.
