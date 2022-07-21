
'''
    Name :- Mohit Jaiswal
    Batch :- G1
    Roll no. :- 705 
'''

import pandas as pd
import numpy as nmp                        #importing required modules
import matplotlib.pyplot as plt
import plotly.express as px


print("\n\n------------------------------------------SMART WATCH ANALYSIS------------------------------------------------\n\n")

brand_data = pd.read_excel('D:\\brands.xlsx')            #reading data sheet of smart watch brands

print("Smart Watch Brands in India -->\n")
print(brand_data.to_string(index=False))                #printing data sheet of smart watch brands

while True : 

    print("\n")
    choice = int(input("Enter the brand :- "))

    print("\n---------------------------------------------------------------------------------------------------------------")

    if choice==1 :

        apple_data = pd.read_excel('D:\\apple.xlsx')            #reading data of apple watch
            
        print("\nApple Smart Watch -->\n")
        print(apple_data.to_string(index=False))                #printing data of apple watch

        print("\n1.Scatter Analysis\n2.Bar Analysis")
        analysis = int(input("\nEnter the value :- "))
        
        if analysis==1 :
            apple_data.plot(kind = 'scatter', x = 'Total Steps', y = 'Calories', title="Relation b/w Calories and Total Steps", color="red")
            plt.show()                                                                                                                                     #scatter analysis
            
            

        if analysis==2 : 
            apple_data.plot(kind = 'bar', x = 'Total Steps', y = 'Calories', title="Relation b/w Calories and Total Steps", color="red")
            plt.show()                                                                                                                                 #bar analysis
            break

    elif choice == 2 :
        
        boat_data = pd.read_excel('D:\\boat.xlsx')

        print("\nboAt Smart Watch -->\n")
        print(boat_data.to_string(index=False))

        print("\n1.Scatter Analysis\n2.Bar Analysis")
        analysis = int(input("\nEnter the value :- "))

        if analysis==1 :
            boat_data.plot(kind = 'scatter', x = 'Total Steps', y = 'Calories', title="Relation b/w Calories and Total Steps", color="red")
            plt.show()
            break

        if analysis==2 : 
            boat_data.plot(kind = 'bar', x = 'Total Steps', y = 'Calories', title="Relation b/w Calories and Total Steps", color="red")
            plt.show()
            break

        break

    elif choice == 3 :

        samsung_data = pd.read_excel('D:\\samsung.xlsx')

        print("\nSamsung Galaxy Smart Watch -->\n")
        print(samsung_data.to_string(index=False))

        print("\n1.Scatter Analysis\n2.Bar Analysis")
        analysis = int(input("\nEnter the value :- "))

        if analysis==1 :
            samsung_data.plot(kind = 'scatter', x = 'Total Steps', y = 'Calories', title="Relation b/w Calories and Total Steps", color="red")
            plt.show()
            break

        if analysis==2 : 
            samsung_data.plot(kind = 'bar', x = 'Total Steps', y = 'Calories', title="Relation b/w Calories and Total Steps", color="red")
            plt.show()
            break

    elif choice == 4 :

        oneplus_data = pd.read_excel('D:\\oneplus.xlsx')

        print("\nHonor Brand Smart Watch -->\n")
        print(oneplus_data.to_string(index=False))

        print("\n1.Scatter Analysis\n2.Bar Analysis")
        analysis = int(input("\nEnter the value :- "))

        if analysis==1 :
            oneplus_data.plot(kind = 'scatter', x = 'Total Steps', y = 'Calories', title="Relation b/w Calories and Total Steps", color="red")
            plt.show()
            break

        if analysis==2 : 
            oneplus_data.plot(kind = 'bar', x = 'Total Steps', y = 'Calories', title="Relation b/w Calories and Total Steps", color="red")
            plt.show()
            break

    elif choice == 5 :

        noise_data = pd.read_excel('D:\\noise.xlsx')

        print("\nNoise Colorfit Smart Watch -->\n")
        print(noise_data.to_string(index=False))

        noise_data.plot(kind = 'scatter', x = 'Total Steps', y = 'Calories', title="Relation b/w Calories and Total Steps")
        plt.show()
        
        print("\n1.Scatter Analysis\n2.Bar Analysis")
        analysis = int(input("\nEnter the value :- "))

        if analysis==1 :
            noise_data.plot(kind = 'scatter', x = 'Total Steps', y = 'Calories', title="Relation b/w Calories and Total Steps", color="red")
            plt.show()
            break

        if analysis==2 : 
            noise_data.plot(kind = 'bar', x = 'Total Steps', y = 'Calories', title="Relation b/w Calories and Total Steps", color="red")
            plt.show()
            break

    elif choice==0 :
        exit()

'''
    For other brands, we can analyse the same way by using the same code
'''
    