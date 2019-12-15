from bottle import jinja2_template as template
from bottle import route, Bottle, request
from models import monster2

import logging
logging.basicConfig(level=logging.DEBUG)


app: Bottle = Bottle()

@app.route('/index')
@app.route('/result')
def index():
    """
    初期画面表示

    Returns
    ----------
    templateオブジェクト
    """
    return template('summon_index')

@app.route('/result', 'POST')
def battle():
    """
    モンスター同士の攻撃処理
    　処理結果を画面に返す

    Returns
    ----------
    templateオブジェクト
    """
    monster_name = request.forms.getunicode('name')
    summoned_monster = monster2.Monster(monster_name)
    params = {
        'name': summoned_monster.get_name(),
        'hp' : summoned_monster.get_hp(),
        'power' : summoned_monster.get_power(),
        'defence': summoned_monster.get_defence(),
        'attribute': summoned_monster.get_converted_attribute(),
    }
    return template('summon_result', params=params)