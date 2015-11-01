#! /usr/bin/python2
from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_appconfig import AppConfig
from flask_wtf import Form, RecaptchaField
from flask_wtf.file import FileField
from wtforms import TextField, HiddenField, ValidationError, RadioField,\
    BooleanField, SubmitField, IntegerField, FormField, validators
from wtforms.validators import Required
import pygal
import pygal.style as ps
import lxml.html as lxh
from urllib import unquote
from HTMLParser import HTMLParser as hp



# straight from the wtforms docs:
class TelephoneForm(Form):
    country_code = IntegerField('Country Code', [validators.required()])
    area_code = IntegerField('Area Code/Exchange', [validators.required()])
    number = TextField('Number')


class ExampleForm(Form):
    field1 = TextField('First Field', description='This is field one.')
    field2 = TextField('Second Field', description='This is field two.',
                       validators=[Required()])
    hidden_field = HiddenField('You cannot see this', description='Nope')
    recaptcha = RecaptchaField('A sample recaptcha field')
    radio_field = RadioField('This is a radio field', choices=[
        ('head_radio', 'Head radio'),
        ('radio_76fm', "Radio '76 FM"),
        ('lips_106', 'Lips 106'),
        ('wctr', 'WCTR'),
    ])
    checkbox_field = BooleanField('This is a checkbox',
                                  description='Checkboxes can be tricky.')

    # subforms
    mobile_phone = FormField(TelephoneForm)

    # you can change the label as well
    office_phone = FormField(TelephoneForm, label='Your office phone')

    ff = FileField('Sample upload')

    submit_button = SubmitField('Submit Form')


    def validate_hidden_field(form, field):
        raise ValidationError('Always wrong')


def generate_graph():
    custom_style = ps.Style(
     background='transparent',
     plot_background='white',
     foreground='#53E89B',
     foreground_light='white',
     foreground_dark='white',
     opacity='.6',
     opacity_hover='.9',
     transition='400ms ease-in',
     colors=('green', '#E8537A', '#E95355', '#E87653', '#E89B53'))

    barchart = pygal.Bar(show_legend=False, human_readable=True, rounded_bars=20, style=custom_style)
    barchart.add("", [1,2,3])
    barchart.value_formatter = lambda _: ""
    barchart.x_labels = ("Nutrients", "Water", "Ph")
    return unquote(hp().unescape(lxh.tostring(barchart.render_tree())))

def create_app(configfile=None):
    app = Flask(__name__)
    AppConfig(app, configfile)  # Flask-Appconfig is not necessary, but
                                # highly recommend =)
                                # https://github.com/mbr/flask-appconfig
    Bootstrap(app)

    # in a real app, these should be configured through Flask-Appconfig
    app.config['SECRET_KEY'] = 'devkey'
    app.config['RECAPTCHA_PUBLIC_KEY'] = \
        '6Lfol9cSAAAAADAkodaYl9wvQCwBMr3qGR_PPHcw'

    @app.route('/', methods=('GET', 'POST'))
    def index():
        form = ExampleForm()
        form.validate_on_submit()  # to get error messages to the browser
        #flash('critical message', 'critical')
        #flash('error message', 'error')
        #flash('warning message', 'warning')
        # Your garden <name>
        # What do your water levels look like?
        flash('Deltacademy', 'info')
        # you need to add <amount> of water
        # you will need to add water in <n> days
        # your garden has enough water right now
        #flash('debug message', 'debug')
        #flash('different message', 'different')
        #flash('uncategorized message')
        return render_template('test2.html', form=form)

    return app

if __name__ == '__main__':
    create_app().run(debug=True)
