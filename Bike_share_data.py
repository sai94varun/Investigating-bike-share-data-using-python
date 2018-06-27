import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    #TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city1 = input('Please enter a city from (chicago,new york city,washington) :')
      city = city1.lower()
      if city in ['chicago','new york city','washington']:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month1 = input('Please enter a month from (all,january,february,march,april,may,june) : ')
      month = month1.lower()
      if month in ['all','january','february','march','april','may','june']:
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day1=input('Please enter a day from (all,monday,tuesday,wednesday,thursday,friday,saturday,sunday) : ')
      day = day1.lower()
      if day in ['all','monday','tuesday','wednesday','thursday','friday','saturday']:
        break

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
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
	
        # filter by day of week if applicable
	
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
	
    return df
      
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])

	# extract hour from the Start Time column to create an hour column
    df['month'] = df['Start Time'].dt.month
    
    # find the most popular month
    popular_month = df['month'].mode()[0]
    month_list = [ 'january', 'February', 'march','april','may','june']
    month = month_list[popular_month -1]
    
    print('Printing the Most Common Month:')
    print('Most Popular month:', month)
    
    # TO DO: display the most common day of week
	# convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

	# extract hour from the Start Time column to create an hour column
    df['weekday_name'] = df['Start Time'].dt.weekday_name
    
    # find the most popular hour
    
    popular_weekday = df['weekday_name'].mode()[0]
    
    print('Printing the Most Popular Weekday:')
    print('Most Popular weekday:', popular_weekday)
    
    # TO DO: display the most common start hour
    # convert the Start Time column to datetime
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])

	# extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour

	# find the most popular hour
    popular_hour = df['hour'].mode()[0]
    
    print('Printing the Most Popular Start Hour:')
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('Printing the Popular Start Station:')
    print('Popular Start Station:',popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('Prinitng the Common End station:')
    print('Common End station:',popular_end_station)
    
    # TO DO: display most frequent combination of start station and end station trip
    df['start end station'] = df['Start Station']+df['End Station']
    start_end_station = df['start end station'].mode()[0]
    #start_end_station = df.groupby(['Start Station','End Station'])
    print('Printing the frequent combination of Start and End Station')
    print('Frequent Combinaion of Start and End Station:',start_end_station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_travel_time = df['Trip Duration'].sum()
    print('Printing the Total Time Travelled:')
    print('Total Time Travelled:',Total_travel_time)
    
    # TO DO: display mean travel time
    Mean_travel_time = df['Trip Duration'].mean()
    print('Printing the Mean Travel Time:')
    print('Mean Travel Time:',Mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Printing the User Types:')
    print('Number of User Types:',user_types)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def gender_birthstats(df):
	"""Displays statistics on bikeshare users."""
    
	print('\nCalculating Gender/Birth Stats...\n')
    
	start_time = time.time()
    
    # TO DO: Display counts of gender
	gender = df['Gender'].value_counts()
	print('Printing Gender Counts:')
	print('Gender Counts:',gender)
    
    # TO DO: Display earliest, most recent, and most common year of birth
	print('Printing Birth Statistics')
	ear_common_dob = df['Birth Year'].min()
	print('Earliest Birth Year:',ear_common_dob)
	rec_common_dob = df['Birth Year'].max()
	print('Most Recent Birth Year:',rec_common_dob)
	common_dob = df['Birth Year'].mode()[0]
	print('Common Birth Year:',common_dob)
    
	print("\nThis took %s seconds." % (time.time() - start_time))
	print('-'*40)
    
def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more,
    continuing asking until they say stop.

    Args:
        none.
    Returns:
        TODO: fill out return type and description (see get_city for an example)
    '''
    display = input('\nWould you like to view individual trip data?'
                    'Type \'yes\' or \'no\'.\n')
    while True:
      if display.lower() != 'yes':
        return
      else:
        break
    # TODO: handle raw input and complete function
    print('Displaying individual data')
    i = 0
    n = 5
    while i in range(0,len(df.index)):
      display2 = input('Would you like to continue : ')
      if display2.lower() != 'no' :
        print('Displaying next 5 lines :',df.iloc[i:n])
        i = i+5
        n = n+5
        
      if display2.lower() !='yes':
        break
           
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        if(city != 'washington'):
        	gender_birthstats(df)
            
        display_data(df)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
