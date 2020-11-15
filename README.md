### Messages API 


**Base URL**: https://floating-fjord-14244.herokuapp.com/

## Available URLS:
- /admin/ - admin site where you can manage users and their permission. If you want credentials ask app author about it. 


## API DOCS

**Note that there should be always slash sign / at the end of each path**

- GET `/api/messages/`  - get list of all objects.

    
    Valid response code: 200 OK

Try it by command:

    curl -XGET -H 'Authorization: Token 83a5c23faf63baa2f41fa6083fd038681dadb488' -H "Content-type: application/json" 'https://floating-fjord-14244.herokuapp.com/api/messages/'`


- GET `/api/messages/<id>/`  - get only one object with given  \<id> - each request should increment `views_count` field value.


    Valid response code: 200 OK

Try it by command:

    curl -XGET -H 'Authorization: Token 83a5c23faf63baa2f41fa6083fd038681dadb488' -H "Content-type: application/json" 'https://floating-fjord-14244.herokuapp.com/api/messages/4/'`
 
- POST `/api/messages/`  - create new object. you have to provide `content` attribute so your request data can be:

    ```
    {
        "content": "Content of the message"
    }
    ```


    Valid response code: 201 CREATED
    
Try it by command:

    curl -XPOST -H 'Authorization: Token 83a5c23faf63baa2f41fa6083fd038681dadb488' -H "Content-type: application/json" -d '{
	"content": "Message created by CURL "}' 'https://floating-fjord-14244.herokuapp.com/api/messages/'
        

- PATCH `/api/messages/<id>/` - update some object with given \<id> and provide data to be updated

```
{
	"content": "New data "
}
```

    Valid response code: 200 OK
    
Try it by command:

    curl -XPATCH -H 'Authorization: Token 83a5c23faf63baa2f41fa6083fd038681dadb488' -H "Content-type: application/json" -d '{
    "content": "Message created by CURL UPDATE"
    }' 'https://floating-fjord-14244.herokuapp.com/api/messages/5/'


- DELETE `/api/messages/<id>/` - delete some object with given \<id>

    
    Valid response code: 204 No content 
 
Try it by command:

    curl -XDELETE -H 'Authorization: Token 83a5c23faf63baa2f41fa6083fd038681dadb488' -H "Content-type: application/json" -d '{
        "content": "Message created by CURL "
    }' 'https://floating-fjord-14244.herokuapp.com/api/messages/5/'
    
 
So final URLs are:
- https://floating-fjord-14244.herokuapp.com/admin/
- https://floating-fjord-14244.herokuapp.com/api/
- https://floating-fjord-14244.herokuapp.com/api/messages/
- https://floating-fjord-14244.herokuapp.com/api/messages/5/


## Deploy instructions

### Before everything clone repository to local machine:

1. Run command `git clone https://github.com/rafald121/messages`

2. Entry cloned repository by command: `cd messages`

3. Create virtualenv by command: `python3 -m venv ./.venv`

4. Install requirements by command `pip install -r requirements.txt`


### Then you can deploy it to Heroku 

1   Create `Procfile` if it not exist yet and put the content: 
```
release: python manage.py migrate
web: gunicorn settings.wsgi
```

2 Add the following import statement to the top of settings.py if it is not visible yet:
`import django_heroku`

3 Then add the following to the bottom of settings.py if it is not visilble yet:
`django_heroku.settings(locals())`

4 Run command `heroku create` in application directory

5 after displaying remotes  run command from next step
```
git remote -v
heroku  https://git.heroku.com/thawing-inlet-61413.git (fetch)
heroku  https://git.heroku.com/thawing-inlet-61413.git (push)
```

6 Run command `heroku git:remote -a thawing-inlet-61413`

7 Push changes from repository by command: `git push heroku master`



 

