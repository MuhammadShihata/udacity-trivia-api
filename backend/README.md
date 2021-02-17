# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

## Database Setup

With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:

```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior.

1. Use Flask-CORS to enable cross-domain requests and set response headers.
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories.
3. Create an endpoint to handle GET requests for all available categories.
4. Create an endpoint to DELETE question using a question ID.
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score.
6. Create a POST endpoint to get questions based on category.
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question.
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions.
9. Create error handlers for all expected errors including 400, 404, 422 and 500.

REVIEW_COMMENT

```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code.
```

## Endpoints

```
GET '/categories'
GET '/questions'
POST '/questions'
DELETE '/questions'
GET '/categories/:id/questions'
POST '/quizzes'
```

#### GET '/categories'
##### Fetches a dictionary of categories

```
- Fetches a dictionary of categories, total number of categories
- Request Arguments: None
- Returns: An object with a multiple keys...
  - categories: contains an object its keys are the ids and value is corresponding string of category...
    - id: category_string key:value pairs,
  - total_categories: total_number_of_categories_integer,
  - success: success_status_boolean.
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true,
  "total_categories": 6
}
```

#### GET '/questions'
##### Fetches a list of paginated questions
```
- Fetches a list of paginated questions (10 questions per page), total number of questions, dictionanry of categories and the current category.
- Request Arguments: page, 1 by default.
- Returns: An object with multiple keys...
    - questions: contains a list of 10 questions each question is an object with multiple keys...
      - id: the_question_id_integer
      - question: the_qustion_itself_string
      - answer: the_answer_string
      - category: its_category_id_string
      - difficulty: the_difficulty_score_integer
    - total_questions: total_questions_integer,
    - categories:  contains an object its keys are the ids and value is corresponding string of category id: category_string key:value pairs,
    - current_category: current_directory_id_string,
    - success: success_status_boolean.

{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": "All",
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },...
  ],
  "success": true,
  "total_questions": 25
}

```

#### POST '/questions'
##### Create a new question

```
- Create a new question using a request body looks like this...
{
  answer: "Maya Angelou",
  category: "4",
  difficulty: 2,
  question: "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
}

- Request Arguments: None
- Returns: object of 2 keys...
  - created: created_question_id_integer,
  - success': succes_status_boolean.

  {
    "created": 26, 
    "success": true
  }

```

#### POST '/questions'
##### Searches for question(s)

```
- Searches for a substring in questions and return all questions that match paginated if more than 10 using a request body look like this...
{
  searchTerm: "title"
}
- Request Arguments: page, 1 by default.
- Returns: An object with multiple keys...
    - questions: contains a list of 10 questions max each question is an object with multiple keys...
      - id: the_question_id_integer
      - question: the_qustion_itself_string
      - answer: the_answer_string
      - category: its_category_id_string
      - difficulty: the_difficulty_score_integer
    - total_questions: total_questions_integer,
    - current_category: current_directory_id_string,
    - success: success_status_boolean.

  {
    "current_category": "All",
    "questions": [
      {
        "answer": "Maya Angelou",
        "category": "4",
        "difficulty": 2,
        "id": 5,
        "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
      },...
    ],
    "success": true,
    "total_questions": 26
  }

```

#### DELETE '/questions/:id'
##### Deletes a question using it's ID

```
- Deletes a question using it's ID...
- Request Arguments: None
- Returns: An object with multiple keys...
  - deleted: deleted_post_id_integer,
  - total_questions: total_question_after_deletion_integer,
  - success: sucess_status_string.
  
  DELETE '/questions/5'
  {
    "deleted": 5, 
    "success": true, 
    "total_questions": 25
  }
          
```          

#### GET '/categories/:id/questions'
##### Fetches a list of paginated questions of a specific category using it's ID 
```
- Fetches a list of paginated questions (10 questions per page), total number of questions, dictionanry of categories and the current category.
- Request Arguments: page, 1 by default.
- Returns: An object with multiple keys...
    - questions: contains a list of 10 questions each question is an object with multiple keys...
      - id: the_question_id_integer
      - question: the_qustion_itself_string
      - answer: the_answer_string
      - category: its_category_id_string
      - difficulty: the_difficulty_score_integer
    - total_questions: total_questions_integer,
    - current_category: current_directory_id_string,
    - success: success_status_boolean.
  GET 'categories/5/questions'
{
  "current_category": "History",
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": "4",
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },...
  ],
  "success": true,
  "total_questions": 3
}

```

#### POST '/quizzes'
##### Fetches a random question using it's category and previous asked questions
```
- Fetches a random question using a category object and a list of previous questions ids on the body request, body should look like this...
  {
    previous_questions: [], 
    quiz_category: {type: "History", id: "4"}
  }
- Request Arguments: None
- Returns: An object with 2 keys...
    - question: question object with multiple keys...
      - id: the_question_id_integer
      - question: the_qustion_itself_string
      - answer: the_answer_string
      - category: its_category_id_string
      - difficulty: the_difficulty_score_integer
    - success: success_status_boolean.

  {
    "question": {
      "answer": "Maya Angelou", 
      "category": "4", 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    "success": true
  }

```




## Testing

To run the tests, run

```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
