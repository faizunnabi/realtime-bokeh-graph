import pandas as pd
from datetime import datetime
import random
from bokeh.plotting import figure,output_file,show,curdoc,ColumnDataSource

def getColor(d):
	color=''
	if 8>d>5:
		color='yellow'
	elif d>8:
		color='red'
	elif d<5:
		color='green'
	return color
	
source=ColumnDataSource({'x':[datetime.now()],'y':[random.random()*10],'color':['green']})
p=figure(plot_width=800,plot_height=600,x_axis_type='datetime')
p.circle(source=source,x='x',y='y',size=10,alpha=0.5,color='color')

def update():
        cld=random.random()*10
        clr=getColor(cld)
        new_source={'x':[datetime.now()],'y':[cld],'color':[clr]}
        source.stream(new_source)
    
curdoc().add_root(p)
curdoc().add_periodic_callback(update,1000)
