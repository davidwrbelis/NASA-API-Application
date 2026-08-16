import requests
from flask  import Flask, render_template

#Sending JSON Data (POST Request) (try this as well)

app = Flask(__name__)
url = "https://ll.thespacedevs.com/2.3.0/events/upcoming/?format=json"

space_image       = []
image_description = []
slug              = []
return_list       = []
image_date        = []
location          = []

try:
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        print('inside the if statement')
        data = response.json() # .json() method to immediately convert the response string
        print('success!')      #  method to immediately convert the response string into a usable Python dictionary or list
        print(data)
        for i in range(0,10):
            space_image.append(data['results'][i]["image"]["thumbnail_url"])
            image_description.append(data['results'][i]["description"])
            slug.append(data['results'][i]["slug"])
            image_date.append(data['results'][i]["date"][:16])
            location.append(data['results'][i]["location"])


    for i in range(len(space_image)):
        return_list.append({'image'       : space_image[i],
                            'description' : image_description[i],
                            'slug'        : slug[i],
                            'image_date'  : image_date[i],
                            'location'    : location[i]}
                           )
        print(return_list)
except Exception as e:
    print(e)

@app.route("/", methods = ['GET', 'POST'])
def home():
    return render_template("index.html", p_return_list = return_list)


    ###############################################################################
if __name__ == '__main__':
    print('call function app.run()')
    app.run(debug=True)
    print("past app.run()")