import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__),'../lib'))
from transwarp import db

def test_connection():
    db.create_engein(user='root', password='111111', database='test',
        host='127.0.0.1', port=3306)