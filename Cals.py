from flask import Flask,request, jsonify
# Route for addition
app = Flask(__name__)
# Route for addition that takes num1 and num2 directly in the route

##Addition 
@app.route('/add/<int:num1>/<int:num2>', methods=['GET'])
def add(num1, num2):
    result = num1 + num2
    return jsonify(result=result)

##Subtraction
@app.route('/sub/<int:num1>/<int:num2>', methods=['GET'])
def sub(num1, num2):
    result = num1 - num2
    return jsonify(result=result)

##Multiplocation
@app.route('/mul/<int:num1>/<int:num2>', methods=['GET'])
def mul(num1, num2):
    result = num1 * num2
    return jsonify(result=result)

##Devision
@app.route('/div/<float:num1>/<float:num2>', methods=['GET'])
def div(num1, num2):
    result = num1/num2
    return jsonify(result=result)
 
if __name__ == '__main__':
    app.run(debug=True)

