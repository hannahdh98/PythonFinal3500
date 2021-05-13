from wtforms import Form, StringField, DateField, IntegerField, SelectField, TextAreaField, HiddenField, SubmitField


# New entry from Drop down entries: birdhouse
class NewEntry(Form):
    house_num = [('1', '1'),
                 ('2', '2'),
                 ('3', '3'),
                 ('4', '4'),
                 ('5', '5'),
                 ('6', '6'),
                 ('7', '7'),
                 ('8', '8'),
                 ('9', '9'),
                 ('10', '10'),
                 ('11', '11'),
                 ('12', '12'),
                 ('13', '13')]

    # New entry from Drop down entries: active species
    species_typ = [('Eastern Blue Bird', 'Eastern Blue Bird'),
                   ('Tree Swallow', 'Tree Swallow'),
                   ('House Wren', 'House Wren'),
                   ('Brown-Headed Cowbird', 'Brown-Headed Cowbird'),
                   ('Unknown', 'Unknown'),
                   ('other', 'other')]
    # New entry from Drop down entries: cowbird present
    cowbird_sel = [('yes', 'yes'),
                   ('no', 'no')]
    # New entry from Drop down entries: yes or no
    repairs_sel = [('yes', 'yes'),
                   ('no', 'no')]
    # New entry from Drop down entries: bird house id 1-13
    bhid = SelectField('bhid', choices=house_num)
    date = DateField('date', format='%m-%d-%Y')
    id = IntegerField('id')
    comments = TextAreaField('comments')
    numeggspres = IntegerField('numeggspres')
    alive = IntegerField('alive')
    dead = IntegerField('dead')
    # New entry from Drop down entries: active species
    activespecies = SelectField('activespecies', choices=species_typ)
    # New entry from Drop down entries: yes or no
    cowbird = SelectField('cowbird', choices=cowbird_sel)
    # New entry from Drop down entries: yes or no
    repairs = SelectField('repairs', choices=repairs_sel)
    other = TextAreaField('other')
    entryId = HiddenField('entryId')
    submit = SubmitField('submit')


# EditEntry Form
class EditEntryForm(Form):
    bhid = SelectField('bhid')
    date = DateField('date', format='%m-%d-%Y')
    id = IntegerField('id')
    comments = TextAreaField('comments')
    numeggspres = IntegerField('numeggspres')
    alive = IntegerField('alive')
    dead = IntegerField('dead')
    activespecies = SelectField('activespecies')
    cowbird = SelectField('cowbird')
    repairs = TextAreaField('repairs')
    other = TextAreaField('other')
    entryId = HiddenField('entryId')
    submit = SubmitField('submit')
