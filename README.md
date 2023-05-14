# Welcome to the Quizes-Django

***

## Description

Quizes-Django is an application that allows users to create and participate in timed quizzes. The application should have a RESTful API that provides functionalities for creating and retrieving quizzes

***

## Prerequisites

One has to install python version 3.9.7 and above

One must have mongodb database

### Other Libraries
* asgiref==3.6.0
* Django==4.1.9
* django-cors-headers==4.0.0
* djangorestframework==3.14.0
* djongo==1.3.6
* pymongo==3.12.1
* pytz==2023.3
* sqlparse==0.2.4
* tzdata==2023.3

***

## Installation

After cloning application go to Quiz folder and run command `python manage.py runserver` to start app

Mongo Server must be running

***

## APIs


### API endpoint if you wanna use https://quizes-django.vercel.app/

### _POST /quizzes_ - to create a new quiz

The body of this APIs must be like:

`{
    "question": "What is 3+1",
    "options": [0,1,4,3],
    "rightAnswer":2,
    "startDate":"2023-05-14",
    "endDate":"2023-05-15"
}`

The response will be like:

`{"question":"What is 5+1","options":[0,1,6,3],"rightAnswer":2,"startDate":"2023-05-14T00:00:00Z","endDate":"2023-05-15T00:00:00Z"}`

### _GET /quizzes/active_ - to retrieve the active quiz (the quiz that is currently within its start and end time)

The response will be like:

`{"_id":{"$oid":"*****************"},"id":2,"question":"What is 3+1","options":"[0, 1, 4, 3]","rightAnswer":2,"startDate":{"$date":1684022400000},"endDate":{"$date":1684108800000},"status":"active"}`

### _GET /quizzes/:id_- to retrieve a quiz by its ID

The response will be like:

if id found 

`{"id":2,"question":"What is 3+1","options":"[0, 1, 4, 3]","rightAnswer":2,"startDate":"2023-05-14T00:00:00","endDate":"2023-05-15T00:00:00","status":"active"}`

else

`{"result":"something went wrong check id again"}`

### _GET /quizzes/:id/result_ - to retrieve the result of a quiz by its ID

The response will be like:

if id found 

`{"id":2,"question":"What is 3+1","options":"[0, 1, 4, 3]","rightAnswer":2,"startDate":"2023-05-14T00:00:00","endDate":"2023-05-15T00:00:00","status":"active"}`

else

`{"result":"something went wrong check id again"}`

### _GET /quizzes/all_ - to retrieve the all quizes

The response will be like:

`{"ans":[{"_id":{"$oid":"***********"},"id":1,"question":"What is 1+1","options":"[0, 1, 2, 3]","rightAnswer":2,"startDate":{"$date":1684022400000},"endDate":{"$date":1684108800000},"status":null},{"_id":{"$oid":"**********"},"id":2,"question":"What is 3+1","options":"[0, 1, 4, 3]","rightAnswer":2,"startDate":{"$date":1684022400000},"endDate":{"$date":1684108800000},"status":"active"},{"_id":{"$oid":"**********"},"id":3,"question":"What is 5+1","options":"[0, 1, 6, 3]","rightAnswer":2,"startDate":{"$date":1684022400000},"endDate":{"$date":1684108800000},"status":null}]}`

### _GET /check_ - check status of quiz

The response will be like:

`{{"changes":[{"_id":{"$oid":"6460d821d602f2e473fbcb42"},"id":1,"question":"What is 5+1","options":[0,1,6,3],"rightAnswer":2,"startDate":{"$date":1684022400000},"endDate":{"$date":1684108800000},"status":null},{"_id":{"$oid":"6460e41d5fa77aeb3500bb9c"},"id":2,"question":"What is 7+1","options":[0,1,6,8],"rightAnswer":3,"startDate":{"$date":1684195200000},"endDate":{"$date":1684281600000},"status":null}]}`

Anyone can use cron job to check status daily



