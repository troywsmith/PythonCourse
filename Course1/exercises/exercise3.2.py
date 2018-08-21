hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")

try: 
  fh = float(hrs)
  fr = float(rate)
except:
  print("Error, please enter a numeric input.")
  quit()

if fh <= 40:
  pay = fh * fr
else:
  overtimeHours = fh - 40
  overtimeRate = fr * 1.5
  pay = (40 * fr) + (overtimeHours * overtimeRate)

print('Pay: ', pay)