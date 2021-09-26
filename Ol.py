import requests
import json


token='බොට් api එම්ක'
method='sendMessage'

def get_data(index_no):
    try:
        r=requests.get('https://result.doenets.lk/result/service/OlResult?index='+str(index_no)+'&nic=')
        jsondata = json.loads(r.text)
        if jsondata['examination']==None:
            print(str(index_no)+' is not valid')
        else:
            exam=str(jsondata['examination'])
            ye=str(jsondata['year'])
            na=str(jsondata['name'])
            index=str(jsondata['indexNo'])
            nic=str(jsondata['nic'])
            Sub1name=jsondata['subjectResults'][0]['subjectName']
            Sub1result=jsondata['subjectResults'][0]['subjectResult']
            Sub2name=jsondata['subjectResults'][1]['subjectName']
            Sub2result=jsondata['subjectResults'][1]['subjectResult']
            Sub3name=jsondata['subjectResults'][2]['subjectName']
            Sub3result=jsondata['subjectResults'][2]['subjectResult']
            Sub4name=jsondata['subjectResults'][3]['subjectName']
            Sub4result=jsondata['subjectResults'][3]['subjectResult']
            Sub5name=jsondata['subjectResults'][4]['subjectName']
            Sub5result=jsondata['subjectResults'][4]['subjectResult']
            Sub6name=jsondata['subjectResults'][5]['subjectName']
            Sub6result=jsondata['subjectResults'][5]['subjectResult']
            Sub7name=jsondata['subjectResults'][6]['subjectName']
            Sub7result=jsondata['subjectResults'][6]['subjectResult']
            Sub8name=jsondata['subjectResults'][7]['subjectName']
            Sub8result=jsondata['subjectResults'][7]['subjectResult']
            Sub9name=jsondata['subjectResults'][8]['subjectName']
            Sub9result=jsondata['subjectResults'][8]['subjectResult']
            ex=('Exam')
            namee=('Name')
            year=('Year')
            idd=('Index No')
            ni=('Nic No')


            print(ex)
            print(namee)
            print(year)
            print(idd)
            print(ni)
            print(exam)
            print(ye)
            print(na)
            print(index)
            print(nic)
            print(Sub1name)
            print(Sub1result)
            print(Sub2name)
            print(Sub2result)
            print(Sub3name)
            print(Sub3result)
            print(Sub4name)
            print(Sub4result)
            print(Sub5name)
            print(Sub5result)
            print(Sub6name)
            print(Sub6result)
            print(Sub7name)
            print(Sub7result)
            print(Sub8name)
            print(Sub8result)
            print(Sub9name)
            print(Sub9result)

            msg=ex+' 👉 '+exam+'\n'+namee+' 👉 '+na+'\n'+year+' 👉 '+ye+'\n'+idd+' 👉 '+index+'\n'+ni+' 👉 '+nic+'\n'+Sub1name+' 👉 '+Sub1result+'\n'+Sub2name+' 👉 '+Sub2result+'\n'+Sub3name+' 👉 '+Sub3result+'\n'+Sub4name+' 👉 '+Sub4result+'\n'+Sub5name+' 👉 '+Sub5result+'\n'+Sub6name+' 👉 '+Sub6result+'\n'+Sub7name+' 👉 '+Sub7result+'\n'+Sub8name+' 👉 '+Sub8result+'\n'+Sub9name+' 👉 '+Sub9result

            response = requests.post(
            url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
            data={'chat_id':-චැනල් id එම්ක, 'text': msg}
            ).json() 
    except:
        print('err')
for i in range(10000000,99999999):
    get_data(i)

response = requests.post(
    url='https://api.telegram.org/bot{0}/{1}'.format(token, method),
    data={'chat_id':-චැනල් id එම්ක, 'text': 'Done start again'}
    ).json()
