import csv, sys , os
import django

project_dir = "/home/phil/dev/jungle/src"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE'] = 'jungle.settings'
django.setup()

from customers.models import Customer 
with open('customers.csv') as f:
	reader = csv.reader(f)
	for row in reader:
		print ('importing ', row[0], '(', row[1], ')')
		cust = Customer()
		cust.name 	= row[1]
		cust.phone	= row[2]
		cust.address = row[3]
		cust.city 	= row[4]
		cust.county  = row[5]
		cust.county  = row[5]
		cust.postcode= row[6]
		cust.country = 'UK'
		cust.notes	= row[7]
		# cust.active	= row[9]
		cust.save()
