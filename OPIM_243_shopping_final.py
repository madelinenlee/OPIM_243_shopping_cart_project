#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 14:19:16 2019

@author: madeline
"""
import datetime

#------------------------------------------------------------------------------
#                           Product Inventory Lists (Given)
#------------------------------------------------------------------------------

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

#------------------------------------------------------------------------------
#                       Products Inventory List (Barcode, Given)
#------------------------------------------------------------------------------

#ids are strings instead of numbers, must accomodate input exception handling to that
barcode_products = [
    {"id": "99482452704", "name": "Organic Black Beans", "price": 0.99, 'price_per': 'item'},
    {"id": "99482434182", "name": "Organic Almonds Roasted Unsalted", "price": 7.33, 'price_per': 'pound'},
    {"id": "99482418939", "name": "Jug of Spring Water", "price": 0.99, 'price_per': 'item'},
    {"id": "898248001107", "name": "Siggi's Strawberry Yogurt", "price": 1.45, 'price_per': 'item'},
    {"id": "898248001114", "name": "Siggi's Peach Yogurt", "price": 1.45, 'price_per': 'item'},
    {"id": "290295004269", "name": "Whole Foods Guacamole - Small", "price": 6.50, 'price_per': 'item'},
    {"id": "012000161155", "name": "LIFE Water", "price": 2.15, 'price_per': 'item'}
    ]

#------------------------------------------------------------------------------
#                           User Inputs Function
#------------------------------------------------------------------------------
#function to put user inputs of identifiers in a dictionary (according to 
#quantity and if applicable, per lb)

def user_inputs(product_list):
    
    #note - couldnt figure out a faster, less bulky way to do this ... runtime is long ):
    
    identifier_dict = {} #initialize identifier dict to store index, identifier
    for i in range(0, len(product_list)):
        identifier_dict[i] = str(product_list[i]['id']) #populate list for exception handling later
    #print(identifier_dict)  
    user_input = '' #initialize variables
    number_input = '' #initialize variables
    product_identifier_dict = {}

    while user_input != 'DONE': #if 'DONE', then list should not append 'DONE'
        user_input = str(input('Please input a product identifier, or DONE if done: '))
        
        #check to see if list is done, if so, print identifiers
        if user_input == 'DONE':
            #product_identifier_list = list(set(product_identifier_list))
            return (product_identifier_dict)
        
       
        elif user_input in identifier_dict.values():
            #print(user_input in identifier_dict.values())
            #while loop to check the identifier exists in the system
            index = list(identifier_dict.keys())[list(identifier_dict.values()).index(user_input)]
            #print(index)
            if product_list[index]['price_per'] == 'pound':
                #if per lb, input how many
                number_input = input('How many pounds of ' + product_list[index]['name'] + '?: ')
                    
            else:
                #not per lb, per item - input quantity
                number_input = input('What quantity of ' + product_list[index]['name'] + '?: ')
            
            #populate dictionary
            product_identifier_dict[user_input] = number_input
            
        
        else:
            #error checking
            print('User input error: please enter a valid product identifier number...')


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
    #returns dictionary
    return (product_identifier_dict)


#test function
#product_identifier_dict = user_inputs(barcode_products)

#------------------------------------------------------------------------------
#                           Cost Dictionary Function
#------------------------------------------------------------------------------

#function to create a cost dictionary with necessary information for receipt
#subtotal, tax rate, added tax, and total cost are all keys
#takes input cart contents, and desired tax rate

def create_cost_dictionary(product_list, product_identifier_dict, tax_rate):
    #initialize variables
    cost_dictionary = {}
    subtotal = 0
    added_tax = 0
    total_cost = 0
    
    identifier_dict = {} #initialize identifier dict to store index, identifier
    for i in range(0, len(product_list)):
        identifier_dict[i] = str(product_list[i]['id'])
        
    
    #add tax rate to dict
    cost_dictionary['tax_rate'] = tax_rate
    
    #calculate subtotals (rounding each time)
    for key in product_identifier_dict:
        index = list(identifier_dict.keys())[list(identifier_dict.values()).index(key)]
        #print(index)
        #print(product_identifier_dict[key])
        subtotal = subtotal + (float(product_list[index]['price']) * float(product_identifier_dict[key]))
        subtotal = round(subtotal, 2)
        #print(subtotal)
    
    #populate dictionary, round variables to the nearest cent (2 decimal places)
    cost_dictionary['subtotal'] = subtotal
    added_tax = round(subtotal * tax_rate,2)
    total_cost = round(subtotal+ added_tax, 2)
    cost_dictionary['added_tax'] = added_tax
    cost_dictionary['total_cost'] = total_cost
    
    #return finished dictionary
    return(cost_dictionary)
    
#test function 
#cost_dictionary = create_cost_dictionary(barcode_products, product_identifier_dict, 0.0725)

#------------------------------------------------------------------------------
#                       Print Formatting Function
#------------------------------------------------------------------------------

#function to properly print out an item, its quantity, and the resulting subtotal
#takes inputs from inventory system, the customer's shopping cart, and the 
#specific identifier

    
def print_item_and_price(product_list, product_identifier_dict, identifier):
    
    #note - couldnt figure out a faster, less bulky way to do this ... runtime is theoretically long ):
    
    for i in range(0, len(product_list)):
        if str(product_list[i]['id']) == identifier:
            if product_list[i]['price_per'] == 'item':
                return('+ ' + str(product_identifier_dict[identifier]) + ' ' +
                      product_list[i]['name'] + ' at $' + str('%0.2f' % product_list[i]['price']) + ' each ($' +
                      str('%0.2f' % round(float(product_list[i]['price'] *
                                  float(product_identifier_dict[identifier])),2)) + ')')
            elif product_list[i]['price_per'] == 'pound':
                return('+ ' + str(product_identifier_dict[identifier]) + ' lbs ' +
                      product_list[i]['name'] + ' at $' +
                      str('%0.2f'% product_list[i]['price']) + '/lb ($' +
                      str('%0.2f' % round(float(product_list[i]['price'] *
                                  float(product_identifier_dict[identifier])),2) ) + ')')        
    

#test print item and price function
#print_item_and_price(barcode_products, product_identifier_dict, '99482434182')
             
#------------------------------------------------------------------------------
#                       Print Receipt Function
#------------------------------------------------------------------------------

#function to write receipt to a text file, to a folder in the same directory as script, named 'Receipts'
#has timestamp when the file is created
#inputs - product list, customer cart items, subtotals

def write_receipt(product_list, product_identifier_dict, cost_dictionary):

    with open('Receipts/' + datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')+'.txt', 'w') as text_file:
        text_file.write('---------------------------------\n')
        text_file.write('Madeline Lee\'s Grocery Store (: \n')
        text_file.write('---------------------------------\n')
        text_file.write('Web: github.com/madelinenlee/OPIM_243_shopping_cart_project\n')
        text_file.write('Phone: 123-456-5789\n')
        text_file.write('Checkout time: ' + str(datetime.datetime.now()) + '\n')
        text_file.write('---------------------------------')
        text_file.write('Shopping Cart Items: \n')
        for key in product_identifier_dict:
            temp_string = print_item_and_price(product_list, product_identifier_dict, str(key))
            text_file.write(temp_string + '\n')
        text_file.write('---------------------------------\n')
        text_file.write('Subtotal: $' + str('%0.2f' % cost_dictionary['subtotal']) + '\n')
        text_file.write('Plus Sales Tax at ' + str(cost_dictionary['tax_rate']) + '%: $' + str('%0.2f' % cost_dictionary['added_tax']) + '\n')
        text_file.write('Total: $' + str('%0.2f' % cost_dictionary['total_cost']) + '\n')
        text_file.write('---------------------------------\n')
        text_file.write('Thank you for your business! Please come again.\n')
    
    #text_file.close()
    
    
#test print_receipt function
# write_receipt(barcode_products, product_identifier_dict, cost_dictionary)

#------------------------------------------------------------------------------
#                           Automation Function
#------------------------------------------------------------------------------

#function to run all functions in order
#takes input products list and desired tax rate

def run_shopping_cart(product_list, tax_rate):
    product_identifier_dict = user_inputs(product_list)
    cost_dictionary = create_cost_dictionary(product_list, product_identifier_dict, tax_rate)
    write_receipt(product_list, product_identifier_dict, cost_dictionary)

#test final function
#if you wanted to try running on the original product list, change 'barcode_products'
#to 'products'
    
run_shopping_cart(barcode_products, 0.0725)
#run_shopping_cart(products, 0,0725)