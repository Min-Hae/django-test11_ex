from django.shortcuts import render
from myapp.models import Jikwon, Buser
import json
from django.http.response import HttpResponse
# Create your views here.
def MainFunc(request):
    return render(request, 'main.html')

def ListFunc(request):
    jik = request.GET['searchKey']
    print(jik)
    sdata = Jikwon.objects.filter(jikwon_jik = jik)
    
    datas = []
    
    for s in sdata:
        buser = Buser.objects.get(buser_no = s.buser_num)
        dic = {'jikwon_no':s.jikwon_no, 'jikwon_name':s.jikwon_name, 'buser_name':buser.buser_name}
        datas.append(dic)
        
    print(datas)
    return HttpResponse(json.dumps(datas), content_type="application/json")