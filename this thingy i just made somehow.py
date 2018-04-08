while True:


        grandTotal = int(input('     Moving-in expenses  '))

        print(' ')

        if grandTotal <= 100000:
                grandTotal = 100

        elif grandTotal <= 120000 and grandTotal >=100001:
                grandTotal = 90

        elif grandTotal <= 140000 and grandTotal >=120001:
                grandTotal = 80

        elif grandTotal <= 160000 and grandTotal >=140001:
                grandTotal = 70

        elif grandTotal <= 180000 and grandTotal >=160000:
                grandTotal = 60

        elif grandTotal <= 200000 and grandTotal >=180000:
                grandTotal = 50

        elif grandTotal <= 220000 and grandTotal >=200000:
                grandTotal = 40

        elif grandTotal <= 240000 and grandTotal >=220000:
                grandTotal = 30

        elif grandTotal <= 260000 and grandTotal >=240000:
                grandTotal = 20

        elif grandTotal <= 270000 and grandTotal >=260000:
                grandTotal = 10

        else:
                print('This apartment does not qualify for rent.')
                break


        price = int(input('     Monthly Rent  '))

        print(' ')

        if price <= 50000:
                price = 100

        elif price <= 55000:
                price = 90

        elif price <= 57000:
                price = 80

        elif price <= 59000:
                price = 70

        elif price <= 61000:
                price = 60

        elif price <= 63000:
                price = 50

        elif price <= 65000:
                price = 40

        elif price <= 67000:
                price = 30

        elif price <= 69000:
                price = 20

        elif price <= 71000:
                price = 10
        
        else:
                print('This apartment does not qualify for rent.')
                break

        sqMeters = int(input('     Room Size  '))

        print(' ')

        if sqMeters >= 50:
                sqMeters = 100

        elif sqMeters >= 47 and sqMeters <= 49:
                sqMeters = 90

        elif sqMeters >= 44 and sqMeters <= 46:
                sqMeters = 80

        elif sqMeters >= 41 and sqMeters <= 43:
                sqMeters = 70

        elif sqMeters >= 38 and sqMeters <= 40:
                sqMeters = 60

        elif sqMeters >= 35 and sqMeters <= 37:
                sqMeters = 50

        elif sqMeters >= 32 and sqMeters <= 34:
                sqMeters = 40

        elif sqMeters >= 29 and sqMeters <= 31:
                sqMeters = 30

        elif sqMeters >= 26 and sqMeters <= 28:
                sqMeters = 20

        elif sqMeters >= 23 and sqMeters <= 25:
                sqMeters = 10

        else:
                print('This apartment does not qualify for rent.')
                break


        dtStation = int(input('     Distance to station  '))

        print(' ')

        if dtStation == 1:
                dtStation = 100

        elif dtStation == 2:
                dtStation = 90

        elif dtStation == 3:
                dtStation = 80

        elif dtStation == 4:
                dtStation = 70

        elif dtStation == 5:
                dtStation = 60

        elif dtStation == 6:
                dtStation = 50

        elif dtStation == 7:
                dtStation = 40

        elif dtStation == 8:
                dtStation = 30

        elif dtStation == 9:
                dtStation = 20

        elif dtStation == 10:
                dtStation = 10

        else:
                print('This apartment does not qualify for rent.')
                break

        dtSchool = int(input('     Distance to school  '))

        print(' ')

        if dtSchool <= 30:
                dtSchool = 100

        elif dtSchool <= 32 and dtSchool >= 31:
                dtSchool = 90

        elif dtSchool <= 34 and dtSchool >= 33:
                dtSchool = 80

        elif dtSchool <= 36 and dtSchool >= 35:
                dtSchool = 70

        elif dtSchool <= 38 and dtSchool >= 37:
                dtSchool = 60

        elif dtSchool <= 40 and dtSchool >= 39:
                dtSchool = 50

        elif dtSchool <= 42 and dtSchool >= 41:
                dtSchool = 40

        elif dtSchool <= 44 and dtSchool >= 43:
                dtSchool = 30

        elif dtSchool <= 46 and dtSchool >= 45:
                dtSchool = 20

        elif dtSchool <= 48 and dtSchool >= 47:
                dtSchool = 10

        elif dtSchool <= 55 and dtSchool >= 49:
                dtSchool = 5

        else:
                print('This apartment does not qualify for rent.')
                break

        elevator = input('     Elevator?  ')

        print(' ')

        if elevator == 'Yes':
                elevator = 50

        elif elevator == 'No': 
                elevator = 0

        score = grandTotal + price + sqMeters + dtStation + dtSchool



        print('   Score: ' + str(score))
        print(' ')
        print(' ')
        print(' ')
