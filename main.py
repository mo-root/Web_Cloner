from flask import Flask, request, send_file, render_template
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        # Request the website
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Get the HTML content
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')

            # Create a directory named `clone` to store the files
            dir_path = os.path.join(os.getcwd(), "clone")
            if not os.path.exists(dir_path):
                os.makedirs(dir_path)

            # Download all the files
            for link in soup.find_all("a"):
                href = link.get("href")
                if href.startswith("http"):
                    # Name the file `duplicate`
                    file_path = os.path.join(dir_path, "duplicate.html")

                    # Download the file
                    file_response = requests.get(href)
                    with open(file_path, "wb") as f:
                        f.write(file_response.content)

            return render_template("download.html", file_path=file_path)
        else:
            return "Couldn't reach the URL"
    return render_template("form.html")


@app.route('/download/<path:file_path>')
def download(file_path):
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run()
