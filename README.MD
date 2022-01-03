This is a marketplace where vendors can sell their items and buy from each other!
to have this website working locally on your machine you must have python3 installed and added to your environment variables

open cmd then type
	
	pip install virtualenv
	virtualenv env
	env\Scripts\activate
	cd marketplace
	pip install -r requirements.txt
	python manage.py runserver

then the website should be working fine on your localhost port 8000.