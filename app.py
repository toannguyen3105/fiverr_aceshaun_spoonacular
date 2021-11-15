# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 21:10:10 2021

@author: Maryam Botrus
"""
from flask import Flask, request
from flask import render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def main_page():
    if request.method == 'GET':
        return render_template("index.html")
    else:
        data = request.form
        print(data)
        food_name = data['food-name']
        print(food_name)

        import requests

        url = f"https://api.spoonacular.com/recipes/complexSearch?query={food_name}&apiKey=7eed9fc216f3497787aace1852c949ab"

        payload = {}
        headers = {}

        response = requests.request("GET", url, headers=headers, data=payload)

        print(response.text)
        print(response.json())
        print(response.json()['results'])
        print(response.json()['offset'])
        print(response.json()['number'])
        print(response.json()['totalResults'])

        return render_template("index.html", food_name=food_name, response=response.json())


'''
tabulates food costs
'''


@app.route("/calculator")
def food_costs():
    return render_template("calculator.html")


'''
 provides nutritional information on food options
 consider building api logic in a seperate class 
'''


@app.route("/nutrition")
def nutrition():
    return render_template("nutrition.html")


@app.route("/recipes")
def recipes():
    return render_template("recipes.html")


@app.route("/diet_selection")
def diets():
    return render_template("diet_selection.html")


'''
allows the user to search for different meal or food options
'''


@app.route("/meals")
def meal_search():
    return render_template("meal_search.html")


if __name__ == "__main__":
    app.run(debug=True)
