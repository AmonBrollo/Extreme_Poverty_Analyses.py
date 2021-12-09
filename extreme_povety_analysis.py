import pandas as pd

def main():
    # Ask a year from the user to investigate
    year_of_choice = int(input("Which year would you like to invertigate? "))

    dataset = pd.read_csv("extreme-poverty-dataset.csv")

    # Find the rows with the chosen year
    rows = dataset.loc[dataset["Year"] == year_of_choice,  "$30.00 per day - share of population below poverty line"]

    countries_largest_bpl = find_largest_portion_by_year(dataset, year_of_choice, rows)

    countries_smallest_bpl = find_smallest_portion_by_year(dataset, year_of_choice, rows)

    # Display the countries with largest portions of people below poverty line and
    # smallest portions of people below poverty line.
    print("The countries with the largest portions of people below the poverty line are:")
    for country in countries_largest_bpl:
        print(country)
    print("\nThe countries with the smallest portions of people below the poverty line are:")
    for country in countries_smallest_bpl:
        print(country)
    print()

    # Ask the user weather he would like to continue exploring the dataset by entity
    y_or_n = input("Would you like to investigate by country?(y/n) ")
    if y_or_n == "n":
        print("\nThank you for using this program. Good bye!\n")
    else: 
        country_of_interest = input("Which country would you like to investigate? ")
        largest_by_country = find_largest_portion_by_country(dataset, country_of_interest)

        # Display the years when the country of interest had the largest percent of the population below the line of poverty
        print(f"The years when {country_of_interest} had the most its people below the poverty line were:")
        for year in largest_by_country:
            print(year)

def find_largest_portion_by_year(dataset, year_of_choice, rows):
    # Find the country with the largest portion of people below the poverty line
    largest_below_poverty = rows.max()
    # Tell the user the percentage of people below the poverty line
    print(f"\nThe largest number of people below the poverty line in a given country in the year {year_of_choice} is {largest_below_poverty:.2f}%")
    country_with_largest_below_poverty = dataset[(dataset["Year"] == year_of_choice) & (dataset["$30.00 per day - share of population below poverty line"] == largest_below_poverty)]

    # Get the countries with the largest portions of people below the poverty line
    countries_largest_bpl = country_with_largest_below_poverty["Entity"].to_list()
    return countries_largest_bpl

def find_smallest_portion_by_year(dataset, year_of_choice, rows):
    # Find the country with the smallest portion of people below the poverty line
    smallest_below_poverty = rows.min()

    # Tell the user the percentage of people below the poverty line
    print(f"And the smallest is {smallest_below_poverty:.2f}%\n")
    country_with_smallest_below_poverty = dataset[(dataset["Year"] == year_of_choice) & (dataset["$30.00 per day - share of population below poverty line"] == smallest_below_poverty)]

    # Get the countries with the smallest portions of people below the poverty line
    countries_smallest_bpl = country_with_smallest_below_poverty["Entity"].to_list()
    return countries_smallest_bpl

def find_largest_portion_by_country(dataset, country_of_interest):
    # Find the rows of the country of interest
    coi_rows = dataset.loc[dataset["Entity"] == country_of_interest, "$30.00 per day - share of population below poverty line"]

    # Find the years with the largest portion of people below the poverty line
    largest_by_country = coi_rows.max()
    poorest_years = dataset[(dataset["Entity"] == country_of_interest) & (dataset["$30.00 per day - share of population below poverty line"] == largest_by_country)]
    poorest_years = poorest_years["Year"].to_list()
    return poorest_years

def find_smallest_portion_by_country():
    pass

if __name__ == "__main__":
    main()
