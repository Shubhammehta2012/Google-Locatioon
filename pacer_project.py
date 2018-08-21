


import pandas as pd


data = pd.read_csv('C:/Users/shubh/Desktop/saloni/OP_DTL_OWNRSHP_PGYR2016_P06292018.csv')


name = input('Please give the name: ')


count = 0 
got = ''
chk = False
for i in data.Physician_First_Name:
    if str(i).lower().strip() == name.strip().lower():
        chk = True
        break
    count = count + 1

if chk:
    count2 = 0
    for a in data.Recipient_Primary_Business_Street_Address_Line1:
        if count2 == count:
            got = got + str(a.strip()) + ' '
            break
        count2 = count2 + 1

    count2 = 0
    for c in data.Recipient_City:
        if count2 == count:
            got = got + str(c.strip()) + ' '
            break
        count2 = count2 + 1

    count2 = 0
    for d in data.Recipient_State:
        if count2 == count:
            got = got + str(d.strip()) + ' '
            break
        count2 = count2 + 1

    count2 = 0
    for e in data.Recipient_Zip_Code:
        if count2 == count:
            got = got + str(e)
            break
        count2 = count2 + 1


    ad = got
    st = ad.split(' ')

    import requests
    
    GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

    params = {
        'address': ad,
        'sensor': 'false',
        'region': 'uk'
    }

    # Do the request and get the response data
    req = requests.get(GOOGLE_MAPS_API_URL, params=params)
    res = req.json()

    # Use the first result
    result = res['results'][0]

    geodata = dict()
    geodata['lat'] = result['geometry']['location']['lat']
    geodata['lng'] = result['geometry']['location']['lng']
    geodata['address'] = result['formatted_address']

    loc = 'https://www.google.com/maps/place/'
    for i in st:
        loc = loc + '+' + str(i)

    loc = loc + '/@' + str(geodata['lat']) + ',' + str(geodata['lng'])

    loc = loc + '/data=!3m1!4b1!4m5!3m4!1s0x808fba027820e5d9:0x60a90600ff6e7e6e!8m2!3d'

    loc = loc + str(geodata['lat']) + 'd-' + str(geodata['lng'])

    loc = loc + '?hl=en&authuser=0'

    import webbrowser
    webbrowser.open(loc)

else:
    print('The entered name does not exist in database')


# In[ ]:



