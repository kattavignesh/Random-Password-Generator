#####################################################
__author__ = "VIGNESH"
__copyright__ = "Copyright (C) 2024 Author Vignesh"
__license__ = "Public"
__version__ = "1.0"
#####################################################

#############
import random
#############

passlength = int(input("enter the length of password:"))
keyword ="abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
pswd = "".join(random.sample(keyword,passlength ))
print(("Strongest Password: "),pswd)
