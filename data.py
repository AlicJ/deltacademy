#! /usr/bin/python2

import pygal

from pygal.style import *

# education / literacy
# post-secoNoney degrees
got_degrees = [43.4, 46.0, 47.8, 46.2, 46.0, 49.4, 50.2, 51.8, 49.5, 50.6, 50.8, 51.4, 51.7, 53.9, 53.4]
didnt_get = [100-n for n in got_degrees]

ps_years = ["20%02d" % n for n in xrange(0,15)]
years = ["2000", "2005", "2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013"]

bar_chart = pygal.StackedBar(style=LightGreenStyle)
bar_chart.x_labels = ps_years
bar_chart.add("post-secondary degrees", got_degrees)
bar_chart.add("no post-secondary degrees", didnt_get)
bar_chart.render_to_file("post_secondary.svg")

# library use

library_circulation = [[year, None] for year, n in zip(years, xrange(0,10))]
libuse = [
        ("Sudbury",    [7.78, 7.11, 7.32, 7.60, None, None, None, None, None, None]),
        ("Toronto",    [10.64, 12.07, 12.15, 11.56, 10.88, 11.35, 11.66, 11.92, 11.48, 11.60]),
        ("Missisauga", [10.50, 10.33, 10.39, 10.62, 11.03, 11.28, 10.37, 10.47, 9.85, 8.79]),
        ("Newmarket",  [6.84, 5.72, 5.51, 5.09, None, None, None, None, None, None]),
        ("Oakville",   [10.10, 13.69, 13.06, 12.41, 12.32, 12.99, 12.44, 12.03, 11.65, 11.38]),
        ("Pickering",  [None, 11.20, 11.54, 12.43, 12.25, 13.03, None, None, None, None])]

for i in xrange(0, 10):
    for city, lib in libuse:
        if lib[i] is not None:
            if library_circulation[i][1] is not None:
                library_circulation[i][1] = (library_circulation[i][1] + lib[i]) / 2
            else:
                library_circulation[i][1] = lib[i]

bar_chart = pygal.StackedBar(style=LightGreenStyle)
bar_chart.x_labels = years
bar_chart.add("Library Circulation per capita", [l[1] for l in library_circulation])
bar_chart.render_to_file("libraries.svg")

smokers = [23.2, 25.2, 21.4, 21.1, 21.6, 20.0, 21.5, 23.8, 18.2]
smoker_years = ["2005", "2007", "2008", "2009", "2010", "2011", "2012", "2013", "2014"]

bar_chart = pygal.StackedBar(style=LightGreenStyle)
bar_chart.x_labels = smoker_years
bar_chart.add("Smoking Rates per year (percentage)", smokers)
bar_chart.render_to_file("smoking.svg")

earnings = [31800, 21200, 25500, 32700, 32700, 48600]
levels = ["All levels", "No diploma", "High school", "Trades", "College", "University"]

bar_chart = pygal.StackedBar(style=LightGreenStyle)
bar_chart.x_labels = levels
bar_chart.add("Earnings by education", earnings)
bar_chart.render_to_file("income_education.svg")
