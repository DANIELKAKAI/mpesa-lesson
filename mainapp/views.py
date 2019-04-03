from django.shortcuts import render
from django.http import HttpResponse
from mpesa.b2c import transaction
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.


def index(request):
	if request.method=='POST':
		name= request.POST.get('name')
		phone = request.POST.get('phone')
		phone = '254'+phone[-9:]
		message = transaction(phone,name)
		return render(request,"index.html",{'message':message})
	result_code = request.session.get('result_code')
	print(result_code)
	return render(request,"index.html",{'result_code':result_code})


@csrf_exempt
def mpesa_callback(request):
	print(request.POST) #gives nothing
	body = json.loads(request.body.decode('utf-8'))
	print(body)
	result_code = body['Body']['stkCallback']['ResultCode']
	request.session['result_code'] = result_code
	print(result_code)
	return HttpResponse('callback')