import pandas as pd

def main():
    # Ask a year from the user to investigate
    year_of_choice = int(input("Which year would you like to invertigate?(1981-2019) "))

    # Turn the dataset file into a readable dataset
    dataset = pd.read_csv("extreme-poverty-dataset.csv")

    # Get the rows with the chosen year
    rows = dataset.loc[dataset["Year"] == year_of_choice,  "$30.00 per day - share of population below poverty line"]

    # Get the countries with the largest population below the extreme poverty line.
    countries_largest_bpl = get_largest_year_below(dataset, year_of_choice, rows)

    # Get the countries with the smallest population below the extreme poverty line.
    countries_smallest_bpl = get_smallest_year_below(dataset, year_of_choice, rows)

    # Display the countries with largest portions of people below poverty line and smallest portions of people 
    # below poverty line.
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
        pass
    else: 
        # Ask the country of interest
        country_of_interest = input("\nWhich country would you like to investigate? ")

        largest_below = get_largest_country_below(dataset, country_of_interest)

        # Display the years when the country of interest had the largest percent of the population below 
        # the line of poverty
        print(f"The years when {country_of_interest} had the most of its people below the poverty line were:")
        for year in largest_below:
            print(year)

        smallest_below = get_smallest_country_below(dataset, country_of_interest)

        # Display the years when the country of interest had the smallest percent of the population below 
        # the line of poverty
        print(f"And the years when it had least people below the poverty line were:")
        for year in smallest_below:
            print(year)

    print("\nThank you for using this program. Good bye!\n")

def get_largest_year_below(dataset, year_of_choice, rows):
    """
    Get the country with the largest portion of people below the poverty line, tell the user
    the percentage of people below the poverty line and get the countries with the largest portions 
    of people below the extreme poverty line.
    Parameters
        dataset: The dataset being analysed
        year_of_coice: The user's choice of year to explore
        rows: The rows that hold the data for the chosen year
    Return: the counties with the largest portions of people below the extreme poverty line in the user's chosen 
    year. 
    """
    largest_below_poverty = rows.max()
    print(f"\nThe largest number of people below the poverty line in a given country in the year {year_of_choice} is {largest_below_poverty:.2f}%")
    country_with_largest_below_poverty = dataset[(dataset["Year"] == year_of_choice) & (dataset["$30.00 per day - share of population below poverty line"] == largest_below_poverty)]
    countries_largest_bpl = country_with_largest_below_poverty["Entity"].to_list()
    return countries_largest_bpl

def get_smallest_year_below(dataset, year_of_choice, rows):
    """
    get the country with the smallest portion of people below the poverty line, tell the user
    the percentage of people below the poverty line and get the country with the smallest portions 
    of people below the extreme poverty line.
    Parameters
        dataset: The dataset being analysed
        year_of_coice: The user's choice of year to explore
        rows: The rows that hold the data for the chosen year
    Return: A list of counties with the smallest portions of people below the extreme poverty line in the user's 
    chosen year. 
    """
    smallest_below_poverty = rows.min()
    print(f"And the smallest is {smallest_below_poverty:.2f}%\n")
    country_with_smallest_below_poverty = dataset[(dataset["Year"] == year_of_choice) & (dataset["$30.00 per day - share of population below poverty line"] == smallest_below_poverty)]
    countries_smallest_bpl = country_with_smallest_below_poverty["Entity"].to_list()
    return countries_smallest_bpl

def get_largest_country_below(dataset, country_of_interest):
    """
    Get the years when the country of interest had the largest percent of the population below the line of poverty.
    Parameters
        dataset: The dataset being analysed.
        country_of_interest: The user's choice of country to explore.
    Return: The years where most of the population was under the extreme poverty line.
    """
    coi_rows = get_country_of_interest_rows(dataset, country_of_interest)
    largest_below = coi_rows.max()
    poorest_years = dataset[(dataset["Entity"] == country_of_interest) & (dataset["$30.00 per day - share of population below poverty line"] == largest_below)]
    poorest_years = poorest_years["Year"].to_list()
    return poorest_years

def get_smallest_country_below(dataset, country_of_interest):
    """
    Get the years when the country of interest had the smallest percent of the population below the line of poverty.
    Parameters
        dataset: The dataset being analysed.
        country_of_interest: The user's choice of country to explore.
    Return: The years where most of the population was above the extreme poverty line.
    """
    coi_rows = get_country_of_interest_rows(dataset, country_of_interest)
    smallest_below = coi_rows.min()
    richest_years = dataset[(dataset["Entity"] == country_of_interest) & (dataset["$30.00 per day - share of population below poverty line"] == smallest_below)]
    richest_years = richest_years["Year"].to_list()
    return richest_years

def get_country_of_interest_rows(dataset, country_of_interest):
    """
    get the rows of the country of interest
    return: the rows with the data of the countries of interest
    """
    rows = dataset.loc[dataset["Entity"] == country_of_interest, "$30.00 per day - share of population below poverty line"]
    return rows

if __name__ == "__main__":
    main()
