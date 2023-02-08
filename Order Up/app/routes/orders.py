from flask import Blueprint, render_template
from flask_login import current_user, login_required

bp = Blueprint("orders", __name__, url_prefix="")


@bp.route("/")
@login_required
def index():
    curr = current_user.is_anonymous
    return render_template('orders.html')
