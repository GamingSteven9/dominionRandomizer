# Gets the selected expansions from the checkboxes
def getExpansions(chk_vars):
    selected_Expansions = [var.get() for var in chk_vars]
    #print(selected_Expansions)
    return selected_Expansions