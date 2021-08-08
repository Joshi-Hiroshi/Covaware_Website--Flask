from flask import Flask, render_template, request, redirect , flash , url_for,json,jsonify
import data_file
import requests
from flask_sitemap import Sitemap


app=Flask(__name__)
app.config['SECRET_KEY'] = 'babaBlackSheep$123'

#Main Home Route
@app.route("/")
def home():
    return render_template("index.html")

def data_in(Country, State=None):
    index_in, data_in_c = data_file.data_Confirmed(Country, State)
    data_in_r = data_file.data_Recovered(Country, State)
    data_in_d = data_file.data_Deaths(Country, State)

    return [index_in, data_in_c, data_in_r, data_in_d]


@app.route('/world_map', methods=['GET'])
def world_wide():
    list_of_data = data_file.data_of_world_wide()
    index = [['Country', 'Confirmed', 'Recovered']]
    for i in list_of_data:
        index.append(i)
    data_json = json.dumps(index)
    # print(index[0:2], type(index))

    return render_template('worldwide.html', list_data=data_json)

@app.route("/covid/cases")
def covid_cases():
    from data_render import daywise_data_world
    data = daywise_data_world()
    
    return render_template("covid_cases.html" , data = data )

@app.route("/covid/india", methods = ["POST", "GET"])
def india():

    from data_render import daywise_data_india
    india_plot_daywise_data = daywise_data_india()
    day = india_plot_daywise_data[0]
    confirmed = india_plot_daywise_data[1]
    deaths = india_plot_daywise_data[2]

    from data_render import statewise_analysis
    statewise_data = statewise_analysis()

    india_data_url = "https://disease.sh/v2/countries/India?yesterday=true&strict=true"
    india_content = requests.get(india_data_url)
    india_data = india_content.json()

    #from data_render import district_zone_analysis
    #states_district_zone_data = district_zone_analysis()
    #district_data = states_district_zone_data

    return render_template("india.html", data = india_data, day = day, confirmed = confirmed, deaths = deaths, states = statewise_data)

@app.route("/about")
def about_page():
    return render_template("about.html")

@ext.register_generator
def sitemap():
    yield 'home' , {}
    yield 'india' , {}
    yield 'covid_cases', {}
    yield 'abt_covid',{}
    yield 'symptoms',{}
    yield 'precautions',{}
    yield 'myths',{}
    yield 'vaccines',{}
    yield 'stuff',{}
    yield 'about_page' ,{}
    yield 'world_wide',{}

#app.run(debug=True)
