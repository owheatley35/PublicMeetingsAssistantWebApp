import threading

from flask import Flask, send_from_directory, jsonify, _request_ctx_stack, request
from flask_cors import CORS, cross_origin

# Created with help from this tutorial: https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9
from api.endpoints.GetBasicMeetingsEndpoint import GetBasicMeetingsEndpoint
from api.endpoints.GetMeetingEndpoint import GetMeetingEndpoint
from api.endpoints.notes.CreateNoteEndpoint import CreateNoteEndpoint
from api.endpoints.notes.UpdateNoteEndpoint import UpdateNoteEndpoint
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


@app.route("/api/get/meeting-from-id", methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_meeting_from_id():
    meeting_id = request.json["meeting_id"]
    endpoint = GetMeetingEndpoint(_request_ctx_stack.top.current_user_id, meeting_id)
    endpoint_result = endpoint.get_endpoint_result()
    threading.Thread(target=endpoint.close_endpoint).start()
    return jsonify(meeting=endpoint_result)


@app.route("/api/update/meeting-note", methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def update_meeting_note():
    meeting_id = request.json["meeting_id"]
    note_content = request.json["note_content"]
    note_index = request.json["note_index"]
    endpoint = UpdateNoteEndpoint(_request_ctx_stack.top.current_user_id, meeting_id, note_content, note_index)
    endpoint.update_note()
    endpoint.close_endpoint()
    return jsonify(success=True)


@app.route("/api/create/meeting-note", methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def create_meeting_note():
    meeting_id = request.json["meeting_id"]
    note_content = request.json["note_content"]
    endpoint = CreateNoteEndpoint(_request_ctx_stack.top.current_user_id, meeting_id, note_content)
    endpoint.create_note()
    endpoint.close_endpoint()
    return jsonify(success=True)


if __name__ == '__main__':
    app.run()
