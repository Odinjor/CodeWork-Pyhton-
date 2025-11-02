import pandas as pd 
import matplotlib.pyplot as plt

file_path = "/Users/odinj/Downloads/car_info.csv"
cars = pd.read_csv(file_path)

def shape():
    print(f"Shape of DataFrame: {cars.shape}")

def japanese_cars_wV6():
    car = 'japan'
    engine = 6

    filtered_cars = cars[(cars['origin'] == car) & (cars['cylinders'] == engine)]

    print("Japanese V6 cars:", filtered_cars['name'].tolist())

def cars_w_missing_horsepower():

    filtered_cars = cars[(cars['horsepower'].isna())]
    
    print("Cars with missing horsepower:", filtered_cars['name'].tolist())

def miles_per_gallon():
    mpg = 20

    filtered_cars = cars[cars['mpg'] >= mpg]
    count = filtered_cars['name'].value_counts()
    sum_count = sum(count)

    print(f"Number of cars having mpg >= 20: {sum_count}")

def most_fuel_efficent():
    highest_value = cars['mpg'].max()

    filtered_cars = cars[cars['mpg'] == highest_value]
    print("Most fuel-efficent car:", filtered_cars["name"].tolist())

def min_max_avg():
    minimum_value = cars['weight'].min()
    maximum_value = cars['weight'].max()
    average_value = cars['weight'].mean()

    print(f"Minimum weight: {minimum_value}, Maximum weight: {maximum_value}, Average Weight: {average_value:.2f}")

def drop_it_like_its_hot():
    cleaned_cars = cars.dropna()

    print(cleaned_cars.shape)

def pie_chart():
    different_origins = cars["origin"].unique().tolist()
    sizes = [sum(cars[(cars['origin'] == 'usa')].value_counts()), 
            sum(cars[(cars['origin'] == 'japan')].value_counts()),
            sum(cars[(cars['origin'] == 'europe')].value_counts())]
    
    plt.pie(sizes, labels = different_origins)
    plt.title('Number of Cars Manufactured in Different Countries')
    plt.show()

def the_plot():
    x = pd.Series(cars['mpg'].tolist())
    y = pd.Series(cars['weight'].tolist())
    plt.subplot(1, 2, 1)
    plt.scatter(x,y)
    plt.xlabel('Miles Per Gallon')
    plt.ylabel('Weight of the Cars')
    plt.xlim(0, max(cars["mpg"])+10)
    plt.ylim(0, max(cars["weight"]+1000))
    plt.tight_layout()
    
    x = pd.Series(cars['mpg'].tolist())
    y = pd.Series(cars['displacement'].tolist())
    plt.subplot(1,2,2)
    plt.plot(x, y)
    plt.xlabel("Miles Per Gallon of each car")
    plt.ylabel("The Displacement of each car")
    plt.tight_layout()
    plt.show()

shape()
japanese_cars_wV6()
cars_w_missing_horsepower()
miles_per_gallon()
most_fuel_efficent()
min_max_avg()
drop_it_like_its_hot()
pie_chart()
the_plot()

