def main():
    print("This program calulates overtime pay and total weekly wages")
    pay = float(input("What is your hourly rate of pay: "))
    hours = float(input("How many hours did you work during the week in question?: "))
    if hours <= 40:
        print("You've kept a good work/life balance. With no ovetime, your pay for the week is $", pay * hours)
    elif hours >40:
        print("You've been hard at work this week. Your wages are $", 40 * pay, "and your overtime pay is $", (hours - 40) * (pay * 1.5))
main()
