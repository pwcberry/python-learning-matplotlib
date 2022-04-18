from calendar import monthrange
from datetime import datetime
from pandas import to_datetime

def get_x_range(start, end):
    y1, m1 = start
    y2, m2 = end
    _, days = monthrange(y2, m2)
    return to_datetime(datetime(y1, m1, 1)), to_datetime(datetime(y2, m2, days))

def draw_date_span(ax, color, start, end):
    x1, x2 = get_x_range(start, end)
    ax.axvspan(x1, x2, facecolor=color)

def draw_la_nina_spans(ax):
    draw_date_span(ax, "#D8F8FC", (2000, 1), (2001, 3))
    draw_date_span(ax, "#D8F8FC", (2007, 6), (2008, 2))
    draw_date_span(ax, "#D8F8FC", (2008, 8), (2009, 4))
    draw_date_span(ax, "#D8F8FC", (2010, 4), (2012, 3))
    draw_date_span(ax, "#D8F8FC", (2021, 11), (2022, 3))

def draw_el_nino_spans(ax):
    draw_date_span(ax, "#FCE0C8", (2002, 3), (2003, 1))
    draw_date_span(ax, "#FCE0C8", (2006, 5), (2007, 1))
    draw_date_span(ax, "#FCE0C8", (2009, 5), (2010, 3))
    draw_date_span(ax, "#FCE0C8", (2015, 4), (2016, 4))
