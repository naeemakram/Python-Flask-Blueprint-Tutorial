# Flask Blueprint Tutorial

Using Blueprint to structure a Flask website is a cool idea.
But it is also a useful idea for bigger sites. 
There's a tutorial about Flask Blueprint in Flask docs, which is pretty useless. 
I had a hard time grasping the subject and putting it to use. 
Now that I've got a hang of it, I will document things here to help others. 

Today I added separate routes for the main site and blog pages.
I learned that we can keep routes separate for the main application and the blog site, which is a requirement for most modern public-facing websites. 
The blog page blueprint is registered with the main site blueprint, the main site blueprint is registered with the app.
By doing this we overcome the need always to update the main.py with new routes. 

Learned how to put blueprints in separate folders.

Here's how to run the app properly:
```
flask --app main run
```

A command showing how to run a Flask application with Gunicorn
```
gunicorn -w 4 'main:create_app()'
```
