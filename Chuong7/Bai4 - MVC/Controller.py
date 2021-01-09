from Model import Car

import View
def showAll():
   Car_in_db = Car.get_All_Car()
   View.showAllView(Car_in_db)

def start():
   choice = View.startView()
   if choice == 'y':
      showAll()
   else:
      View.endView()
if __name__ == "__main__":
   start()