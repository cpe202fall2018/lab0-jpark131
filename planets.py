def weight_on_planets():
   print("What do you weigh on earth? ")
   Earthweight = input()
   print("On Mars you would weigh " + str(0.38 * int(Earthweight)) + " pounds.")
   print("On Jupiter you would weigh " + str(2.34 * int(Earthweight)) + " pounds.")
   
   
if __name__ == '__main__':
   weight_on_planets()
