class banquet: 
  def __init__(self, ID, Capacity, Price_list, Amenities):
    self.ID = ID
    self.Capacity = Capacity
    self.Price_list = Price_list
    self.Amenities = Amenities
All_banquets = []
n_objects = int(input())
for object in range(n_objects):
  id = input()
  name = (input())
  capacity = int(input())
  n_price_list = int(input())
  price_list=[]
  for plist in range(n_price_list):
    per_plate = int(input())
    low_guest = int(input())
    high_guest = int(input())
    price_list.append([per_plate, low_guest, high_guest])
  n_Amenities = int(input())
  Amenities = []
  for amenity in range(n_Amenities):
    Amenities.append(input())
  name = banquet(id, capacity, price_list, Amenities)
  All_banquets.append(name)
Req_capacity = int(input())
N_req_amenities = int(input())
Req_amenities = []
for amenitiy in range(N_req_amenities):
  Req_amenities.append(input())
GST_price = "Hall Not Found."
for hall in All_banquets:
    max_capacity = hall.Capacity
    if all([(Amenities in hall.Amenities) for Amenities in Req_amenities]) and Req_capacity <= max_capacity:
        for price_list in hall.Price_list:
          price_per_plate = price_list[0]
          low = price_list[1]
          high = price_list[2]
          if low <= Req_capacity <= high:
              final_price = price_per_plate * Req_capacity
              GST_price = final_price + (final_price / 100) * 13
              print((GST_price))
              break
if GST_price == "Hall Not Found.":
    print(GST_price)





