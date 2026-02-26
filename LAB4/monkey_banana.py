def monkey_banana():
  print("Give the positions")
  monkey=input("Enter monkey position: ")
  box=input("Enter box position: ")
  banana=input("Enter banana position: ")
  state={"monkey" : monkey,"box" : box,"banana" : banana}
  print("Initial state: ",state)
  state["monkey"]=state["box"]
  state["box"]=state["banana"]
  state["monkey"]=state["banana"]
  print("Goal Achieved: ",state)
monkey_banana()



output
============================================================

Give the positions
Enter monkey position: door
Enter box position: window
Enter banana position: center
Initial state:  {'monkey': 'door', 'box': 'window', 'banana': 'center'}
Goal Achieved:  {'monkey': 'center', 'box': 'center', 'banana': 'center'}
