first_entrance_height = int(input())
second_entrance_height = int(input())
third_entrance_height = int(input())
floor = int(input())

shift = 0
if floor <= first_entrance_height:
    print(3*floor-2+shift, 3*floor-1+shift, 3*floor+shift, sep="\n")
shift += first_entrance_height*3
if floor <= second_entrance_height:
    print(3*floor-2+shift, 3*floor-1+shift, 3*floor+shift, sep="\n")
shift += second_entrance_height*3
if floor <= third_entrance_height:
    print(3*floor-2+shift, 3*floor-1+shift, 3*floor+shift, sep="\n")
