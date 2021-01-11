import time
import pandas as pd
import numpy as np
import datetime

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    ***Extra line for Github project***
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input('\nWhich city data would you like to see: Chicago, New York City or Washington?\n')
        if city.lower() in CITY_DATA.keys():
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('\nWhich months data would you like to see: January, February, March, April, May, June or All?\n')
        if month.lower() in ['all', 'january', 'february', 'march','april', 'may', 'june']:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('\nWhich days data would you like to see: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All?\n')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday', 'sunday']:
            break

    print('--o'*20)
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

    # loading city data file into a dataframe
    df = pd.read_csv(CITY_DATA[city.lower()])

    # Convert the 'Start Time' column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from 'Start Time' to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # Filter by month if applicable
    if month.lower() != 'all':
        # Use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # Filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day.lower() != 'all':
        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('\nMost Common Month is:')
    print(df['month'].mode()[0])

    # display the most common day of week
    print('\nMost Common Day of Week is:')
    print(df['day_of_week'].mode()[0])

    # display the most common start hour
    print('\nMost Common Start Hour is:')
    print(df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('--o'*20)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\nMost Commonly Used Start Station is:')
    print(df['Start Station'].mode()[0])

    # display most commonly used end station
    print('\nMost Commonly Used End Station is:')
    print(df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print('\nMost Frequent Combination of Start and End Station is:')
    print(df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('--o'*20)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('\nTotal Travel Time is:')
    print(datetime.timedelta(seconds=int(df['Trip Duration'].sum())))

    # display mean travel time
    print('\nMean Travel Time is:')
    print(datetime.timedelta(seconds=int(df['Trip Duration'].mean())))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('--o'*20)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Counts of User Types is:')
    print(df['User Type'].value_counts())

    # Display counts of gender
    print('\nCounts of Gender is:')
    try:
        print(df['Gender'].value_counts())
    except:
        print('Our data does not include gender!..')

    # Display earliest, most recent, and most common year of birth
    print('\nEarliest, Most Recent and Most Common Year of Birth:')
    try:
        print('Earliest: {}\nMost Recent: {}\nMost Common: {}'
              .format(int(df['Birth Year'].min()), int(df['Birth Year'].max()),
                      int(df['Birth Year'].mode()[0])))
    except:
        print('Our data does not include year of birth!..')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('--o'*20)

def disp_data(df):
    """Raw data is displayed upon request by the user"""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    count = 0
    # Display row data
    while True:
        display = input('\nWould you like to display raw data? Enter yes or no.\n')
        if display.lower() != 'yes':
            break
        else:
            print(df.iloc[count:count+5])
            count +=5

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('--o'*20)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        disp_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
