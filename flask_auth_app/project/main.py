from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user
from .forms import NewEntry
from .models import Entries
from . import db
from .forms import EditEntryForm


main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


#profile call
@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


# new entry
@main.route('/entry.html', methods=['GET', 'POST'])
@login_required
def entry():
    form = NewEntry(request.form)
    if request.method == 'POST' and form.validate():
        entry = Entries()
        save_changes(entry, form, new=True)
        flash('entry successful')
        return redirect(url_for('main.tables'))
    return render_template('entry.html', form=form)

# saved the changes from entry
@main.route('/entry.html', methods=['GET', 'POST'])
@login_required
def save_changes(entry, form, new=False):
    entry.bhid = form.bhid.data
    entry.date = form.date.data
    entry.comments = form.comments.data
    entry.numeggspres = form.numeggspres.data
    entry.alive = form.alive.data
    entry.dead = form.dead.data
    entry.activespecies = form.activespecies.data
    entry.cowbird = form.cowbird.data
    entry.repairs = form.repairs.data
    entry.id = form.id.data
    entry.other = form.other.data
# commits the entry
    if new:
        db.session.add(entry)
        db.session.commit()
        return render_template('tables.html')


#recententry call
@main.route('/recententry')
@login_required
def recententry():
    return render_template('recententry.html')


#main call
@main.route('/help')
@login_required
def helpuser():
    return render_template('helpuser.html')


#graphs call
@main.route('/graphs')
@login_required
def graph():
    return render_template('graph.html')


#makes the login required for the tables, sets results to entries and table = results
@main.route('/tables', methods=['GET', 'POST'])
@login_required
def tables():
    entryTable = Entries.query.all()
    table = entryTable
    return render_template('tables.html', table=table)

#deletes the entry
@main.route('/<int:entryId>/delete_entry', methods=['GET', 'POST'])
@login_required
def delete_entry(entryId):
    entry = Entries.query.get(entryId)
    Entries.query.filter(Entries.entryId == entryId).delete()
    db.session.commit()
    flash('successfully deleted')
    return redirect(url_for('main.tables'))

#edits the entry
@main.route('/<int:entryId>/edit_entry', methods=['GET', 'POST'])
@login_required
def editEntry(entryId):
    entry = Entries.query.get(entryId)
    form = EditEntryForm(obj=entry)
    if request.method == "POST":
        bhid = request.form.get('bhid')
        date = request.form.get('date')
        id = request.form.get('id')
        comments = request.form.get('comments')
        activespecies = request.form.get('activespecies')
        alive = request.form.get('alive')
        dead = request.form.get('dead')
        repairs = request.form.get('repairs')
        entryId = request.form.get('entryId')
        numeggspres = request.form.get('numeggspres')
        cowbird = request.form.get('cowbird')

# assigns new data to the old data
        entry.bhid = bhid
        entry.date = date
        entry.id = id
        entry.comments = comments
        entry.activespecies = activespecies
        entry.alive = alive
        entry.dead = dead
        entry.repairs = repairs
        entry.numeggspres = numeggspres
        entry.cowbird = cowbird

        # commit
        db.session.commit()
        flash('entry added successfully')
        return redirect(url_for('main.tables'))
    return render_template('edit-entry.html', title='Edit Entry', form=form, entry=entry)



