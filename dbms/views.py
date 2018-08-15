from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import user, Event, Participant, Registration, Slot_list
# Create your views here.

def home(request):
	return render(request, 'dbms/index.html', {})

def check(request):

	if 'certify' in request.POST:
		rno = request.POST['rno']
		result = Registration.objects.filter(receipt_no__receipt_no=rno,reported=True,certificate=False)
		stat = 1
		return render(request, 'dbms/report.html', {'pend_events':result,'status':stat})
	else:
		rno = request.POST['rno']
		result = Registration.objects.filter(receipt_no__receipt_no=rno,reported=False)
		return render(request, 'dbms/report.html', {'pend_events':result})

def update(request,pk):
	obj = Registration.objects.get(pk=pk)
	obj.reported = True
	obj.save()
	messages.success(request, obj.receipt_no.name + " reported succesfully for " + obj.event.event_name)
	return HttpResponseRedirect('/')

def award(request,pk):
	obj = Registration.objects.get(pk=pk)
	obj.certificate = True
	obj.save()
	messages.success(request, obj.receipt_no.name + " given certificate for " + obj.event.event_name)
	return HttpResponseRedirect('/certify/')

def certify(request):
	return render(request, 'dbms/certify.html')

def chosevent(request):
	evelist = Event.objects.all()
	slotlist = Slot_list.objects.all()
	return render(request, 'dbms/list.html', {'ename':evelist,'slotlist':slotlist})

def event(request):
	ename = request.POST.get('ename',False)
	slot = request.POST.get('slot',False)
	if slot=="all":
		result1 = Registration.objects.filter(event__event_name=ename,reported=True,certificate=False).order_by('receipt_no__receipt_no')
	else:
		result1 = Registration.objects.filter(event__event_name=ename,slot_no__slot_no=slot,reported=True,certificate=False).order_by('receipt_no__receipt_no')
	return render(request, 'dbms/eventlist.html', {'p_list':result1})
