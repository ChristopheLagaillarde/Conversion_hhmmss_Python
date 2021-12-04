try:
    def conversion_unite_sup(unite_temps):
        unite_temps_sup = 0

        while unite_temps >= 60:
            unite_temps_sup += 1
            unite_temps = unite_temps - 60

        return unite_temps, unite_temps_sup

    def formate(unite_temps):
        if len(str(unite_temps)) < 2:
            unite_temps = str("0") + str(unite_temps)
        return unite_temps

    ss = int(0)
    mm = int(0)
    hh = int(0)

    while 0 >= ss or ss >= 86400:
        ss = int(input("Saisir le nombre de seconde"))

    ss, mm = conversion_unite_sup(ss)
    mm, hh = conversion_unite_sup(mm)

    hh = formate(hh)
    mm = formate(mm)
    ss = formate(ss)

    hh_mm_ss = str(hh) + ":" + str(mm) + ":" + str(ss)

    print(hh_mm_ss)

except ValueError:
    print("Saisie non valide")