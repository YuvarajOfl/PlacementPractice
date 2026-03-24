class ParkingSystem:

    def __init__(self, total_slots):
        
        self.total_slots=total_slots
        self.available_slots=total_slots
        self.parked_vehicles= {}

    def parkVehicle(self, vehicle_id):

        if self.available_slots > 0:

            if vehicle_id in self.parked_vehicles:
                print(f"Vehicle {vehicle_id} is already parked")
                
            else:
                self.parked_vehicles[vehicle_id]=True
                self.available_slots-=1
                print(f"Vehicle {vehicle_id} has been parked")
        else:
            print("No Available Slots")

    def removeVehicle(self, vehicle_id):

        if vehicle_id in self.parked_vehicles:

            del self.parked_vehicles[vehicle_id]
            self.available_slots+=1
            print(f"Vehicle{vehicle_id} has been removed")

        else:
            print(f"Vehicle {vehicle_id} was not found in the parking list!")

def main():

    parking_list= ParkingSystem(total_slots=5)

    while True:

        print("\n Welcome to Parking System!")
        print("\n 1. Park Vehicle")
        print("\n 2. Remove Vehicle")
        print("\n 3. Show Status")
        print("\n 4. Exit")

        choice=input("Enter your choice:")

        if choice == "1":

            vehicle_id= input("Enter your vehicle id to park: ")
            parking_list.parkVehicle(vehicle_id)

        elif choice == "2":
                
            vehicle_id= input("Enter the vehicle id to remove: ")
            parking_list.removeVehicle(vehicle_id)

        elif choice == "4":

            print("Exiting...")
            break
            
        else:

            print("Invalid choice. Please choose again!")

if __name__ == "__main__":
    
    main()
