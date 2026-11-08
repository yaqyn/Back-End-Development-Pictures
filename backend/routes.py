from . import app
import os
import json
from flask import jsonify, request, make_response, abort, url_for  # noqa; F401

SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
json_url = os.path.join(SITE_ROOT, "data", "pictures.json")
data: list = json.load(open(json_url))

######################################################################
# RETURN HEALTH OF THE APP
######################################################################


@app.route("/health")
def health():
    return jsonify(dict(status="OK")), 200

######################################################################
# COUNT THE NUMBER OF PICTURES
######################################################################


@app.route("/count")
def count():
    """return length of data"""
    if data:
        return jsonify(length=len(data)), 200

    return {"message": "Internal server error"}, 500


######################################################################
# GET ALL PICTURES
######################################################################
@app.route("/picture", methods=["GET"])
def get_pictures():
    """Return every picture in the in-memory collection."""
    return jsonify(data), 200

######################################################################
# GET A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["GET"])
def get_picture_by_id(id):
    """Return one picture by id, or 404 when it does not exist."""
    picture = next((item for item in data if item["id"] == id), None)
    if picture is None:
        return {"message": "picture not found"}, 404

    return jsonify(picture), 200


######################################################################
# CREATE A PICTURE
######################################################################
@app.route("/picture", methods=["POST"])
def create_picture():
    """Create a picture and reject a duplicate id."""
    picture = request.get_json(silent=True)
    if not isinstance(picture, dict) or "id" not in picture:
        return {"message": "invalid picture payload"}, 400

    if any(item["id"] == picture["id"] for item in data):
        return {
            "Message": f"picture with id {picture['id']} already present"
        }, 302

    data.append(picture)
    return jsonify(picture), 201

######################################################################
# UPDATE A PICTURE
######################################################################


@app.route("/picture/<int:id>", methods=["PUT"])
def update_picture(id):
    """Replace an existing picture."""
    picture = request.get_json(silent=True)
    if not isinstance(picture, dict):
        return {"message": "invalid picture payload"}, 400

    for index, existing in enumerate(data):
        if existing["id"] == id:
            data[index] = picture
            return jsonify(picture), 200

    return {"message": "picture not found"}, 404

######################################################################
# DELETE A PICTURE
######################################################################
@app.route("/picture/<int:id>", methods=["DELETE"])
def delete_picture(id):
    """Delete a picture and return an empty 204 response."""
    for index, picture in enumerate(data):
        if picture["id"] == id:
            data.pop(index)
            return "", 204

    return {"message": "picture not found"}, 404
