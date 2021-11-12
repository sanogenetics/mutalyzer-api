from flask_restx import Namespace, Resource, reqparse

from mutalyzer.mutator import mutate

from .common import errors

ns = Namespace("/")


@ns.route("/mutate/<string:description>")
class Mutate(Resource):
    def get(self, description):
        """Obtain the observed sequence from a description."""
        return mutate(description)
