from django.shortcuts import render, get_object_or_404

from .forms import CustomerCreateForm

from .models import Customer
# Create your views here.
def customer_detail_view(request, my_id):
	# obj = Customer.objects.get(id=my_id) # generates an exception if record not found...
	obj = get_object_or_404(Customer, id=my_id) # this does an proper error page
	context = {
		'object': obj	
	}
	return render(request, "customers/customer_detail.html", context)

def customer_create_view(request):
	form = CustomerCreateForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = CustomerCreateForm() # Resets the form

	context = {
		'form': form	
	}
	return render(request, "customers/customer_create.html", context)

def customer_list_view(request):
	queryset = Customer.objects.all()
	context = {
		'object_list': queryset	
	}
	return render(request, "customers/customer_list.html", context)

def customer_delete_view(request, my_id):
	obj = get_object_or_404(Customer, id=my_id)
	if request.method == "POST":
		# confirming delete
		obj.delete()
		return redirect('../../')
	context = {
		'object': obj	
	}
	return render(request, "customers/customer_delete.html", context)
