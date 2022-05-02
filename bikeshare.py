import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ('january', 'february', 'march', 'april', 'may', 'june')
weekdays = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        cities= ['chicago','new york city','washington']
        city= input("\n Which city would you like to select? (Chicago, New york city, Washington) \n").lower()
        if city in cities:
            break
        else:
            print("\n Kindly enter a valid city name")    

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        months= ['January','February','March','April','June','May','None']
        month = input("\n Which month would you like to select? (January, February, March, April, May, June)? Type 'None' for no month filter\n").title()
        if month in months:
            break
        else:
            print("\n Kindly enter a valid month")    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        days= ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday','None']
        day = input("\n Which day of the week would you like to select? Type 'None' if you don\'t want any \n").title()         
        if day in days:
            break
        else:
            print("\n Kindly enter a valid day, please") 



    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'None':
        # use the index of the months list to get the corresponding int
        months = ['January', 'February', 'March', 'April', 'May', 'June']
        month = months.index(month)+ 1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month] 

    # filter by day of week if applicable
    if day != 'None':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]
 # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    # filter by month if applicable
    if month != 'None':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+ 1
    
        # filter by month to create the new dataframe
        df = df[df['month']== month] 

    # filter by day of week if applicable
    if day != 'None':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day]

    return df

#Calculating the statistics
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if month =='None':
        common_month= df['month'].mode()[0]
        months= ['January','February','March','April','May','June']
        pop_month= months[common_month - 1]
        print("The most Popular month is", common_month)

    # TO DO: display the most common day of week
    if day =='None':
        common_day= df['day_of_week'].mode()[0]
        print("The most Popular day is", common_day)

    # TO DO: display the most common start hour
    df['Start Hour'] = df['Start Time'].dt.hour
    common_hour=df['Start Hour'].mode()[0]
    print("The popular Start Hour is {}:00 hrs".format(common_hour))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start_station= df['Start Station'].mode()[0]
    print("The most commonly used Start Station is {}".format(common_start_station))

    # TO DO: display most commonly used end station
    common_end_station= df['End Station'].mode()[0]
    print("The most commonly used End Station is {}".format(common_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['combination']=df['Start Station']+" "+"to"+" "+ df['End Station']
    common_combo= df['combination'].mode()[0]
    print("The most frequent combination of Start and End Station is {} ".format(common_combo))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration= df['Trip Duration'].sum()
    minute,second= divmod(total_duration, 60)
    hour,minute= divmod(minute, 60)
    print("The total trip duration: {} hour(s) {} minute(s) {} second(s)".format(hour, minute, second))

    # TO DO: display mean travel time
    average_duration= round(df['Trip Duration'].mean())
    m,sec= divmod(average_duration,60)
    if m>60:
        h,m= divmod(m,60)
        print ("The total trip duration: {} hour(s) {} minute(s) {} second(s)".format(h, m, sec))
    else:
        print("The total trip duration: {} minute(s) {} second(s)".format(m, sec))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_counts= df['User Type'].value_counts()
    print("The user types are:\n",user_counts)

    # TO DO: Display counts of gender
    try:
        gender_distribution = df['Gender'].value_counts().to_string()
        print("\nDistribution for each gender:")
        print(gender_distribution)
    except KeyError:
        print("Sorry! No data of user genders for {}."
              .format(city.title()))

    # TO DO: Display earliest, most recent, and most common year of birth
     try:
        earliest_birth_year = str(int(df['Birth Year'].min()))
        print("\nFor the selected filter, the oldest person to ride one "
              "bike was born in: " + earliest_birth_year)
        most_recent_birth_year = str(int(df['Birth Year'].max()))
        print("For the selected filter, the youngest person to ride one "
              "bike was born in: " + most_recent_birth_year)
        most_common_birth_year = str(int(df['Birth Year'].mode()[0]))
        print("For the selected filter, the most common birth year amongst "
              "riders is: " + most_common_birth_year)
    except:
        print("We're sorry! There is no data of birth year for {}."
              .format(city.title()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):

    while True:
        response=['yes','no']
        choice= input("Would you like to view individual trip data (5 entries)? Type 'yes' or 'no'\n").lower()
        if choice in response:
            if choice=='yes':
                start=0
                end=5
                data = df.iloc[start:end,:9]
                print(data)
            break
        else:
            print('Kindly enter a valid response')
    if choice=='yes':       
            while True:
                choice_2= input("Would you like to view more trip data? Type 'yes' or 'no'\n").lower()
                if choice_2 in response:
                    if choice_2 =='yes':
                        start += 5
                        end += 5
                        data = df.iloc[start:end,:9]
                        print(data)
                    else:    
                        break  
                else:
                    print("Kindly enter a valid response") 


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
