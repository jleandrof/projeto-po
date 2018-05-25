from easygui import *
import sys
import simplex

while 1:

    # Misc messages
    cont = "Do you wish to continue?"

    # Source A
    src_msg_a = "Source A Information"
    title = "Transportation Department"
    fieldNames = ["Supply", "Destinaion 1 Cost","Destinaion 2 Cost", "Destinaion 3 Cost"]
    src_1 = []  # we start with blanks for the values
    src_1 = multenterbox(src_msg_a, title, fieldNames)
    if not all(src_1):
        msgbox("Invalid Input")
        continue
    src_1_supply = src_1.pop(0)

    # Source B
    src_msg_b = "Source B Information"
    src_2 = []
    src_2 = multenterbox(src_msg_b,title, fieldNames)
    if not all(src_2):
        msgbox("Invalid Input")
        continue
    src_2_supply = src_2.pop(0)

    # Demand info
    dmd_msg = "Demand Information"
    demand_info_fn = ["Destination 1 Demand", "Destination 2 Demand", "Destination 3 Demand"]
    demand_info = []
    demand_info = multenterbox(dmd_msg, title, demand_info_fn)
    if not all(demand_info):
        msgbox("Invalid Input")
        continue
    
    obj_func = src_1 + src_2
    
    result = simplex.simplex(obj_func,
                             [src_1_supply, src_2_supply] + demand_info)

    A1 = result.x[0]
    A2 = result.x[1]
    A3 = result.x[2]
    B1 = result.x[3]
    B2 = result.x[4]
    B3 = result.x[5]
    
    msgbox("Total Cost: " + str(-1 * result.fun) +
           "\n" + "From Source A to Destination 1: " + str(A1) +
           "\n" + "From Source A to Destination 2: " + str(A2) +
           "\n" + "From Source A to Destination 3: " + str(A3) +
           "\n" + "From Source B to Destination 1: " + str(B1) +
           "\n" + "From Source B to Destination 2: " + str(B2) +
           "\n" + "From Source B to Destination 3: " + str(B3) +
           "\n" + "Objective Function: Z = " +
           str(-1*obj_func[0]) + "*X1 + " +
           str(-1*obj_func[1]) + "*X2 + " +
           str(-1*obj_func[2]) + "*X3 + " +
           str(-1*obj_func[3]) + "*X4 + " +
           str(-1*obj_func[4]) + "*X5 + " +
           str(-1*obj_func[5]) + "*X6")
    msgbox(str(result))
    
    if ccbox(cont, title):     # show a Continue/Cancel dialog
        pass
    else:
        sys.exit(0)
