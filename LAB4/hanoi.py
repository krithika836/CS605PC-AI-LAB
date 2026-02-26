def hanoi(n,start,target,aux):
  if n==1:
    print(f"Move disc 1 from {start} to {target}")
    return
  hanoi(n-1,start,aux,target)
  print(f"Move disc {n} from {start} to {target}")
  hanoi(n-1,aux,target,start)
hanoi(3,'A','C','B')

output
=====================================
Move disc 1 from A to C
Move disc 2 from A to B
Move disc 1 from C to B
Move disc 3 from A to C
Move disc 1 from B to A
Move disc 2 from B to C
Move disc 1 from A to C
