import quart
import json
from app.utils import decorators
from app.utils import data as data_utils

blueprint = quart.Blueprint("tokens", __name__)


@blueprint.route("/api/tokens/verify", methods=["POST"])
@decorators.req_fields({"token": str})
async def token_verify():
    json_resp = await quart.request.json
    token = json_resp["token"]
    result = await data_utils.verify_token(token)
    return quart.jsonify({"result": result})
