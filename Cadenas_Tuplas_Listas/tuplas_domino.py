def encajar_domino(fichauno, fichados):
    #Recibe dos fichas de domino e indica si encajan.
    for element in fichauno:
        if element in fichados:
            return True
    return False



