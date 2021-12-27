import numpy as np
import pandas as pd
import calendar
import time

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
    months_dic={'january':'Jan','february':'Feb','march':'Mar','april':'Apr','may':'May',"june":'Jun'}
    print('Hello! Let\'s explore some US bikeshare data!')
    
    """(str) city - name of the city to analyze"""
    city=input("Would you like to see data from Chicago, new york city or Washington ? ").lower()
    while city not  in ['chicago','new york city','washington']:
        city=input("Please choose city from (chicago,newyork,washington) ").lower()     
    
    """(str) month - name of the month to filter by, or "all" to apply no month filter"""    
    month=input("Would you like to filter time by month or all months? ").lower()
    if month !="all":
        while month not  in ['january', 'february', 'march', 'april', 'may', 'june']:
            month=input('please select from the following[jan,feb,mar,apr,may,jun]').lower()
            if month=="all":
                break
    """"(str) day - name of the day of week to filter by, or "all" to apply no day filter"""
    day=input("Would you like to filter by day or all days ? ").lower()
    if day !="all":
        while day not in ['saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']:
            day=input('Please select from the following options [Saturday,Sunday,Monday,Tuesday,Wednesday,Thursday,Friday] ').lower()
            if day=="all":
                break
    print('-'*40)
    if month in months_dic:   
       month=months_dic[month]
    return city, month, day

def five_lines(df):
    """display the first five rows of data ad the following five rows"""
    
    i=0
    answer=input('Do you like to see the first five rows :').capitalize()
    while True:
        if answer == "No":
            break
        if answer =="Yes":
            print(df[i:i+5])
            answer=input("Do you like to see the next five rows :").capitalize()
        else:
            answer=input("Please enter yes or no :").capitalize()

     


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
    
    df=pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['hour']=df['Start Time'].dt.hour
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name
    df['month'] = df['month'].apply(lambda x: calendar.month_abbr[x])
    if month!="all" :
       df=df.loc[(df['month']==month)]  
    
    if day !="all":
        df=df.loc[(df['day']==day)]

    

    return df   
    
 
    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())



    # TO DO: Display counts of gender
    
    try:
        print(df["Gender"].value_counts())
    except:
        print("no Gender to display")    
    
    
    #TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The earlist value is : "+str(df['Birth Year'].min()))
        print("The most common value is : "+str(df['Birth Year'].value_counts().idxmax()))
        print("The most recent value : "+str(df['Birth Year'].max()))
    except:
        print("no Birth year data")

    



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)






def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month   
    print('The most common month is '+str(df['month'].value_counts().idxmax()))
    

    # TO DO: display the most common day of week
    print('The most common day is '+str(df['day'].value_counts().idxmax()))
    

    # TO DO: display the most common start hour
    print('The most common hour is '+str(df['hour'].value_counts().idxmax()))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most Start Station is '+str(df['Start Station'].value_counts().idxmax()))


    # TO DO: display most commonly used end station
    print('The most common End Station is '+str(df['End Station'].value_counts().idxmax()))




    # TO DO: display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is '+str(df.groupby(['Start Station','End Station']).size().idxmax()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time is : '+str(df['Trip Duration'].sum()))



    # TO DO: display mean travel time
    print('The avarege travel time is :'+str(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)












def main():
    while True:
        city, month, day = get_filters()
        
        df = load_data(city, month, day)
        five_lines(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



if __name__ == "__main__":
	main()


   
