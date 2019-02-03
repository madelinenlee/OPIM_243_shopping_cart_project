#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:19:16 2019

@author: madeline
"""
import datetime

#copy-paste given output
products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50, "price_per": "item"},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99, "price_per": "item"},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49, "price_per": "item"},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99, "price_per": "item"},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99, "price_per": "item"},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99, "price_per": "item"},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50, "price_per": "item"},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25, "price_per": "item"},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50, "price_per": "item"},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99, "price_per": "item"},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99, "price_per": "item"},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50, "price_per": "item"},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00, "price_per": "item"},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99, "price_per": "item"},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50, "price_per": "item"},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50, "price_per": "item"},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99, "price_per": "pound"},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50, "price_per": "item"},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99, "price_per": "item"},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25, "price_per": "item"},
    {"id":21, "name": "Organic Bananas", "department": "produce", "aisle": "fruit", "price": 0.79, "price_per": "pound"}
    ]

def user_inputs(product_list):
    user_input = ''
    number_input = ''
    product_identifier_dict = {}

    while user_input != 'DONE':
        user_input = input('Please input a product identifier, or DONE if done: ')
        #check to see if list is done, if so, print identifiers
        if user_input == 'DONE':
            #product_identifier_list = list(set(product_identifier_list))
            return (product_identifier_dict)
        
        #check to see if it is a digit
        elif user_input.isdigit() and int(user_input) <= len(product_list):
            #while loop to check not out of range
            if product_list[int(user_input) - 1]['price_per'] == 'pound':
                number_input = input('How many pounds of ' + product_list[int(user_input) - 1]['name'] + '?: ')
            else:
                number_input = input('What quantity of ' + product_list[int(user_input) - 1]['name'] + '?: ')
            
            product_identifier_dict[int(user_input)] = number_input
            
        
        else:
            print('User input error: please enter a number between 1 and ' + 
                  str(len(product_list)))


    #product_identifier_list = list(set(product_identifier_list))
    '''print('These are the items in your cart: ')
    for item in product_identifier_list:
        print(product_list[item-1]['name'])
    remove_input = ''
    checkout = input('Would you like to check out? y/n: ')
    if checkout == 'n':
        action = input('Would you like to add or remove more items? a/r: ')
        if action == 'a':
            print('add item')
            #go back up to while loop
        elif action == 'r':
            while remove_input != 'DONE':
                remove_input = input('Please input a product identifier to DELETE, or DONE if done: ')
                
    if checkout == 'y':'''
    return (product_identifier_dict)


#test function
#product_identifier_dict = user_inputs(products)

def create_cost_dictionary(product_identifier_dict, tax_rate):
    cost_dictionary = {}
    subtotal = 0
    added_tax = 0
    total_cost = 0
    cost_dictionary['tax_rate'] = tax_rate
    for identifier in product_identifier_list:
        print(identifier)
        print(product_identifier_dict[identifier])
        subtotal = subtotal + (float(products[identifier-1]['price']) * product_identifier_dict[identifier])
        print(subtotal)
    cost_dictionary['subtotal'] = subtotal
    added_tax = round(subtotal * tax_rate,2)
    total_cost = round(subtotal+ added_tax, 2)
    cost_dictionary['added_tax'] = added_tax
    cost_dictionary['total_cost'] = total_cost
    
    return(cost_dictionary)
    
#test function 
#cost_dictionary = create_cost_dictionary(product_identifier_list, 0.0725)

def print_item_and_price(product_list, identifier):
    print('+ ' + product_list[identifier-1]['name'] + ' ($' + str('%0.2f' % product_list[identifier-1]['price']) + ')')
    

#test print item and price function
# print_item_and_price(products, 1)

def print_receipt(product_identifier_list, cost_dictionary):

    print('---------------------------------')
    print('Madeline Lee\'s Grocery Store (: ')
    print('---------------------------------')
    print('Web: github.com/madelinenlee/OPIM_243_shopping_cart_project')
    print('Phone: 123-456-5789')
    print('Checkout time: ', datetime.datetime.now())
    print('---------------------------------')
    print('Shopping Cart Items: ')
    for identifier in product_identifier_list:
        print_item_and_price(products, identifier)
    print('---------------------------------')
    print('Subtotal: $' + str('%0.2f' % cost_dictionary['subtotal']))
    print('Plus CA Sales Tax: $' + str('%0.2f' % cost_dictionary['added_tax']))
    print('Total: $' + str('%0.2f' % cost_dictionary['total_cost']))
    print('---------------------------------')
    print('Thank you for your business! Please come again.')
    
#test print_receipt function
# print_receipt([1, 3, 12], create_cost_dictionary([1, 3, 12], 0.0725))

def run_shopping_cart(product_list, tax_rate):
    product_identifier_list = user_inputs(product_list)
    cost_dictionary = create_cost_dictionary(product_identifier_list, tax_rate)
    print_receipt(product_identifier_list, cost_dictionary)

#test final function
#