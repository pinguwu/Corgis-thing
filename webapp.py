from flask import Flask, url_for, render_template, request, Markup
import os
import json
app = Flask(__name__)

@app.route("/") #the default thing
def render_main():
    with open('state_demographics.json') as demographics_data:
        states = json.load(demographics_data)
    try:
        state = request.args['states']
        madre= get_fun_fact(state)
        print(madre)
        return render_template('index.html', states = get_state_options(states), funfact = get_fun_fact(state))
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

def get_fun_fact(states):
    state = states

    with open('state_demographics.json') as list_o_things:
        info = json.load(list_o_things)

        #highest median income i guess lmao

    most_under = info[0]["County"]
    state_most_under = info[0]["State"]
    percent = info[0]["Income"]["Median Household Income"]
    loas = {}
    for x in info:
        if (x["Income"]["Median Household Income"] > percent):
            most_under = x["County"]
            state_most_under = x["State"]
            percent = x["Income"]["Median Household Income"]
            loas[state_most_under] = percent

    return Markup("<p>" + "This state has a median household income of: " + str(loas.get(state) + "</p>"))

if __name__=="__main__":
    app.run(debug=True)
