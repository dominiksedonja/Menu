#!/usr/bin/env python
# -*- coding: utf-8 -*-

menu = {}

while True:
    food = raw_input("Enter today's menu: ")
    price = float(raw_input("Please enter price of today's menu in EUR: "))

    menu[food] = price

    addMenu = raw_input("Is there one more menu (yes/no)? ")

    if addMenu.lower() == "no":
        print "Ok see you soon - bye"
        break
    elif addMenu.lower() == "yes":
        continue
    else:
        while (addMenu.lower() != "yes") or (addMenu.lower() != "no"):
            addMenu = raw_input("Is there one more menu (yes/no)? ")
            if addMenu.lower() == "yes":
                break
            elif addMenu.lower() == "no":
                print "Ok see you soon - bye"
                break
        if addMenu.lower() == "no":
            break

menuFile = open("menu.txt", "w+")

max_width = max(len(food) for food in menu)
a = ""
menuFile.write("Today's menu %s Price: \n" % (format(a).ljust(max_width - 4)))
menuFile.write("\n")

for food in menu:
    menuFile.write("%s%s EUR \n" % (format(food).ljust(max_width + 10), menu[food]))

