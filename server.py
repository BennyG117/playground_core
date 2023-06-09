from flask import Flask, render_template
#, render_template  # Import Flask to allow us to create our app

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')
def index():
    return render_template("index3.html",x=4,color="aqua")

@app.route('/play/<int:num>/')
def level_2(num):
    return render_template("index3.html",x=num,color="aqua")

@app.route('/play/<int:num>/<color>/')
def level_3(num, color):
    return render_template("index3.html",x=num, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, port=5001)






# @app.route('/') 
# def hello_world():
#     return 'Hello World!'
# #"render_template("index.html"")  # Return the string 'Hello World!' as a response

# @app.route('/dojo')
# def dojo_name():
#     return 'Dojo!'

# @app.route('/say/<string:name>')
# def hi_name(name):
#     return f'Hi {name.title()}!'

# @app.route('/repeat/<int:num>/<string:word>')
# def repeating_word(num, word):
#     repeating_word = word * num
#     return repeating_word



# @app.errorhandler(404)
# def error_found(e):
#     return "Sorry! No response. Try again.",404

