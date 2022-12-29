def div():
    try:
        n1=int(input())
        n2=int(input())
        n3=n1/n2
        print(n3)
    except ZeroDivisionError:
        print("divided by zero")
    except ValueError:
        print("value should be num")
div()

#############################################################
