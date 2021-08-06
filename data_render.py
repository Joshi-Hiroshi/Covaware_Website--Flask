import requests

def daywise_data_world():
    day_wise = requests.get("https://corona.lmao.ninja/v2/all")
    global_data = day_wise.json()
    #print(day_wise_data)
    new_confirmed = global_data['todayCases']
    print(new_confirmed)
    total_confirmed = global_data['cases']

    new_deaths = global_data['todayDeaths']
    total_deaths = global_data['deaths']

    new_recovered = global_data['todayRecovered']
    total_recovered = global_data['recovered']

    c_per_mil = global_data["casesPerOneMillion"]
    d_per_mil = global_data["deathsPerOneMillion"]
    tests_per_mil = global_data["testsPerOneMillion"]
    total_tests = global_data["tests"]
    #i = 1
    '''for item in day_wise_data:
        day.append(i)
        new_confirmed.append(item['Confirmed'])
        new_deaths.append(item['Deaths'])
        i += 1'''
    
    return {"NewC" : f'{new_confirmed:,}' , "TotalC": f'{total_confirmed:,}' , "NewD" :f'{new_deaths:,}' , "TotalD": f'{total_deaths:,}', "NewR" : f'{new_recovered:,}' , "TotalR": f'{total_recovered:,}' , 'casesPerOneMillion': f'{c_per_mil:,}' , 'deathsPerOneMillion': d_per_mil , "testsPerOneMillion": f'{tests_per_mil:,}' ,"tests": f'{total_tests:,}' }



def daywise_data_india():
    day_wise = requests.get("https://api.covid19api.com/dayone/country/india")
    day_wise_data = day_wise.json()

    day = []
    confirmed = []
    deaths = []
    i = 1
    for item in day_wise_data:
        day.append(i)
        confirmed.append(item['Confirmed'])
        deaths.append(item['Deaths'])
        i += 1
    
    daywise_multi_list = [day[:-1], confirmed[:-1], deaths[:-1]]
    del day
    del confirmed
    del deaths
    return daywise_multi_list



def statewise_analysis():
    state_data = requests.get("https://api.covid19india.org/state_district_wise.json")
    state_data = state_data.json()
    state_names = []
    statewise_confirmed = []
    statewise_deaths = []
    statewise_recovered = []
    statewise_active = []
    i = 0
    for states in state_data:
        state_names.append(states)
        statewise_confirmed.append(0)
        statewise_deaths.append(0)
        statewise_recovered.append(0)
        statewise_active.append(0)
        
        for districts in state_data[states]['districtData']:
            statewise_confirmed[i] += state_data[states]['districtData'][districts]['confirmed']
            statewise_deaths[i] += state_data[states]['districtData'][districts]['deceased']
            statewise_recovered[i] += state_data[states]['districtData'][districts]['recovered']
            statewise_active[i] += state_data[states]['districtData'][districts]['active']
        i += 1

    states_dict = {}
    for i in range(len(state_names)):
        states_dict.update({state_names[i]:[statewise_confirmed[i], statewise_active[i], statewise_recovered[i], statewise_deaths[i]]})
    states_sorted_list = sorted(states_dict.items(), key = lambda kv:[kv[1], kv[0]], reverse = True)
    final_state_names = []
    final_statewise_confirmed = []
    final_statewise_active = []
    final_statewise_recovered = []
    final_statewise_deaths = []
    for item in states_sorted_list:
        final_state_names.append(item[0])
        final_statewise_confirmed.append(item[1][0])
        final_statewise_active.append(item[1][1])
        final_statewise_recovered.append(item[1][2])
        final_statewise_deaths.append(item[1][3])
    state_report_list = [final_state_names, final_statewise_confirmed, final_statewise_active, final_statewise_recovered, final_statewise_deaths]
    del state_names
    del statewise_confirmed
    del statewise_deaths
    del statewise_recovered
    del statewise_active
    del final_state_names
    del final_statewise_confirmed
    del final_statewise_active
    del final_statewise_recovered
    del final_statewise_deaths
    del states_sorted_list
    return state_report_list

def district_zone_analysis():
    import requests
    district_data = requests.get("https://api.covid19india.org/zones.json").json()
    states_district = {}
    states_district_zone = {}
    for item in district_data['zones']:
        if item['state'] not in states_district:
            states_district[item['state']] = [item['district']]
            states_district_zone[item['state']] = {item['district']:[item['lastupdated'],item['zone']]}
        else:
            states_district[item['state']].append(item['district'])
            states_district_zone[item['state']].update({item['district']:[item['lastupdated'],item['zone']]})
    return [states_district, states_district_zone]
