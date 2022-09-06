from flask_restx import Namespace, Resource, inputs, reqparse

from mutalyzer.name_checker import name_check, name_check_alt

from .common import errors

ns = Namespace("/")


_args = reqparse.RequestParser()

_args.add_argument(
    "sequence",
    type=str,
    help="Reference sequence.",
    required=False,
)

_args.add_argument(
    "only_variants",
    type=inputs.boolean,
    help="The description consists only of variants.",
    default=False,
    required=False,
)


@ns.route("/name_check/<string:description>")
class NameCheck(Resource):
    @ns.expect(_args)
    @errors
    def get(self, description):
        """Normalize a variant description."""
        return name_check(description, **_args.parse_args())


@ns.route("/name_check_alt/<string:description>")
class NameCheckAlt(Resource):
    @ns.expect(_args)
    @errors
    def get(self, description):
        """Normalize a variant description."""
        return name_check_alt(description, **_args.parse_args())
