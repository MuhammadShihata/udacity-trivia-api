import os
from re import search
from flask import Flask, json, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category
from helpers import paginate


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    # Set up CORS. Allow '*' for origins.
    # CORS(app, resources={r'*/api/*': {'origins': '*'}})
    CORS(app)

    @app.after_request
    def after_request(response):
        '''Sets Access-Control-Allow.'''
        response.headers.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, DELETE, OPTIONS')
        return response

    @app.route('/categories')
    def retrieve_categories():
        '''
        Handles GET requests for all available categories.
        Returns a list of categories, number of categories.
        '''
        categories = Category.query.order_by(Category.id).all()
        formatted_categories = {
            category.id: category.type for category in categories
        }

        return jsonify({
            'success': True,
            'categories': formatted_categories,
            'total_categories': len(categories)
        })

    @app.route('/questions')
    def retrieve_questions():
        '''
        Handles GET requests for questions,
        including pagination (every 10 questions).
        Returns a list of questions, number of total questions,
        current category, categories.
        '''
        questions = Question.query.all()
        page = request.args.get('page', 1, type=int)
        page_questions = paginate(page, questions)

        if len(page_questions) == 0:
            abort(404)

        categories = Category.query.order_by(Category.id).all()
        formatted_categories = {
            category.id: category.type for category in categories
        }

        return jsonify({
            'success': True,
            'questions': page_questions,
            'total_questions': len(questions),
            'categories': formatted_categories,
            'current_category': 'All'
        })

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        '''Handels DELETE question using a question ID.'''
        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()

            return jsonify({
                'success': True,
                'deleted': question.id,
                'total_questions': Question.query.count()
            })

        except:
            abort(422)

    @app.route('/questions', methods=['POST'])
    def create_search_question():
        '''
        POST endpoing to create a new question or search for a questions,
        Creation requires the question and an answer text, category,
        and difficulty score. Search requires search term.
        '''
        body = request.get_json()
        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)
        search_term = body.get('searchTerm', None)

        try:
            if search_term:
                questions = Question.query.filter(
                    Question.question.ilike('%{}%'.format(search_term))).all()
                page = request.args.get('page', 1, type=int)
                page_questions = paginate(page, questions)

                if len(page_questions) == 0:
                    abort(404)

                else:
                    return jsonify({
                        'success': True,
                        'questions': page_questions,
                        'total_questions': len(questions),
                        'current_category': 'All'
                    })

            else:
                if not new_question or not new_answer \
                        or not new_category or not new_difficulty:
                    abort(400)

                else:
                    question = Question(
                        question=new_question,
                        answer=new_answer,
                        category=new_category,
                        difficulty=int(new_difficulty)
                    )

                    question.insert()

                    return jsonify({
                        'success': True,
                        'created': question.id,
                    })

        except:
            abort(422)

    @app.route('/categories/<int:category_id>/questions')
    def retrieve_category_questions(category_id):
        ''' GET endpoint to get questions based on category.'''
        category = Category.query.filter_by(id=category_id).one_or_none()

        if category is None:
            abort(404)

        questions = Question.query.filter_by(category=str(category_id)).all()
        page = request.args.get('page', 1, type=int)
        page_questions = paginate(page, questions)

        if len(page_questions) == 0:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'questions': page_questions,
                'total_questions': len(questions),
                'current_category': category.type
            })

    @app.route('/quizzes', methods=['POST'])
    def play():
        body = request.get_json()
        previous_questions = body.get('previous_questions', [])
        category = body.get(
            'quiz_category', {"id": 0, "type": "All"}).get('id')
        if category == 0:
            category = '1'

        question = Question.query.filter_by(category=category).filter(
            Question.id not in previous_questions).first()

        return jsonify({
            'success': True,
            'question': question.format()
        })

    @app.errorhandler(400)
    def bad_request(error):
        '''Handles 400 Error'''
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        '''Handles 404 Error'''
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not Found"
        }), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        '''Handles 405 Error'''
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method Not Allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable(error):
        '''Handles 422 Error'''
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity"
        }), 422

    return app
