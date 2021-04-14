'''
Pair programming project
by Paco Hung
3/3/2021
'''


def income():
    try:
        global h, w, seperate, joint
        h = float(input("Your personal income: "))
        if not h >= 0:
            print("Non-negative numbers only...")
            h = float(input("Your personal income: "))

        w = float(input("Spouse's personal income: "))
        if not h >= 0:
            print("Non-negative numbers only...")
            w = float(input("Spouse's personal income: "))
        seperate = ' no data'
        joint = ' no data'
    except:
        print("Please input a number...")
        income()


def tax(type, x, y):
    global xtax, xstandard, xmpf, xflag

    if type == 'seperate':
        if x*0.05 <= 18000:
            xmpf = x*0.05
        else:
            xmpf = 18000

        xnet = max(0, x-xmpf-132000)

    elif type == 'joint':
        if x*0.05 <= 18000:
            xmpf = x*0.05
        else:
            xmpf = 18000

        if y*0.05 <= 18000:
            ympf = y*0.05
        else:
            ympf = 18000

        x = x+y

        xmpf = xmpf+ympf

        xnet = max(0, x-xmpf-264000)

    xstandard = (x-xmpf)*0.15

    xtax = 0

    if (xnet-50000) >= 0:
        xtax += 50000*0.02
        xnet -= 50000
        if (xnet-50000) >= 0:
            xtax += 50000*0.06
            xnet -= 50000
            if (xnet-50000) >= 0:
                xtax += 50000*0.1
                xnet -= 50000
                if (xnet-50000) >= 0:
                    xtax += 50000*0.14
                    xnet -= 50000
                    xtax += xnet*0.17
                    xnet = 0
                else:
                    xtax += xnet*0.14
                    xnet = 0
            else:
                xtax += xnet*0.1
                xnet = 0
        else:
            xtax += xnet*0.06
            xnet = 0
    else:
        xtax += xnet*0.02
        xnet = 0

    if xtax <= xstandard:
        xflag = 0
    elif xtax > xstandard:
        xflag = 1
        xtax = xstandard

    xtax = int(xtax)

    return xmpf, xtax, xflag


def menu():
    print(
        '''
====================================================================
--------------------- Hong Kong Tax Calculator ---------------------
====================================================================
╔════════════════════════════════════════════╗
    Current data:                  
    Your income = HK${}/year  
    Spouse's income = HK${}/year

    Seperate assessment = HK${}
    Joint assessment = HK${}
╚════════════════════════════════════════════╝                               

[1] Seperate

[2] Joint

[3] Recommend

[4] Re-enter

[0] Exit program
        '''
        .format(h, w, seperate, joint)
    )


if __name__ == '__main__':
    try:
        print("Welcome! To begin, please enter the following...\n")
        income()
        menu()
        select = int(input("Selection: "))

        while select != 0:
            if select == 1:
                seperate = 0

                tax('seperate', h, 0)

                print("-----------------------------------------------")

                print("Your MPF deduction: HK${}".format(xmpf))

                if xflag == 1:
                    print("Your tax payable: HK${} (At standard rate)".format(xtax))
                else:
                    print("Your tax payable: HK${}".format(xtax))

                seperate += xtax

                tax('seperate', w, 0)

                print("\n")

                print("Spouse's MPF deduction: HK${}".format(xmpf))

                if xflag == 1:
                    print("Spouse's tax payable: HK${} (At standard rate)".format(xtax))
                else:
                    print("Spouse's tax payable: HK${}".format(xtax))

                seperate += xtax

                print("\n")

                print("Combined seperate tax payable: HK${}".format(seperate))

                input("Press Enter to return to the menu...")

            elif select == 2:
                joint = 0

                tax('joint', h, w)

                joint += xtax

                print("-----------------------------------------------")

                print("Total MPF deduction: HK${}".format(xmpf))

                if xflag == 1:
                    print("Joint tax payable: HK${} (At standard rate)".format(xtax))
                else:
                    print("Joint tax payable: HK${}".format(xtax))

                input("Press Enter to return to the menu...")

            elif select == 3:
                if type(seperate) == str or type(joint) == str:
                    print("Please calculate both seperate and joint assessments first")
                else:
                    print("Seperate assessment = HK${}".format(seperate))
                    print("Joint assessment = HK${}".format(joint))
                    
                    if seperate < joint:
                        print("It is recommended that you select seperate assessment")
                    elif joint < seperate:
                        print("It is recommended that you select joint assessment")
                    else:
                        print("Both assessment methods are equal")

                input("Press Enter to return to the menu...")

            elif select == 4:
                income()
                input("Press Enter to return to the menu...")

            elif select == 0:
                break
            else:
                print("Invalid input")

            menu()
            select = int(input("Selection: "))

        print("Goodbye!")

    except Exception as e:
        print("Fatal error: ")
        print(e)
