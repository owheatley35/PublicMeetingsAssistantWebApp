import threading

from flask import Flask, send_from_directory, jsonify, _request_ctx_stack
from flask_cors import CORS, cross_origin

# Created with help from this tutorial: https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9
from api.endpoints.GetBasicMeetingsEndpoint import GetBasicMeetingsEndpoint
from security.auth_zero_authentication import requires_auth
from security.credentials import auth0_domain, api_audience, algorithms, auth0_key
from security.exceptions.AuthError import AuthError

AUTH0_DOMAIN = auth0_domain
API_AUDIENCE = api_audience
ALGORITHMS = algorithms
AUTH0_KEY = auth0_key

app = Flask(__name__, static_url_path='', static_folder='ui/build')
CORS(app)


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


# ENDPOINTS:
@app.route('/', defaults={'path': ''})
@app.errorhandler(404)
def root(path):
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/api/get/all-basic-meetings")
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_basic_meetings():
    endpoint = GetBasicMeetingsEndpoint(_request_ctx_stack.top.current_user_id)
    endpoint_result = endpoint.get_endpoint_result()
    threading.Thread(target=endpoint.close_endpoint).start()
    return jsonify(message=endpoint_result)


if __name__ == '__main__':
    app.run()
