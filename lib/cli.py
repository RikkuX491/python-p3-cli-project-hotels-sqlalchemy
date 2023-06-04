import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.models import Hotel

if __name__ == '__main__':
    
    engine = create_engine('sqlite:///db/hotels.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    print("Welcome to the Hotels app!")
    print("What would you like to do?")
    user_input = input('Enter "c" to create a new hotel\nEnter "r" to get / read info about hotels\nEnter "u" to update existing hotels\nEnter "d" to delete hotels\n')

    while(not user_input in ['c', 'r', 'u', 'd']):
        print("Invalid input! Please try again!")
        print("What would you like to do?")
        user_input = input('Enter "c" to create a new hotel\nEnter "r" to get / read info about existing hotels\nEnter "u" to update existing hotels\nEnter "d" to delete hotels\n')

    if user_input == 'c':
        print("You've chosen to create a new hotel!")
        hotel_name = input("Enter the name for the hotel you would like to create:\n")
        hotel = Hotel(name=hotel_name)
        session.add(hotel)
        session.commit()
        print(f"Success! Your new hotel, {hotel.name}, has been created!")

    elif user_input == 'r':
        print("You've chosen to get / read info about existing hotels!")
        hotels = session.query(Hotel)
        print(f"There are {hotels.count()} hotels available!")
        print("Here is the info of all available hotels:")
        for hotel in hotels:
            print(hotel)

    elif user_input == 'u':
        print("You're chosen to update existing hotels!")
        hotels = session.query(Hotel)
        print("Here is the info of all available hotels:")
        for hotel in hotels:
            print(hotel)
        hotel_id = input("Please enter the integer value for the id of the hotel that you would like to update: ")
        hotel = hotels.filter(Hotel.id == int(hotel_id)).first()
        hotel_name = input("Please enter the name that you would like to update this hotel to: ")
        hotel.name = hotel_name
        session.commit()
        print(f"Success! Hotel #{hotel.id} has been updated to have the name {hotel.name}!")

    elif user_input == 'd':
        print("You've chosen to delete existing hotels!")
        hotels = session.query(Hotel)
        print("Here is the info of all available hotels:")
        for hotel in hotels:
            print(hotel)
        hotel_id = input("Please enter the integer value for the id of the hotel that you would like to delete or enter 'a' to delete all hotels: ")
        if hotel_id == 'a':
            hotels.delete()
            session.commit()
            print(f"Success! All hotels have been deleted from the database!")
        else:
            hotel = hotels.filter(Hotel.id == int(hotel_id)).first()
            session.delete(hotel)
            session.commit()
            print(f"Success! Hotel #{hotel.id}: {hotel.name} has been deleted from the database!")