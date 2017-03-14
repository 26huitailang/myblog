# coding: utf-8
from flask import Flask, render_template, render_template_string
from . import app

user = {'id': 123, 'nickname': '< IAMKING>'}
tpl1 = '<h1>homepage of <a href="/user/{{id}}">{{nickname | e}}</a></h1>'
# 递归循环，遍历friend_circle的friends
tpl2 = '''
    <ul>
        {% for item in friend_circle recursive %}
        <li>
            {{ item }}
            <ul>{{ loop(item.friends) }}</ul>
        </li>
        {% endfor %}
    </ul>
    '''
tpl3 = '''
    <ul>
        {% for item in contacts %}
        {% if loop.index % 2 == 0 %}
        <li class="even-row">{{ item }}</li>
        {% else %}
        <li class="odd-row">{{ item }}</li>
        {% endif %}
        {% endfor %}
    </ul>
    '''

contacts = [
    {'name': 'linda', 'tel': '897123'},
    {'name': 'mary', 'tel': '1928739'},
    {'name': 'jack', 'tel': '9872314'},
    {'name': 'tommy', 'tel': '9081233'},
    {'name': 'jimi', 'tel': '5091234'},
    {'name': 'obama', 'tel': '8782012'}
]

friend_circle = [{
    'name': 'zhang3',
    'friends': [
        {
            'name': 'li4',
            'friends': [
                {'name': 'wang5'},
                {'name': 'zhao6'}
            ]
        },
        {
            'name': 'lin7',
            'friends': [
                {'name': 'wu8'},
                {'name': 'he9'}
            ]
        }
    ]
}]



@app.route('/string')
def v_index():
    return render_template_string(tpl3, contacts=contacts)


@app.route('/')
def index():
    return render_template('table.html', contacts=contacts)


if __name__ == '__main__':
    app.run('0.0.0.0', port=8000, debug=True)
