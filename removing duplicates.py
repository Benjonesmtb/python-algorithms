#-------------------------------------------------------------------------------
# Name:        removing duplicates
# Purpose:
#
# Author:      pa8jones
#
# Created:     03/02/2022
# Copyright:   (c) pa8jones 2022
# Licence:     <your licence>
#-------------------------------------------------------------------------------

new_menu = ['Hawaiian', 'Margherita', 'Mushroom', 'Prosciutto', 'Meat Feast', 'Hawaiian', 'Bacon', 'Black Olive Special', 'Sausage', 'Sausage']

final_new_menu = list(dict.fromkeys(new_menu))

print(final_new_menu)