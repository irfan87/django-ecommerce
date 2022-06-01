# DJANGO E-COMMERCE

## Introduction
This is a simple e-commerce application that developed using Django, Python web framework. 

## Use Case
1. User can views the product.
2. User can views the details of the choosen product.
3. User can decide the quantity of the choosen product.
4. User can add the product to the cart.
5. Admin can add the new categories and products.
6. Admin can update the current category and product.
7. Admin can remove the old category and product.

## Specs
1. Python 3.10
2. Django 4.0.*
3. SQLite3

## Testing Libraries
1. Unittest that already provided by Python
2. Coverage for code coverage

## Usage
1. Aimply run `python -m venv env` and `env/Scripts/activate` to enable the modules
2. Run `pip -r requirements.txt` to install the packages
3. Run `py manage.py migrate` 
4. Run `py manage.py runserver` after migrate
5. All codes was test to check it's functionality and business needs. Feel free to check the availability of code coverage by running `coverage run manage.py test`