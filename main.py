from re import A
from flask import Flask, render_template, request, redirect
import common.json_operations as json_utils
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods =['POST','GET'])
def index():
    if request.method == 'POST':
        task_content=request.form['content']
        data=add_new_json(task_content)
        print(data)
        return render_template('index.html', tasks=data)
    else:
        data=json_utils.read_json("data/task.json")

        return render_template('index.html', tasks=data['Task_list'])

@app.route('/delete/<int:id>')
def delete(id):
    try:
        json_utils.delete_data("data/task.json",id)
        return redirect ("/")
    except:
        return print("There is a problem deleting the task")

@app.route('/update/<int:id>')
def update(id):
    try:
        json_utils.update_data("data/task.json",id)
        return redirect ("/")
    except:
        return print("There is a problem updating the task")

def add_new_json(input):
    data_json=json_utils.read_json("data/task.json")
    try:
        if(data_json['Task_list'][0]):
            size_of_task = len(data_json['Task_list'])
            index=size_of_task+1
    except:
        index=1
    task_id=index
    task_description = input
    task_details = "Open"
    task_time =  datetime.utcnow()

    task_dict={
        "id":task_id,
        "task_description":task_description,
        "task_details": task_details,
        "task_time":str(task_time)
    }
    data_json['Task_list'].append(task_dict)
    json_utils.write_json("data/task.json",data_json)
    return data_json['Task_list']

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")

