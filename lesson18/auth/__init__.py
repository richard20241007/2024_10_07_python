from flask import Blueprint
auth = Blueprint('auth', __name__)
from . import registration
from . import login
from . import successful

