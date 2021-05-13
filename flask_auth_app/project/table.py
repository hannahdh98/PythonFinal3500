from flask_table import Table, Col, Linkcol


# Results class calling Table
class Results(Table):
    bhid = Col('bhid')
    date = Col('date')
    id = Col('id')
    comments = Col('comments')
    numeggspres = Col('numeggspres')
    alive = Col('alive')
    dead = Col('dead')
    activespecies = Col('activesprecies')
    other = Col('other')
    cowbird = Col('cowbird')
    repairs = Col('repairs')
    entryId = Col('entryId')


