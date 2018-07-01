from flask import render_template
from . import main
from ..models import Bloopers

# Error handler decorator
@main.app_errorhandler(404)
def four_Ow_four(error):
    '''
    Function to render the 404 error page
    '''
    title = '404 page'
    return render_template('fourOwfour.html', title=title,bloopers=Bloopers.getrandom()),404
