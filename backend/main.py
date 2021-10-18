from sanic import Sanic, response
from sanic_cors import CORS
import json


def create_app():
    app = Sanic(__name__)
    CORS(app, automatic_options=True)

    @app.route("/", methods=["GET"])
    async def index(request):
        return response.json({'message': 'Backend Service !'}, headers={'X-Served-By': 'sanic'}, status=200)

    @app.route("/backend", methods=["GET"])
    async def analytics(request):
        return response.html('<p>Backend</p>')

    # Modify to take a search filter and return only matching results
    # @app.route("/backend/stores", methods=["POST"])
    @app.route("/backend/stores", methods=["GET"])

    async def stores(request):
        stores = [
            {"id": 1, "name": "Buffalo", "tags": "gen3, northeast"},
            {"id": 2, "name": "Gilbert", "tags": "gen3, southwest, kitchen"},
            {"id": 3, "name": "Water Buffalo", "tags": "gen2, northeast"},
            {"id": 4, "name": "North Buffalo 17", "tags": "gen2, northeast"},
            {"id": 5, "name": "Tempe 12", "tags": "gen3, southwest, kitchen"},
            {"id": 6, "name": "Avondale 5", "tags": "gen2, southwest"},
            {"id": 7, "name": "Phoenix 55", "tags": "gen3, southwest, kitchen"},
            {"id": 8, "name": "Kenmore 91", "tags": "gen3, northeast"},
            {"id": 9, "name": "Kenmore 97", "tags": "gen3, northeast, kitchen"},
            {"id": 10, "name": "Mesa 12", "tags": "gen3, southwest, kitchen"},
            {"id": 11, "name": "Mesa 18", "tags": "gen3, southwest, kitchen"},
            {"id": 12, "name": "Mesa 22", "tags": "gen3, southwest"},
            {"id": 13, "name": "Mesa 25", "tags": "gen3, southwest, kitchen"},
            {"id": 14, "name": "Apache Junction", "tags": "gen3, southwest, kitchen"},
            {"id": 15, "name": "Scottdale 243", "tags": "gen3, southwest, kitchen"},
            {"id": 16, "name": "Scottsdale 245", "tags": "gen2, southwest"},
            {"id": 17, "name": "Scottsdale 252", "tags": "gen2, southwest"},
            {"id": 18, "name": "Scottsdale 310", "tags": "gen2.5, southwest"},
            {"id": 19, "name": "Scottsdale 320", "tags": "gen3, southwest"},
            {"id": 20, "name": "Scottsdale 142", "tags": "gen4, southwest, kitchen"}
        ]

        return response.json({'stores': stores})

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5004)
