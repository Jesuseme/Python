#main function so enable the program repeat after completion
def main():
    
    #the function to make the calculation
    def circle_area(b):
        return 3.1428571429 * (b*b)
 
 
    print("-----------------------------------------")
    print("Area of circle calculator: ")
    print("Enter circle radius:")
    
    #this enables user input
    z = int( input())
    
    #input is added to the function
    z = circle_area(z)
    print ("Area: " + str(z))
    print("-----------------------------------------")
    
    #the main function is called to restart the program
    main()


main()
