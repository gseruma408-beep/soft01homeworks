gender = input("Enter gender(male, female): ")
hemoglobin = float (input("Enter hemoglobin: "))
if gender == "female":
 if hemoglobin < 117:
        print('hemoglobin is too low')
 elif 117 <= hemoglobin <= 155:
        print('hemoglobin is normal')
 else:
    print('hemoglobin is too high')

if gender == "male":
 if hemoglobin < 135:
        print('hemoglobin is too low')
 elif 135 <= hemoglobin <= 167:
        print('hemoglobin is normal')
 else:
    print('hemoglobin is too high')
