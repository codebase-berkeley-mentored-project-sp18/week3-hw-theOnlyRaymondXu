# Mentored Project Week 3 Homework - Backend Intro

## Instructions

### Installing the Homework Code

1. Clone this repository to your computer and cd into the directory created.

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
```
git commit -am "<YOUR COMMIT MESSAGE HERE>"
```
and then
```
git push
```

If you don't want to wait for the autograder to see if your code works, you can run the tests manually with `python manage.py test`.

## Homework Questions

For this homework, we'll be building a blogging engine called "bloggo". The basic parts of the blog engine are already made
(you can view the blog as is by running the server and going to `localhost:8000/posts`),
but our client wants us to add some more features.

### Question 1 - Static Pages and Templates

The first thing our client wants is an about page for their blog. Specifically, they want to be able to go to the URL
 `localhost:8000/posts/about` and view an about page, which should contain the following text:

> Bloggo is the best blog engine ever and it's gonna make me fifty trillion dollars!

The first thing you'll need to do is add the URL to the list of URLs in `bloggo/posts/urls.py`, because it doesn't exist yet.
A Django URL object looks like this:
```python
url(r'^the_url_for_the_view$', views.the_view_function, name="the_view_name")
```

The view functions are defined as regular functions right in `bloggo/posts/views.py`. For instance, for a function defined as `index`
 in views.py, you would put `views.index` as the view function in the URL object. Our client's code already has a (incomplete)
 view function for the about page, so you should use that.

The client also wants the about page to look nice, so use the existing template for it in `bloggo/posts/templates/posts/about.html`.
Right now the template is incomplete - you should make it extend the base template and add in the text from above that the client wants
the about page to show.

### Question 2 - Dynamic Views and Routes

