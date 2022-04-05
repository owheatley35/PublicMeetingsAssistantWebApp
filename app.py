import logging
import threading

from flask import Flask, send_from_directory, jsonify, _request_ctx_stack, request
from flask_cors import CORS, cross_origin

# Created with help from this tutorial: https://towardsdatascience.com/build-deploy-a-react-flask-app-47a89a5d17d9
from api.endpoints.CreateMeetingEndpoint import CreateMeetingEndpoint
from api.endpoints.DeleteMeetingEndpoint import DeleteMeetingEndpoint
from api.endpoints.GetBasicMeetingsEndpoint import GetBasicMeetingsEndpoint
from api.endpoints.GetMeetingEndpoint import GetMeetingEndpoint
from api.endpoints.UserRoleEndpoint import UserRoleEndpoint
from api.endpoints.notes.CreateNoteEndpoint import CreateNoteEndpoint
from api.endpoints.notes.DeleteNoteEndpoint import DeleteNoteEndpoint
from api.endpoints.notes.UpdateNoteEndpoint import UpdateNoteEndpoint
from security.auth_zero_authentication import requires_auth
from security.credentials import auth0_domain, api_audience, algorithms, auth0_key
from security.exceptions.AuthError import AuthError

# Auth0 configuration
AUTH0_DOMAIN = auth0_domain
API_AUDIENCE = api_audience
ALGORITHMS = algorithms
AUTH0_KEY = auth0_key

# Flask App initiation
app = Flask(__name__, static_url_path='', static_folder='ui/build')
CORS(app)


@app.errorhandler(AuthError)
def handle_auth_error(ex):
    """
    Handling of users being un authorised or un-authenticated when accessing secure endpoints.
    """
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response


#  === ENDPOINTS: ===

@app.route('/', defaults={'path': ''})
@app.errorhandler(404)
def root(path):
    """
    Base endpoint returning the React frontend app found in /ui
    """
    return send_from_directory(app.static_folder, 'index.html')


@app.route("/api/get/all-basic-meetings")
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_basic_meetings():
    """
    Endpoint to retrieve basic information about all meetings belonging to a user.

    SECURE ENDPOINT
    """
    endpoint = GetBasicMeetingsEndpoint(_request_ctx_stack.top.current_user_id)
    endpoint_result = endpoint.get_endpoint_result()
    threading.Thread(target=endpoint.close_endpoint).start()
    return jsonify(message=endpoint_result)


@app.route("/api/get/meeting-from-id", methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_meeting_from_id():
    """
    Endpoint to gather the full information of a meeting from a meeting and user ID

    SECURE ENDPOINT
    """
    meeting_id = request.json["meeting_id"]
    endpoint = GetMeetingEndpoint(_request_ctx_stack.top.current_user_id, meeting_id)
    endpoint_result = endpoint.get_endpoint_result()
    threading.Thread(target=endpoint.close_endpoint).start()
    return jsonify(meeting=endpoint_result)


@app.route("/api/update/meeting-note", methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def update_meeting_note():
    """
    Endpoint to update the value of a meeting note.

    SECURE ENDPOINT
    """
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
    """
    Endpoint to create a meeting note.

    SECURE ENDPOINT
    """
    meeting_id = request.json["meeting_id"]
    note_content = request.json["note_content"]
    endpoint = CreateNoteEndpoint(_request_ctx_stack.top.current_user_id, meeting_id, note_content)
    endpoint.create_note()
    endpoint.close_endpoint()
    return jsonify(success=True)


@app.route("/api/delete/meeting-note", methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def delete_meeting_note():
    """
    Endpoint to delete a Meeting Note.

    SECURE ENDPOINT
    """
    meeting_id = request.json["meeting_id"]
    note_index = request.json["note_index"]
    endpoint = DeleteNoteEndpoint(_request_ctx_stack.top.current_user_id, meeting_id, note_index)
    endpoint.delete_note()
    endpoint.close_endpoint()
    return jsonify(success=True)


@app.route("/api/create/meeting", methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def create_meeting():
    """
    Endpoint to create a meeting.

    SECURE ENDPOINT
    """
    meeting_title = request.json["meeting_title"]
    meeting_description = request.json["meeting_description"]
    meeting_date = request.json["meeting_date"]
    meeting_time = request.json["meeting_time"]
    meeting_attendees = request.json["meeting_attendees"]

    endpoint = CreateMeetingEndpoint(_request_ctx_stack.top.current_user_id, meeting_title, meeting_description,
                                     meeting_date, meeting_time, meeting_attendees)
    endpoint.create_meeting()
    endpoint.close_endpoint()
    return jsonify(success=True)


@app.route("/api/delete/meeting", methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def delete_meeting():
    """
    Endpoint to delete a meeting.

    SECURE ENDPOINT
    """

    meeting_id = request.json["meeting_id"]
    endpoint = DeleteMeetingEndpoint(_request_ctx_stack.top.current_user_id, meeting_id)
    response = endpoint.delete_meeting()
    endpoint.close_endpoint()
    return jsonify(response.get_formatted_response())


@app.route("/api/get/user/role", methods=["POST"])
@cross_origin(headers=["Content-Type", "Authorization"])
@requires_auth
def get_user_role():
    """
    Endpoint to delete a meeting.

    SECURE ENDPOINT
    """

    endpoint = UserRoleEndpoint(_request_ctx_stack.top.current_user_id)
    role = endpoint.get_user_role()
    endpoint.close_endpoint()
    return role.get_formatted_response()


# Start the Flask App
if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000)
