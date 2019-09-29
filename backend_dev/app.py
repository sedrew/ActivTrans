#!flask/bin/python
from flask import (
                    Flask, 
                    jsonify, 
                    abort, 
                    make_response, 
                    request
                   )
import datetime

now = datetime.datetime.now()

print(now.day,now.month,now.year,sep=".")

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Первый городской благотворительный фестиваль “ДОБРЫЙ ИЖЕВСК”',
        'description': u'''8 июня в Парке им. Кирова прошёл Первый городской благотворительный фестиваль “ДОБРЫЙ ИЖЕВСК” — праздник для горожан, где каждый смог сделать доброе дело, узнал больше о благотворительности, городских НКО и адресах помощи.''', 
        'body': 'Первым таким фестивалем в России стал «Добрый Питер» @dobrypiter в 2006 году. Сегодня «Добрые города» — это содружество более 100 добрых городов России. Каждый из членов содружества проводит благотворительные городские фестивали для жителей и вместе с жителями. Фестиваль «ДОБРЫЙ ИЖЕВСК» инициирован и организован активистами некоммерческих организаций города с целью продвижения идеи благотворительности и привлечения жителей города к добрым делам. На фестивале приняли участие более 20 крупных некоммерческих организаций города Ижевска. В программе Фестиваля были представлены: Площадка добрых дел: сбор книг, одежды, кормов для животных. Активные площадки: мастер-классы, квесты, конкурсы. Концерт «День Доброго Ижевска». Флэш-моб «Поющий Ижевск» с песней «Ижевск — цветущий город». Фестиваль прошел душевно, задорно и весело! В небе грело солнышко, а в сердцах жителей любовь и доброта. Фонд «ДОБРО» выступил одним из организаторов Фестиваля и вложил душу и сердце своих сотрудников для того, чтобы ДОБРЫЙ ИЖЕВСК полюбился горожанам и стал хорошей доброй традицией для города Ижевска.',
        'data': '09.06.2019',
        'done': False,
        'tag': ['city','life'],
        'img': ['https://dobrodobro.ru/wp-content/uploads/2019/06/cHG4eETV0F8-768x1024.jpg','https://dobrodobro.ru/wp-content/uploads/2019/06/D_yMjmlHwlQ-1-1024x683.jpg','https://dobrodobro.ru/wp-content/uploads/2019/06/75-Jl-eAkU4-768x1024.jpg'],
        'previe' : '',
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False,
        'data': '09.06.2019',
        'tag': ['city','life',],
        'img': []
    },
    {
        'id': 3,
        'title': 'tyu6ut',
        'description': 'ewrewr', 
        'done': False,
        'data': '09.06.2019',
        'tag': ['city','today'],
        'img': []
    }
]

tag_get = ["city","life","today"]


@app.route('/tasks', methods=['GET'])
def get_tasks():
    print(tasks[0]['title'])
    return jsonify({'tasks': tasks})
 
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = list(filter(lambda t: t['id'] == task_id, tasks))
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

tag_list = []
@app.route('/tasks/tag/<string:tag>', methods=['GET'])
def get_tag(tag):
    tag_list.clear()
    for tg in tasks:
        for i in tg['tag']:
            if i == tag:
               print(i)
               tag_list.append(tg)
            elif i == "":
                 abort(404)
    return jsonify({'tasks': tag_list})
    # task = list(filter(lambda t: t['id'] == task_id, tasks))
    # if len(task) == 0:
        # abort(404)
    # return jsonify({'task': task[0]})


@app.route('/tasks/<string:tags>', methods=['GET'])
def get_tag_list(tags):
    if not tags == "tag":
       abort(404)
    return jsonify({'tags': tag_get})
    
@app.route('/tasks', methods=['POST'])
def create_task():
    print(request.json)
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False,
        'tag': request.json['tag'],
        'data': str(now.day)+"."+str(now.month)+"."+str(now.year),
        #'img': request.json['img' or []]
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
    
@app.route('/echo', methods=['POST'])
def echo():
    return jsonify(request.get_json(force=True))
    
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
 
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0') #10.70.10.216
    