from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse

from .models import Employee, Transfer, Giftcard

from django.http import HttpResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User 
from django.db import connection

def my_sql(self):
    with connection.cursor() as cursor:
        cursor.execute("SELECT username FROM rewards_employee e,auth_user a  WHERE e.user_em_id = a.id and points_remain > 0", )
        row = cursor.fetchone()

    return row
 
  
@login_required
def showinfo(request):
	employee = Employee.objects.get(user_em_id = request.user.id)
	username = request.user.username
	points_remain = employee.points_remain
	points_received = employee.points_received
	
	return render(request, 'rewards/index.html',{'username':username, 'points_remain':points_remain, 'points_received':points_received})

@login_required
def transfer(request):

    giver = Employee.objects.get(user_em_id = request.user.id)
    
    em_list = [i.username for i in User.objects.all()]
    em_list.remove(request.user.username)
    em_list.remove('admin')


    if request.method =="POST":

    	receiver = Employee.objects.get(user_em = User.objects.get(username=request.POST['receiver']).id)

    	points_given = int(request.POST['points_given'])
    	
    	message = request.POST['message']
    	try:
    		#giver's points_remain less
    		giver.points_remain -= points_given
    		giver.save()
    		#receiver's points_received more
    		receiver.points_received += points_given
    		receiver.save()
    		#Transfer + one more entry
    		q = Transfer(giver = giver, receiver=receiver, points_given=points_given,message=message,give_date=timezone.now())
    		q.save()


    	except:
    		pass
    	return redirect('/rewards/transfer/?done=True') 
    elif request.method == "GET":
    	try:
    		done=request.GET['done']
    		print(done)
    	except:
    		pass
    	return render(request, 'rewards/transfer.html', {'z': em_list })


@login_required
def redeem(request):
	this_employee = Employee.objects.get(user_em_id = request.user.id)
	points_received = this_employee.points_received
	dollars= sum([i.amount for i in Giftcard.objects.filter(employee=this_employee)])

	# When user submit form:
	if request.method=="POST":
		try:
			# Employee的object的attribute里减少对应的points
			point_redeemed = request.POST['redeem_amount']
			this_employee.points_received -= int(point_redeemed)
			this_employee.save()
			# Giftcard表里加一个数据,add an object
			a = int(point_redeemed) // 100
			q = Giftcard(amount=a, redeem_date = timezone.now(), employee = Employee.objects.get(user_em_id = request.user.id))
			q.save()

		except:
			pass	

		# return空的页面
		return redirect('/rewards/redeem/?done=True')

	# When user just open the page:
	elif request.method=="GET":
		try:
			done=request.GET['done']
			print(done)
		except:
			pass
		return render(request, 'rewards/redeem.html',{'points_received':points_received, 'dollars':dollars})



		

