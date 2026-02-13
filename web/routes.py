"""
Routes
"""

from flask import request, jsonify
from services.timetable_service import TimetableService

service = TimetableService()

def register_routes(app):
    @app.route('/generate', methods=['POST'])
    def generate():
        data = request.json
        timetable = service.create_timetable(data)
        return jsonify(timetable)