from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response

app = Flask(__name__)


def cities_import() 