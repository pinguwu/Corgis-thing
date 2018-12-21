
from flask import Flask, url_for, render_template, request, flash, Markup
import os
import json
app = Flask(__name__)

@app.route("/")
def render_main():
    return render_template("home.html")

def fun_fact(state):
    with open('state_demographics.json') as demographics_data:
        states = json.load(demographics_data)
    boi = 0
    for s in states:
        if s["State"] == state:
            boi = s["Income"]["Median Houseold Income"]
    
    print (state + "'s Median Income is " + str(boi))
    return state + "'s Median Income is $" + str(boi)

@app.route("/med") #annotation tells the URL that will make this function run
def render_med():
    with open('state_demographics.json') as demographics_data:
        states = json.load(demographics_data)
    try:
        state = request.args['states']
        ff = fun_fact(state)
        return render_template("med.html", states = get_state_options(states), funfact = ff)
    except:
        return render_template("med.html", states = get_state_options(states))

def get_state_options(states):
  bom=[]

  for state in states:
    state = state["State"]
    trfl = state in bom
    if (trfl == False):
      bom.append(state)


  options = ""
  for state in bom:
    options += Markup("<option value=\"" + state + "\">" + state + "</option>")

  return options


@app.route("/about")
def render_about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(debug=False, port=66666)