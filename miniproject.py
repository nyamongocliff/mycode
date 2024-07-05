#! /usr/bin/env python3              #Shebang

import random


us_states_info ={
    'Alabama': {
        'Capital': 'Montgomery',
        'Activity': 'Space Center',
        'Visit': 'Gulf Shores',
        'NOGO': 'Abandoned Bryce Hospital'
    },
    'Alaska': {
        'Capital': 'Juneau',
        'Activity': 'Denali Park',
        'Visit': 'Glacier Bay National Park',
        'NOGO': 'Abandoned Buckner Building'
    },
    'Arizona': {
        'Capital': 'Phoenix',
        'Activity': 'Grand Canyon',
        'Visit': 'Sedona',
        'NOGO': 'Abandoned Vulture Mine'
    },
    'Arkansas': {
        'Capital': 'Little Rock',
        'Activity': 'Hot Springs',
        'Visit': 'Crystal Bridges Museum',
        'NOGO': 'Dogpatch USA'
    },
    'California': {
        'Capital': 'Sacramento',
        'Activity': 'Golden Gate',
        'Visit': 'Yosemite Park',
        'NOGO': 'Salton Sea'
    },
    'Colorado': {
        'Capital': 'Denver',
        'Activity': 'Skiing',
        'Visit': 'Rocky Mountain Park',
        'NOGO': 'Cave of the Winds'
    },
    'Connecticut': {
        'Capital': 'Hartford',
        'Activity': 'Mystic Seaport',
        'Visit': 'Yale Art Gallery',
        'NOGO': 'Pleasure Beach'
    },
    'Delaware': {
        'Capital': 'Dover',
        'Activity': 'Rehoboth Beach',
        'Visit': 'Winterthur Museum',
        'NOGO': 'Old New Castle Courthouse'
    },
    'Florida': {
        'Capital': 'Tallahassee',
        'Activity': 'Disney World',
        'Visit': 'Everglades Park',
        'NOGO': 'Dozier School'
    },
    'Georgia': {
        'Capital': 'Atlanta',
        'Activity': 'Savannah Tour',
        'Visit': 'Georgia Aquarium',
        'NOGO': 'Underground Atlanta'
    },
    'Hawaii': {
        'Capital': 'Honolulu',
        'Activity': 'Waikiki Beach',
        'Visit': 'Haleakalā Park',
        'NOGO': 'Sacred Falls'
    },
    'Idaho': {
        'Capital': 'Boise',
        'Activity': 'Shoshone Falls',
        'Visit': 'Craters of the Moon',
        'NOGO': 'Kellogg'
    },
    'Illinois': {
        'Capital': 'Springfield',
        'Activity': 'Millennium Park',
        'Visit': 'Art Institute',
        'NOGO': 'Lincoln Park Zoo'
    },
    'Indiana': {
        'Capital': 'Indianapolis',
        'Activity': 'Speedway',
        'Visit': 'Indiana Dunes',
        'NOGO': 'Central State Hospital'
    },
    'Iowa': {
        'Capital': 'Des Moines',
        'Activity': 'State Fair',
        'Visit': 'Pikes Peak Park',
        'NOGO': 'Farrar Schoolhouse'
    },
    'Kansas': {
        'Capital': 'Topeka',
        'Activity': 'Flint Hills',
        'Visit': 'Tallgrass Prairie',
        'NOGO': 'Joyland'
    },
    'Kentucky': {
        'Capital': 'Frankfort',
        'Activity': 'Bourbon Trail',
        'Visit': 'Mammoth Cave',
        'NOGO': 'Waverly Hills'
    },
    'Louisiana': {
        'Capital': 'Baton Rouge',
        'Activity': 'Mardi Gras',
        'Visit': 'French Quarter',
        'NOGO': 'Six Flags'
    },
    'Maine': {
        'Capital': 'Augusta',
        'Activity': 'Acadia Park',
        'Visit': 'Portland Head Light',
        'NOGO': 'Stinson Seafood Plant'
    },
    'Maryland': {
        'Capital': 'Annapolis',
        'Activity': 'Inner Harbor',
        'Visit': 'Antietam Battlefield',
        'NOGO': 'Glenn Dale Hospital'
    },
    'Massachusetts': {
        'Capital': 'Boston',
        'Activity': 'Freedom Trail',
        'Visit': 'Boston Common',
        'NOGO': 'Belchertown State School'
    },
    'Michigan': {
        'Capital': 'Lansing',
        'Activity': 'Mackinac Island',
        'Visit': 'Sleeping Bear Dunes',
        'NOGO': 'Northville Psychiatric Hospital'
    },
    'Minnesota': {
        'Capital': 'Saint Paul',
        'Activity': 'Mall of America',
        'Visit': 'Voyageurs Park',
        'NOGO': 'Gray Cloud Island'
    },
    'Mississippi': {
        'Capital': 'Jackson',
        'Activity': 'Natchez Trace',
        'Visit': 'Vicksburg National Military Park',
        'NOGO': 'Windsor Ruins'
    },
    'Missouri': {
        'Capital': 'Jefferson City',
        'Activity': 'Gateway Arch',
        'Visit': 'Branson',
        'NOGO': 'Zodiac Cottage'
    },
    'Montana': {
        'Capital': 'Helena',
        'Activity': 'Glacier Park',
        'Visit': 'Yellowstone Park',
        'NOGO': 'Coloma Ghost Town'
    },
    'Nebraska': {
        'Capital': 'Lincoln',
        'Activity': 'Henry Doorly Zoo',
        'Visit': 'Chimney Rock',
        'NOGO': 'Hummel Park'
    },
    'Nevada': {
        'Capital': 'Carson City',
        'Activity': 'Las Vegas',
        'Visit': 'Lake Tahoe',
        'NOGO': 'Centralia Mine Fire'
    },
    'New Hampshire': {
        'Capital': 'Concord',
        'Activity': 'White Mountains',
        'Visit': 'Mount Washington',
        'NOGO': 'Madame Sherri\'s Castle'
    },
    'New Jersey': {
        'Capital': 'Trenton',
        'Activity': 'Jersey Shore',
        'Visit': 'Liberty State Park',
        'NOGO': 'Greystone Park Hospital'
    },
    'New Mexico': {
        'Capital': 'Santa Fe',
        'Activity': 'Carlsbad Caverns',
        'Visit': 'White Sands',
        'NOGO': 'Los Alamos Laboratory'
    },
    'New York': {
        'Capital': 'Albany',
        'Activity': 'Times Square',
        'Visit': 'Niagara Falls',
        'NOGO': 'Love Canal'
    },
    'North Carolina': {
        'Capital': 'Raleigh',
        'Activity': 'Biltmore Estate',
        'Visit': 'Great Smoky Mountains',
        'NOGO': 'Henrietta Mill'
    },
    'North Dakota': {
        'Capital': 'Bismarck',
        'Activity': 'Theodore Roosevelt Park',
        'Visit': 'Fort Abraham Lincoln',
        'NOGO': 'San Haven Sanatorium'
    },
    'Ohio': {
        'Capital': 'Columbus',
        'Activity': 'Rock & Roll Hall of Fame',
        'Visit': 'Hocking Hills',
        'NOGO': 'Chippewa Lake Park'
    },
    'Oklahoma': {
        'Capital': 'Oklahoma City',
        'Activity': 'Route 66',
        'Visit': 'Wichita Mountains',
        'NOGO': 'Abandoned Black Jail'
    },
    'Oregon': {
        'Capital': 'Salem',
        'Activity': 'Crater Lake',
        'Visit': 'Multnomah Falls',
        'NOGO': 'Fairview Training Center'
    },
    'Pennsylvania': {
        'Capital': 'Harrisburg',
        'Activity': 'Liberty Bell',
        'Visit': 'Gettysburg',
        'NOGO': 'Centralia Mine Fire'
    },
    'Rhode Island': {
        'Capital': 'Providence',
        'Activity': 'Cliff Walk',
        'Visit': 'Newport Mansions',
        'NOGO': 'Ladd School'
    },
    'South Carolina': {
        'Capital': 'Columbia',
        'Activity': 'Charleston Tour',
        'Visit': 'Myrtle Beach',
        'NOGO': 'Hell Hole Swamp'
    },
    'South Dakota': {
        'Capital': 'Pierre',
        'Activity': 'Mount Rushmore',
        'Visit': 'Badlands',
        'NOGO': 'Spooklight Road'
    },
    'Tennessee': {
        'Capital': 'Nashville',
        'Activity': 'Grand Ole Opry',
        'Visit': 'Great Smoky Mountains',
        'NOGO': 'Brushy Mountain State Penitentiary'
    },
    'Texas': {
        'Capital': 'Austin',
        'Activity': 'River Walk',
        'Visit': 'Big Bend Park',
        'NOGO': 'Yorktown Memorial Hospital'
    },
    'Utah': {
        'Capital': 'Salt Lake City',
        'Activity': 'Arches Park',
        'Visit': 'Zion Park',
        'NOGO': 'Thistle Ghost Town'
    },
    'Vermont': {
        'Capital': 'Montpelier',
        'Activity': 'Ben & Jerry\'s Factory',
        'Visit': 'Stowe',
        'NOGO': 'Mad Dog Hill'
    },
    'Virginia': {
        'Capital': 'Richmond',
        'Activity': 'Colonial Williamsburg',
        'Visit': 'Shenandoah Park',
        'NOGO': 'Henricus Historical Park'
    },
    'Washington': {
        'Capital': 'Olympia',
        'Activity': 'Space Needle',
        'Visit': 'Mount Rainier',
        'NOGO': 'Northern State Hospital'
    },
    'West Virginia': {
        'Capital': 'Charleston',
        'Activity': 'New River Gorge',
        'Visit': 'Harpers Ferry',
        'NOGO': 'Lake Shawnee Amusement Park'
    },
    'Wisconsin': {
        'Capital': 'Madison',
        'Activity': 'Wisconsin Dells',
        'Visit': 'Door County',
        'NOGO': 'Summerwind Mansion'
    },
    'Wyoming': {
        'Capital': 'Cheyenne',
        'Activity': 'Yellowstone Park',
        'Visit': 'Grand Teton Park',
        'NOGO': 'Swetts Greybull'
    }
}

print("Welcome to this game. Let's see how much Geography you still remember")
print("**************************************************************************************************************")
while True:
    random_state = random.choice(list(us_states_info.keys())) #Random state
    capital = us_states_info[random_state]['Capital']   #Extract correct capital
    activity = us_states_info[random_state]['Activity']
    visit = us_states_info[random_state]['Visit']
    nogo = us_states_info[random_state]['NOGO']

    capital_choice = input(f" What is the capital city of {random_state}? ").strip().lower()


    if capital_choice == capital.lower():
        print(f"Correct! The capital of {random_state} is indeed {capital}.\n")
        print(f"Did you know if you ever visit {random_state};\nYou can visit {activity} & {visit}.\nPlease stay away from {nogo}.")
    else:
        retry = input(f"Incorrect.The capital of {random_state} is {capital}.\n\nPlease enter yes to get more information about {random_state} or no to quit. (yes/no): ").strip().lower()
        print(f"Here is some information about {random_state};\nSome nice place to are visit {activity} & {visit}.\nPlease stay away from {nogo}!!!")
        if retry == "no":
            print(f"Thanks for playing. It's sad to see you quit.")
            break
        elif retry == "yes":
            print("Let's try another one.")
        else:
            print("Invalid input. Let's try again.")

    play_again = input("Do you want to guess the capital of another state? (yes/no): ").strip().lower()
    if play_again == "no":
        print("Thanks for playing!")
            
    elif play_again == "yes":
        print("Great! Let's continue.")
    else:
        print("Invalid input. Exiting the game.")
        break









