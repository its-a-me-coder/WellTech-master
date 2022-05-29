from lib2to3.pgen2.token import COLONEQUAL
from django.shortcuts import render
import pandas as pd
import plotly
from plotly.subplots import make_subplots
import plotly.express as px
from plotly.offline import plot
import plotly.graph_objects as go
imp_data=pd.read_csv('webapp/processed.csv')
# Create your views here.
import sqlite3
def country_view(request):
        graph1=px.histogram(imp_data, x='comp_no_empl',color='tech_flag',pattern_shape="tech_flag",category_orders=dict(comp_no_empl=['1-5', '6-25', '26-100', '100-500', '500-1000', '>1000']))
        graph=px.histogram(imp_data, x='country_live',color='tech_flag',pattern_shape="tech_flag")
        graph1.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        graph.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        plot_div = plot({'data': graph}, 
                        output_type='div')
        plot_div2 = plot({'data': graph1}, 
                        output_type='div')
        return render(request, 'mapp/chart-2.html', 
                    context={'plot_div': plot_div,'plot_div2': plot_div2})
def gender_view(request):
    all_techs = imp_data[imp_data['tech_flag'] == 1]['sex'].count()
    males = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['sex'] == 1.0)]['sex'].count()
    females = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['sex'] == 2.0)]['sex'].count()
    other = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['sex'] == 3.0)]['sex'].count()
    labels = 'Male', 'Female', 'Other'
    sizes = [males/all_techs, females/all_techs, other/all_techs]
    graph=px.pie(values=sizes,names=labels)
    graph1=px.histogram(imp_data, x=imp_data[imp_data['tech_flag'] == 1]['country_live'],color=imp_data[imp_data['tech_flag'] == 1]['sex'])
    graph1.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    graph.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)'},margin=dict(l=20, r=20, t=20, b=20))
        
    plot_div = plot({'data': graph}, 
                    output_type='div')
    plot_div2 = plot({'data': graph1}, 
                    output_type='div')
    return render(request, 'mapp/chart-2.html', 
                context={'plot_div': plot_div,'plot_div2': plot_div2})
def MHstatusNOW_view(request):
    all_techs_now = imp_data[imp_data['tech_flag'] == 1]['mh_disorder_current'].count()
    no_now = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_current'] == 'No')]['mh_disorder_current'].count()
    yes_now = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_current'] == 'Yes')]['mh_disorder_current'].count()
    maybe_now = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_current'] == 'Maybe')]['mh_disorder_current'].count()
    labels = 'No', 'Maybe', 'Yes'
    sizes = [no_now/all_techs_now, maybe_now/all_techs_now,yes_now/all_techs_now]
    graph=px.pie(values=sizes,names=labels)
    graph1=px.histogram(imp_data,x=imp_data[imp_data['tech_flag'] == 1]['country_live'],color=imp_data[imp_data['tech_flag'] == 1]['mh_disorder_current'])
    graph1.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    graph.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        
    plot_div = plot({'data': graph}, 
                    output_type='div')
    plot_div2 = plot({'data': graph1}, 
                    output_type='div')
    return render(request, 'mapp/chart-2.html', 
                context={'plot_div': plot_div,'plot_div2': plot_div2})
def MHstatusPAST_view(request):
    all_techs_past = imp_data[imp_data['tech_flag'] == 1]['mh_disorder_current'].count()
    no_past = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_past'] == 'No')]['mh_disorder_past'].count()
    yes_past = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_past'] == 'Yes')]['mh_disorder_past'].count()
    maybe_past = imp_data[(imp_data['tech_flag'] == 1) & (imp_data['mh_disorder_past'] == 'Maybe')]['mh_disorder_past'].count()
    labels = 'No', 'Maybe', 'Yes'
    sizes = [no_past/all_techs_past,maybe_past/all_techs_past, yes_past/all_techs_past]
    graph=px.pie(values=sizes,names=labels)
    graph1=px.histogram(imp_data,x=imp_data[imp_data['tech_flag'] == 1]['country_live'],color=imp_data[imp_data['tech_flag'] == 1]['mh_disorder_past'])
    graph1.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    graph.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
        
    plot_div = plot({'data': graph}, 
                    output_type='div')
    plot_div2 = plot({'data': graph1}, 
                    output_type='div')
    return render(request, 'mapp/chart-2.html', 
                context={'plot_div': plot_div,'plot_div2': plot_div2})
def home_view(request):
    return render(request, 'employer/home.html')
def stat_view(request):
    return render(request, 'employer/home.html')
def index(request):
    return render(request, 'index.html')
def employer(request):
    conn = sqlite3.connect(r'C:\Users\Souri\OneDrive\Desktop\WellTech-master\survey.db') 
    cursor = conn.cursor()
    all_info = '''SELECT * from processed order by rowid DESC'''
    cursor.execute(all_info)
    result = cursor.fetchone()
    parameters = ''' SELECT  self_empl_flag,tech_comp_flag,sex from processed order by rowid DESC'''
    cursor.execute(parameters)
    p = cursor.fetchone()
    pstr = list(p)
    resultstr = list(result)
    cursor.execute(''' SELECT  rowid,* from processed WHERE self_empl_flag=? AND tech_comp_flag=? AND sex=?''',(pstr[0],pstr[1],pstr[2]))
    lst= cursor.fetchall()
    lst=str(lst)
    lst = lst.replace('(','[')
    lst = lst.replace(')',']')
    print(lst)
    return render(request, 'result.html',{'data': resultstr,'all': lst})
def result(request):
    conn = sqlite3.connect(r'C:\Users\Souri\OneDrive\Desktop\WellTech-master\depression.db') 
    cursor = conn.cursor()
    all_info = '''SELECT * from short_survey order by rowid DESC'''
    cursor.execute(all_info)
    lst = cursor.fetchone()
    lst = list(lst)
    sum_depressed=0
    sum_anxiety=0
    string_depressed_0='''Based on your responses to questions 1-8, you do not show any sign of depression and seem mentally well. If in case you do feel like you need to have some kind of professional help do seek out for people.'''
    string_depressed_1='''Based on your responses to questions 1-8, you are experiencing some symptoms seen in depression but only an experienced health professional can tell for sure. You should make an appointment to see your therapist or if not assigned you should assign one'''
    string_depressed_2='''Based on your responses to questions 1-8, you are experiencing many symptoms seen in depression but only an experienced health professional can tell for sure. You should make an appointment to see your therapist or seek professional help'''
    string_anxiety_1='''Based on your responses to questions 10-16, you are experiencing some symptoms seen in anxiety. This is probably having a slight impact on your daily life. Make an appointment with your therapist or seek professional help.'''
    string_anxiety_2='''Based on your responses to questions 10-16, you are experiencing many symptoms seen in anxiety. This is probably having a big impact on your daily life and you may also be experiencing physical symptoms. Make an appointment with your therapist or seek professional help.'''
    string_anxiety_0='''Based on your responses to questions 10-16, you are experiencing very few symptoms seen in anxiety. If in case you do feel like you need to have some kind of professional help do seek out for people.'''
    for i in lst[0:9]:
        sum_depressed = sum_depressed + i
    for i in lst[9:]:
        sum_anxiety = sum_anxiety + i
    print(sum_depressed)
    print(sum_anxiety)
    if sum_depressed<=6:
        str_dep=string_depressed_0
    elif sum_depressed>6 and sum_depressed<=18:
        str_dep=string_depressed_1
    if sum_depressed>18:
        str_dep=string_depressed_2
    if sum_anxiety<=6:
        str_anx=string_anxiety_0
    elif sum_anxiety>6 and sum_anxiety<=18:
        str_anx=string_anxiety_1
    if sum_anxiety>18:
        str_anx=string_anxiety_2
    return render(request, 'result.html',{'dep': sum_depressed,'anx': sum_anxiety,'str_dep': str_dep,'str_anx': str_anx})
def chatbot(request):
    return render(request, 'chatbot.html')
def faq(request):
    return render(request, 'faq.html')
def blog(request):
    return render(request, 'blog.html')
def adminview(request):
    return render(request, 'admin.html')

