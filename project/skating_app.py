from http import client
import pymongo
from flask import Flask,request,jsonify


client = pymongo.MongoClient("mongodb+srv://gayathri:Sairambaba@cluster1.davwpcs.mongodb.net/?retryWrites=true&w=majority")
mydata=client['mydatabase']
skating_student_collection = mydata['skating_student']

app = Flask(__name__)

@app.route('/view',methods=['get'])
def view_student():
    try:
        
        curser = []
        for x in skating_student_collection.find({},{ "_id": 0}):
            curser.append(x)   
        return {"data":curser}

    except Exception as e:
        print("Error on updating :" +str(e))

@app.route('/add',methods=['post'])
def add_student():
    try:
        val=request.get_json()
        skating_student_collection.insert_many(val)

        return "Added successfully"

    except Exception as e:
        print("error accures :" +str(e))
        return "failed to add"

@app.route('/update',methods=['put'])
def update_student():
    try:

        val2=request.get_json()
        val=request.args.get('title')

        skating_student_collection.update_many({'title':val},{"$set":val2})
        return "successfully updated"       

    except Exception as e:
        print("Error on updating :" +str(e))
        return "failed on updating"

@app.route('/delete',methods=['get','delete'])
def delete_student():
    try:
        val=request.get_json('_id')
        curser=skating_student_collection.find()
        for i in curser:
            if i['_id']==val:
                skating_student_collection.delete_one(i)
        
        
        return "successfully deleted"

    except Exception as e:
        print("Error on updating :" +str(e))

@app.route('/dropall',methods=['delete'])
def dropall():
    try:
        skating_student_collection.drop()
        return "Files erased successfully"

    except Exception as e:
        print("error", +str(e))


if __name__=='__main__':
   app.run(debug=True)
