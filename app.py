from flask import Flask, render_template, request, redirect, json, send_from_directory
import requests as r 
from bs4 import BeautifulSoup
from openpyxl import Workbook


app = Flask(__name__, static_url_path='', static_folder='static')

print(app.static_url_path)
print(app.static_folder)


ROOT_URL = 'https://www.sitelike.org/'

session = r.Session()

@app.route('/')
def home():
    
    return render_template('home2.html')

@app.route('/submit',methods=["POST"])
def submit():

    data = request.get_data().decode('utf-8')
    data = json.loads(data)
    URLS = data['urls']
    URLS = URLS.split(" ")

    websites=[]
    for SLUG_URL in URLS:
        s = session.get(ROOT_URL + 'similar/' +SLUG_URL)
        contents = BeautifulSoup(s.content, 'html.parser')
        panels_blocks = contents.find_all('div', class_='row panel panel-default rowP')
        for block in panels_blocks:
            links = block.find_all('a', class_ = 'btn btn-link btn-lg')
            website_name = links[0].text.split('\n')[1]
            website_sitelike_url = links[0].get('href')
            website_url = website_name
            if len(links)>1:
                website_url = links[1].get('href')
            websites.append(website_url)
            # print(website_name,'----->', website_sitelike_url, '----->',website_url)
    
    wb = Workbook()
    sheet = wb.active
    x=len(websites)
    for i in range(x):
        sheet.append([websites[i]])
    file_name = 'urls.xlsx'
    PATH = ''
    wb.save(PATH+file_name)

    try:
        print("trying to send file")
        return send_from_directory(PATH, file_name, as_attachment=True)
    except Exception as e:
        print(e)
        return {"error":str(e)}






@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('error2.html'), 404





if __name__ == '__main__':
    app.run(debug=True)
