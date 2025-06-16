# Import necessary tools from Flask
# Flask: the web framework
# render_template: for showing HTML pages
# request: for handling form data
from flask import Flask, render_template, request

# Create a new Flask web application
# __name__ tells Flask where to look for templates and static files
app = Flask(__name__)

# Define what happens when someone visits the website
# '/' means the main page (like example.com/)
# methods=['GET', 'POST'] means this route can handle both:
# - GET: when someone just visits the page
# - POST: when someone submits the form
@app.route('/', methods=['GET', 'POST'])
def main():
    # Check if someone submitted the form (POST request)
    if request.method == 'POST':
        # Get the name from the form
        # If no name was provided, use an empty string
        name = request.form.get('name', '')
        # Show the webpage with the name included
        return render_template('index.html', name=name)
    # If it's a GET request (just visiting the page)
    # Show the webpage without a name
    return render_template('index.html')

# Only run the server if this file is run directly
# (not if it's imported by another file)
if __name__ == "__main__":
    # Start the web server
    # debug=True means it will show errors in the browser
    # port=3001 means the website will be at http://localhost:3001
    app.run(debug=True, port=3001) 