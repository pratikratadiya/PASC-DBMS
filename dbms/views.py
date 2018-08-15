from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ParticipantForm, RegistrationForm
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
	if slot=="repall":
		result1 = Registration.objects.filter(event__event_name=ename,reported=True,certificate=False).order_by('receipt_no__receipt_no')
	elif slot=="all":
		result1 = Registration.objects.filter(event__event_name=ename).order_by('receipt_no__receipt_no')
	else:
		result1 = Registration.objects.filter(event__event_name=ename,slot_no__slot_no=slot,reported=True,certificate=False).order_by('receipt_no__receipt_no')
	return render(request, 'dbms/eventlist.html', {'p_list':result1})

def newparticipant(request):
	if request.method == 'POST':
		form = ParticipantForm(request.POST)
		if form.is_valid():
			a = form.save()
			ename = request.POST.get('ename',False)
			slot = request.POST.get('slot',False)			
			post = Registration()
			post.receipt_no = a
			b = Event.objects.get(event_name=ename)
			post.event = b
			c = Slot_list.objects.get(slot_no=slot)
			post.slot_no = c
			if ('team').checked in request.POST:
				post.is_team = True
			post.save()
			messages.success(request, "Registration done succesfully")
			return HttpResponseRedirect('/newparticipant/')
		else:
			evelist = Event.objects.all()
			slotlist = Slot_list.objects.all()
			return render(request, 'dbms/addparticipant.html', {'ename':evelist,'slotlist':slotlist,'form':form})
	else:
		form = ParticipantForm()
		evelist = Event.objects.all()
		slotlist = Slot_list.objects.all()
		return render(request, 'dbms/addparticipant.html', {'ename':evelist,'slotlist':slotlist,'form':form})

def existing(request):
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid:
			a = form.save(commit=False)
			rno = request.POST.get('rno',False)
			participant = Participant.objects.get(receipt_no=rno)
			a.receipt_no = participant
			if 'team' in request.POST:
				a.is_team = True			
			a.save()
			messages.success(request, "Registration done succesfully")
			return HttpResponseRedirect('/newparticipant/')			
	else:
		form = RegistrationForm()
		return render(request, 'dbms/addexisting.html', {'form':form})