from flask import Flask
# just serve all the static files under root
app = Flask(__name__, static_folder='.', static_url_path='')

# for / root, return Hello Word
@app.route("/")
def root():
    return 'Hello World!'

# Remember from flask import request
# for /request and POST method
@app.route('/request',methods=['POST'])
def request():
  payload=request.data
  # if accept json object as string
  data = json.loads(payload)
  # if accept normal string
  data = payload
  # After process
  
  # If still return json, Remember using jsonify(data) to return.
  # Do not need to return status, and mimetype. jsonify has
  # already helped you do that.
  return jsonify(data)
  return data, 200, {'Content-Type': 'application/json'}
  
  
  # Otherwise, just return with status and type
  # The mimetype can be text/xml, text/html.
  return data, 200, {'Content-Type': 'text/txt'}
  
  
  
  
# start listening
if __name__ == "__main__":
    app.run(debug=True, port='3000', host='0.0.0.0')
    
    
