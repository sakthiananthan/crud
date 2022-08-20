import json

def read_json(file):
    jf=open(file)
    read_jf=jf.read()
    jf.close()
    json_data=json.loads(read_jf)
    return json_data

def write_json(file,data):
    jw=open(file,"w")
    write_jf = json.dumps(data, indent=4)
    jw.write(write_jf)

def delete_data(file,id):
    print(file,id)
    json_data=read_json(file)
    is_deleted=False
    for data in json_data['Task_list']:
        if(data['id']==id):
            json_data['Task_list'].remove(data)
            is_deleted=True
    if (is_deleted):
        for no in range(len(json_data['Task_list'])):
            json_data['Task_list'][no]['id']=no+1
    write_json(file,json_data)

def update_data(file,id):
    print(file,id)
    json_data=read_json(file)
    for data in json_data['Task_list']:
        if(data['id']==id):
            data['task_details'] = 'Done'
    write_json(file,json_data)


