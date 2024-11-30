#Flask Blueprint Tutorial

Using Blueprint for structuring Flask websites is a cool idea.
But it is also a very useful idea for bigger sites. 
There's a tutorial about Flask Blueprint in Flask docs and it is pretty useless. 
I had a hard time grasping the subject and putting it to use. 
Now that I've got a hang of it, I will document things here to help others. 

Today I added separate routes for main site and blog pages.
I learned that we can keep routes separate for main applicaiton and the blog site which is a requirement for most modern public facing websites. 
The blog pages blueprint is registered with the main site blueprint, the main site blueprint is registered with the app.
By doing this we overcome the need to always update the main.py with new routes. 
