import time
import pandas as pd
import numpy as np
import sys

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    
    c = ['chicago','new york','washington']
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while(True):
        city = str(input('Would you like to see data for Chicago, New York, or Washington?\n')).lower()
        if(city not in c):
            print('Entered invalid input, please try again')
        else:
            break
        
    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june','august', 'september', 'october', 'november', 'december']
    
    while(True):
        month = str(input('Would you like to filter the data by month or not at all?  input for month (all, january, february, ... )\n')).lower()
        if(month not in months):
            print('Entered invalid input, please try again') 
        else:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    days = ['all','sunday','monday','tuseday','wenesday','thursday','friday','saturday']
    while(True):
        day = str(input('Would you like to filter the data by month or not at all?   input for day of week (all, monday, tuesday, ... sunday)\n')).lower()
        if(day not in days):
            print('Entered invalid input, please try again')
        else:
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['week_day'] = df['Start Time'].dt.weekday_name
    
    if(month!='all'):
        months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month)+1
        df = df.loc[df['month']==month]
    if(day!='all'):
        day = day.title()
        df = df.loc[df['week_day'] == day]
    return df
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('the most common month',df['month'].mode()[0])

    # TO DO: display the most common day of week
    print('the most common day of week ',df['week_day'].mode()[0])

    # TO DO: display the most common start hour
    print('the most common start hour',df['Start Time'].dt.hour.mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station: ',df['Start Station'].mode()[0])
    #print(df['Start Station'].value_counts())

    # TO DO: display most commonly used end station
    print('most commonly used end station: ',df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    temp = pd.DataFrame('Start Station: ' + df['Start Station']+' __________  The end:'+df['End Station'])
    
    #print(temp['ss'].value_counts())
    print('most frequent combination of start station and end station trip:\n')
    for i in list(temp.mode()[0]):
        print(i)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean travel time',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('total travel time',df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('mean travel time',df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\n---counts of user types---\n\n',df['User Type'].value_counts())

    # TO DO: Display counts of gender
    try:
        print('\n\n---counts of gender---\n\n',df['Gender'].value_counts())

        # TO DO: Dispatlay earliest, most recent, and most common year of birth
        print('\n\n---statistics on birth year---')
        print('\n earliest\t:',int(df['Birth Year'].min()),'\n most recent\t:',int(df['Birth Year'].max()),'\n most common year of birth\t:',int(df['Birth Year'].mode()[0]),'\n')
    except:
        print('counts of gender and  earliest, most recent, and most common year of birth cant be caluclated due absence of Birth Year, Gender in washington.csv')
    while(1):
        f=0
        s = str(input('if they want to see 5 lines of raw data, display that data? Yes or No:\n')).lower()
        if(s=='yes'):
            print(df.head(5))
            step = 5
            while(1):
                i = input('Do you want to print next 5 line of raw data? yes or no\n').lower()
                if(i=='no'):
                    f=1
                    break
                elif(i=='yes'):
                    print(df.iloc[step:step+5])
                    step+=5
                else:
                    print('please enter vaild input\n')
        elif( s=='no'):
            print('ok')
            break
        else:
            print('please enter vaild input\n')
        if(f==1):
            print('ok')
            break


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




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
