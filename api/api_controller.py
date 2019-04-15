from flask import Blueprint, jsonify

api = Blueprint('api', __name__)


@api.route('/test')
def test_api():
    """Test API call."""
    return jsonify({'x': 'y'})
