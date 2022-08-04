from unittest import TestCase, mock
from urllib import response
from project import skating_app
from flask import Flask,json



def test_view_student():
    response = skating_app.app.test_client().get('/view')

    assert response.status_code == 200

def test_add():        
    response = skating_app.app.test_client().post('/add',
        data=json.dumps(
            {
            "DOB": "03/12/1995",
            "Name": "legend",
            "skating Type": "inline"
            }
            ),
        content_type='application/json',
    )
    assert response.status_code == 200
    

def test_update():        
    response = skating_app.app.test_client().put('/update')
    assert response.status_code == 200
    
def test_delete():        
    response = skating_app.app.test_client().delete('/delete',
        data=json.dumps(
            {
            "DOB": "03/12/1995",
            "Name": "legend",
            "skating Type": "inline"
            }
            ),
        content_type='application/json',
    )
    assert response.status_code == 200
    