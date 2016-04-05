from flask import Blueprint, render_template

editor_blueprint = Blueprint('editor', __name__)

@editor_blueprint.route('/editor')
def editor():
    return render_template('editor/index.html')