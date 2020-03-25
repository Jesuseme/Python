def main():
    def circle_area(b):
        return 3.1428571429 * (b*b)
 
 
    print("-----------------------------------------")
    print("Area of circle calculator: ")
    print("Enter circle radius:")
    z = int( input())
    z = circle_area(z)
    print ("Area: " + str(z))
    print("-----------------------------------------")
    main()


main()