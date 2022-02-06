#-------------------------------------------------------------------------------
# Name:        removing duplicates
# Purpose:
#
# Author:      Ben Jones
#
# Created:     03/02/2022
# Copyright:   (c) Ben Jones 2022
#-------------------------------------------------------------------------------

new_menu = ['Hawaiian', 'Margherita', 'Mushroom', 'Prosciutto', 'Meat Feast', 'Hawaiian', 'Bacon', 'Black Olive Special', 'Sausage', 'Sausage']

final_new_menu = list(dict.fromkeys(new_menu))

print(final_new_menu)
