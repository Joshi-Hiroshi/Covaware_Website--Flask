from flask import Flask, render_template, request, redirect , flash , url_for,json,jsonify
import data_file

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

@app.route("/about")
def about_page():
    return render_template("about.html")

app.run(debug=True)