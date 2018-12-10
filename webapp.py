from flask import Flask, url_for, render_template, request, Markup
import os
import json
app = Flask(__name__)

@app.route("/") #the default thing
def render_main():
    with open('state_demographics.json') as demographics_data:
        statess = json.load(demographics_data)
    try:
        state = request.args['states']
        madre = get_fun_fact(state)
        return render_template('index.html', states = get_state_options(states), funfact = madre)
    except:
        return render_template('index.html', states = get_state_options(states))

def get_state_options(states):
  yeetus=[]

  for state in states:
    state = state["State"]
    chief = state in yeetus
    if (chief == False):
      yeetus.append(state)


  options = ""
  for state in yeetus:
    options += Markup("<option value=\"" + state + "\">" + state + "</option>")

  return options

def get_fun_fact(staterino):
    state = request.args["states"]

    with open('state_demographics.json') as list_o_things:
        info = json.load(list_o_things)

        #highest median income i guess lmao

    bigboi = 0
    for state in info:
        if state["State"] == staterino:
            if (state["Income"]["Median Household Income"] > bigboi):
                bigboi = state["Income"]["Median Household Income"]
                higheststate = state["State"]

    return state + "'s Median Household Income is " +  "$" + "{:,}".format(bigboi)

if __name__=="__main__":
    app.run(debug=True)
