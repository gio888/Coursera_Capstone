# -*- coding: utf-8 -*-
"""test merge.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1C0CdjHz6Nf4OdDOkr3lZnhrblN9S6esr
"""

import pandas as pd
import numpy as np

data_string = """Cluster Labels,Neighborhood,1st Most Common Venue,2nd Most Common Venue,3rd Most Common Venue,4th Most Common Venue,5th Most Common Venue,6th Most Common Venue,7th Most Common Venue,8th Most Common Venue,9th Most Common Venue,10th Most Common Venue
0,Agincourt,Latin American Restaurant,Breakfast Spot,Lounge,Chinese Restaurant,Donut Shop,Drugstore,Dumpling Restaurant,Doner Restaurant,Dance Studio,Dog Run
0,Alderwood / Long Branch,Pizza Place,Coffee Shop,Pharmacy,Sandwich Place,Dance Studio,Pub,Athletics & Sports,Skating Rink,Gym,Comfort Food Restaurant
0,Bathurst Manor / Wilson Heights / Downsview North,Coffee Shop,Bank,Pharmacy,Shopping Mall,Sandwich Place,Diner,Bridal Shop,Restaurant,Deli / Bodega,Ice Cream Shop
0,Bayview Village,Chinese Restaurant,Café,Bank,Japanese Restaurant,Distribution Center,Dessert Shop,Dim Sum Restaurant,Diner,Discount Store,Yoga Studio
0,Bedford Park / Lawrence Manor East,Italian Restaurant,Sandwich Place,Coffee Shop,Restaurant,Pizza Place,Thai Restaurant,Liquor Store,Indian Restaurant,Pub,Butcher
0,Berczy Park,Coffee Shop,Cocktail Bar,Bakery,Seafood Restaurant,Café,Restaurant,Cheese Shop,Italian Restaurant,Beer Bar,Farmers Market
0,Birch Cliff / Cliffside West,Skating Rink,College Stadium,General Entertainment,Café,Yoga Studio,Discount Store,Department Store,Dessert Shop,Dim Sum Restaurant,Diner
0,Brockton / Parkdale Village / Exhibition Place,Café,Nightclub,Breakfast Spot,Coffee Shop,Pet Store,Music Venue,Burrito Place,Italian Restaurant,Intersection,Restaurant
0,Business reply mail Processing CentrE,Light Rail Station,Yoga Studio,Auto Workshop,Spa,Farmers Market,Pizza Place,Fast Food Restaurant,Comic Shop,Park,Garden
0,CN Tower / King and Spadina / Railway Lands / Harbourfront West / Bathurst Quay / South Niagara / Island airport,Airport Service,Airport Lounge,Airport Terminal,Coffee Shop,Harbor / Marina,Sculpture Garden,Boutique,Bar,Boat or Ferry,Airport
2,Caledonia-Fairbanks,Park,Women's Store,Pool,Yoga Studio,Diner,Dance Studio,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant
0,Canada Post Gateway Processing Centre,Coffee Shop,Hotel,Sandwich Place,Burrito Place,Middle Eastern Restaurant,Mediterranean Restaurant,Gym,American Restaurant,Intersection,Fried Chicken Joint
0,Cedarbrae,Bank,Fried Chicken Joint,Hakka Restaurant,Athletics & Sports,Gas Station,Caribbean Restaurant,Thai Restaurant,Bakery,Dessert Shop,Dance Studio
0,Central Bay Street,Coffee Shop,Italian Restaurant,Café,Sandwich Place,Bubble Tea Shop,Burger Joint,Ice Cream Shop,Fried Chicken Joint,Salad Place,Restaurant
0,Christie,Grocery Store,Café,Park,Candy Store,Italian Restaurant,Diner,Restaurant,Baby Store,Coffee Shop,Nightclub
0,Church and Wellesley,Sushi Restaurant,Coffee Shop,Japanese Restaurant,Gay Bar,Restaurant,Yoga Studio,Men's Store,Pub,Hotel,Mediterranean Restaurant
0,Clarks Corners / Tam O'Shanter / Sullivan,Pizza Place,Chinese Restaurant,Fast Food Restaurant,Intersection,Thai Restaurant,Fried Chicken Joint,Bank,Pharmacy,Rental Car Location,Italian Restaurant
0,Cliffside / Cliffcrest / Scarborough Village West,Motel,American Restaurant,Yoga Studio,Discount Store,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Distribution Center
0,Commerce Court / Victoria Hotel,Coffee Shop,Café,Restaurant,Hotel,Gym,American Restaurant,Deli / Bodega,Japanese Restaurant,Italian Restaurant,Seafood Restaurant
0,Davisville,Pizza Place,Dessert Shop,Sandwich Place,Sushi Restaurant,Coffee Shop,Italian Restaurant,Gym,Café,Seafood Restaurant,Diner
0,Davisville North,Dance Studio,Park,Food & Drink Shop,Breakfast Spot,Gym,Department Store,Hotel,Sandwich Place,Dim Sum Restaurant,Deli / Bodega
0,Del Ray / Mount Dennis / Keelsdale and Silverthorn,Fast Food Restaurant,Museum,Sandwich Place,Restaurant,Caribbean Restaurant,Yoga Studio,Dim Sum Restaurant,Dance Studio,Deli / Bodega,Department Store
0,Don Mills,Japanese Restaurant,Coffee Shop,Beer Store,Gym,Restaurant,Asian Restaurant,Italian Restaurant,Caribbean Restaurant,Sandwich Place,Bike Shop
0,Dorset Park / Wexford Heights / Scarborough Town Centre,Indian Restaurant,Chinese Restaurant,Vietnamese Restaurant,Pet Store,Discount Store,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Diner
0,Downsview,Grocery Store,Park,Home Service,Athletics & Sports,Liquor Store,Discount Store,Business Service,Hotel,Baseball Field,Bank
0,Dufferin / Dovercourt Village,Pharmacy,Bakery,Park,Supermarket,Middle Eastern Restaurant,Bar,Gym / Fitness Center,Café,Grocery Store,Smoke Shop
2,East Toronto,Park,Coffee Shop,Metro Station,Convenience Store,Diner,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Discount Store
0,Eringate / Bloordale Gardens / Old Burnhamthorpe / Markland Wood,Cosmetics Shop,Coffee Shop,Shopping Plaza,Beer Store,Pet Store,Liquor Store,Pizza Place,Café,Convenience Store,Yoga Studio
0,Fairview / Henry Farm / Oriole,Clothing Store,Coffee Shop,Fast Food Restaurant,Restaurant,Bank,Women's Store,Food Court,Tea Room,Bakery,Bus Station
0,First Canadian Place / Underground city,Coffee Shop,Café,Hotel,Japanese Restaurant,Gym,Restaurant,Asian Restaurant,Deli / Bodega,American Restaurant,Seafood Restaurant
0,Forest Hill North & West,Jewelry Store,Trail,Sushi Restaurant,Mexican Restaurant,Donut Shop,Doner Restaurant,Dog Run,Distribution Center,Discount Store,Curling Ice
0,"Garden District, Ryerson",Clothing Store,Coffee Shop,Café,Cosmetics Shop,Middle Eastern Restaurant,Restaurant,Bubble Tea Shop,Japanese Restaurant,Hotel,Tea Room
3,Glencairn,Pizza Place,Japanese Restaurant,Pub,Yoga Studio,Diner,Dance Studio,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant
0,Golden Mile / Clairlea / Oakridge,Bakery,Bus Line,Metro Station,Park,Soccer Field,Ice Cream Shop,Intersection,Diner,Dessert Shop,Dim Sum Restaurant
0,Guildwood / Morningside / West Hill,Electronics Store,Mexican Restaurant,Breakfast Spot,Intersection,Medical Center,Bank,Rental Car Location,Construction & Landscaping,Convenience Store,Drugstore
0,Harbourfront East / Union Station / Toronto Islands,Coffee Shop,Aquarium,Café,Hotel,Scenic Lookout,Brewery,Restaurant,Sporting Goods Shop,Italian Restaurant,Fried Chicken Joint
0,High Park / The Junction South,Thai Restaurant,Café,Mexican Restaurant,Diner,Flea Market,Bar,Cajun / Creole Restaurant,Bakery,Fast Food Restaurant,Fried Chicken Joint
0,Hillcrest Village,Golf Course,Mediterranean Restaurant,Dog Run,Pool,Diner,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Discount Store
3,Humber Summit,Pizza Place,Yoga Studio,Discount Store,Dance Studio,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Distribution Center
0,Humberlea / Emery,Food Service,Baseball Field,Yoga Studio,Discount Store,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Distribution Center,Ethiopian Restaurant
2,Humewood-Cedarvale,Park,Hockey Arena,Field,Trail,Yoga Studio,Diner,Dance Studio,Deli / Bodega,Department Store,Dessert Shop
0,India Bazaar / The Beaches West,Fast Food Restaurant,Pizza Place,Sandwich Place,Italian Restaurant,Burrito Place,Steakhouse,Ice Cream Shop,Board Shop,Brewery,Restaurant
0,Kennedy Park / Ionview / East Birchmount Park,Coffee Shop,Discount Store,Bus Station,Hobby Shop,Department Store,Train Station,Dog Run,Distribution Center,Doner Restaurant,Curling Ice
0,Kensington Market / Chinatown / Grange Park,Café,Coffee Shop,Bakery,Vietnamese Restaurant,Mexican Restaurant,Grocery Store,Vegetarian / Vegan Restaurant,Dessert Shop,Bar,Gaming Cafe
0,Kingsview Village / St. Phillips / Martin Grove Gardens / Richview Gardens,Mobile Phone Shop,Bus Line,Pizza Place,Sandwich Place,Yoga Studio,Dim Sum Restaurant,Deli / Bodega,Department Store,Dessert Shop,Diner
0,Lawrence Manor / Lawrence Heights,Clothing Store,Furniture / Home Store,Accessories Store,Boutique,Event Space,Miscellaneous Shop,Carpet Store,Coffee Shop,Vietnamese Restaurant,Airport Terminal
2,Lawrence Park,Park,Swim School,Bus Line,Diner,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Discount Store,Electronics Store
0,Leaside,Coffee Shop,Sporting Goods Shop,Bank,Furniture / Home Store,Burger Joint,Electronics Store,Department Store,Brewery,Fish & Chips Shop,Sports Bar
0,Little Portugal / Trinity,Bar,Restaurant,Café,Asian Restaurant,Vietnamese Restaurant,Vegetarian / Vegan Restaurant,Men's Store,Yoga Studio,Japanese Restaurant,Cuban Restaurant
0,Malvern / Rouge,Fast Food Restaurant,Yoga Studio,Curling Ice,Dumpling Restaurant,Drugstore,Donut Shop,Doner Restaurant,Dog Run,Distribution Center,Discount Store
2,Milliken / Agincourt North / Steeles East / L'Amoreaux East,Park,Playground,Coffee Shop,College Gym,Curling Ice,Dumpling Restaurant,Drugstore,Donut Shop,Doner Restaurant,Dog Run
0,Mimico NW / The Queensway West / South of Bloor / Kingsway Park South West / Royal York South West,Hardware Store,Gym,Tanning Salon,Burger Joint,Social Club,Convenience Store,Bakery,Fast Food Restaurant,Discount Store,Grocery Store
4,Moore Park / Summerhill East,Playground,Yoga Studio,Discount Store,Dance Studio,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Distribution Center
0,New Toronto / Mimico South / Humber Bay Shores,Coffee Shop,Café,Pizza Place,Fast Food Restaurant,Bakery,Restaurant,Hobby Shop,Fried Chicken Joint,Mexican Restaurant,Pharmacy
2,North Park / Maple Leaf Park / Upwood Park,Park,Construction & Landscaping,Bakery,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Discount Store,Distribution Center,Dance Studio
0,North Toronto West,Clothing Store,Coffee Shop,Yoga Studio,Spa,Bagel Shop,Restaurant,Fast Food Restaurant,Mexican Restaurant,Sporting Goods Shop,Café
0,Northwest,Rental Car Location,Drugstore,Bar,Discount Store,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Yoga Studio
0,Northwood Park / York University,Massage Studio,Coffee Shop,Bar,Caribbean Restaurant,Discount Store,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Yoga Studio
0,Old Mill South / King's Mill Park / Sunnylea / Humber Bay / Mimico NE / The Queensway East / Royal York South East / Kingsway Park South East,Construction & Landscaping,Baseball Field,Distribution Center,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Discount Store,Yoga Studio,Dance Studio
0,Parkdale / Roncesvalles,Gift Shop,Cuban Restaurant,Breakfast Spot,Italian Restaurant,Dog Run,Bar,Dessert Shop,Restaurant,Bookstore,Eastern European Restaurant
0,Parkview Hill / Woodbine Gardens,Pizza Place,Pharmacy,Fast Food Restaurant,Café,Breakfast Spot,Athletics & Sports,Intersection,Pet Store,Bank,Gym / Fitness Center
2,Parkwoods,Park,Bus Stop,Food & Drink Shop,Diner,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Discount Store,Electronics Store
0,Queen's Park / Ontario Provincial Government,Coffee Shop,Sushi Restaurant,Diner,Yoga Studio,Discount Store,Bank,Bar,Café,Spa,Beer Bar
0,Regent Park / Harbourfront,Coffee Shop,Bakery,Pub,Park,Café,Theater,Restaurant,Breakfast Spot,Dessert Shop,Event Space
0,Richmond / Adelaide / King,Coffee Shop,Café,Restaurant,Thai Restaurant,Gym,Hotel,Clothing Store,American Restaurant,Deli / Bodega,Salad Place
2,Rosedale,Park,Trail,Playground,Yoga Studio,Dance Studio,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Diner
1,Roselawn,Garden,Yoga Studio,Diner,Dance Studio,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Discount Store,Cupcake Shop
0,Rouge Hill / Port Union / Highland Creek,History Museum,Bar,Yoga Studio,Discount Store,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Distribution Center,Dance Studio
0,Runnymede / Swansea,Pizza Place,Café,Coffee Shop,Pub,Italian Restaurant,Sushi Restaurant,Yoga Studio,Gastropub,Latin American Restaurant,Juice Bar
0,Runnymede / The Junction North,Grocery Store,Brewery,Bus Line,Pizza Place,Yoga Studio,Diner,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant
4,Scarborough Village,Convenience Store,Playground,Yoga Studio,Discount Store,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Distribution Center
0,South Steeles / Silverstone / Humbergate / Jamestown / Mount Olive / Beaumond Heights / Thistletown / Albion Gardens,Grocery Store,Pizza Place,Coffee Shop,Japanese Restaurant,Discount Store,Pharmacy,Beer Store,Sandwich Place,Fast Food Restaurant,Fried Chicken Joint
0,St. James Town,Coffee Shop,Café,Gastropub,Cocktail Bar,American Restaurant,Italian Restaurant,Clothing Store,Restaurant,Farmers Market,Seafood Restaurant
0,St. James Town / Cabbagetown,Restaurant,Coffee Shop,Bakery,Italian Restaurant,Café,Pizza Place,Pub,Beer Store,Jewelry Store,Pet Store
0,Steeles West / L'Amoreaux West,Fast Food Restaurant,Chinese Restaurant,Furniture / Home Store,Sandwich Place,Discount Store,Pizza Place,Supermarket,Pharmacy,Bank,Grocery Store
0,Stn A PO Boxes,Coffee Shop,Italian Restaurant,Seafood Restaurant,Café,Japanese Restaurant,Restaurant,Cocktail Bar,Hotel,Beer Bar,Creperie
0,Studio District,Café,Coffee Shop,Gastropub,Bakery,Brewery,American Restaurant,Seafood Restaurant,Sandwich Place,Pet Store,Cheese Shop
0,Summerhill West / Rathnelly / South Hill / Forest Hill SE / Deer Park,Coffee Shop,Pub,Sushi Restaurant,Liquor Store,Supermarket,Bank,Sports Bar,Pizza Place,Fried Chicken Joint,Restaurant
0,The Annex / North Midtown / Yorkville,Sandwich Place,Café,Coffee Shop,Pub,Flower Shop,History Museum,Middle Eastern Restaurant,Cosmetics Shop,Pizza Place,Pharmacy
2,The Beaches,Trail,Park,Pub,Health Food Store,Yoga Studio,Dance Studio,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant
0,The Danforth West / Riverdale,Greek Restaurant,Coffee Shop,Italian Restaurant,Bookstore,Furniture / Home Store,Ice Cream Shop,Caribbean Restaurant,Café,Dessert Shop,Pizza Place
2,The Kingsway / Montgomery Road / Old Mill North,Park,River,Cupcake Shop,Drugstore,Donut Shop,Doner Restaurant,Dog Run,Distribution Center,Discount Store,Diner
0,Thorncliffe Park,Indian Restaurant,Yoga Studio,Gym / Fitness Center,Bank,Fast Food Restaurant,Supermarket,Middle Eastern Restaurant,Pizza Place,Pharmacy,Restaurant
0,Toronto Dominion Centre / Design Exchange,Coffee Shop,Hotel,Café,Japanese Restaurant,Restaurant,American Restaurant,Deli / Bodega,Seafood Restaurant,Salad Place,Italian Restaurant
0,University of Toronto / Harbord,Café,Restaurant,Bar,Bookstore,Italian Restaurant,Japanese Restaurant,Bakery,Chinese Restaurant,Pub,Dessert Shop
0,Victoria Village,Coffee Shop,Grocery Store,Hockey Arena,Portuguese Restaurant,Yoga Studio,Diner,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant
0,Westmount,Pizza Place,Coffee Shop,Sandwich Place,Discount Store,Chinese Restaurant,Intersection,Distribution Center,Dog Run,Doner Restaurant,Curling Ice
2,Weston,Park,Convenience Store,Discount Store,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Distribution Center,Curling Ice
0,Wexford / Maryvale,Smoke Shop,Shopping Mall,Bakery,Auto Garage,Vietnamese Restaurant,Breakfast Spot,Sandwich Place,Middle Eastern Restaurant,Diner,Department Store
0,Willowdale,Coffee Shop,Pizza Place,Ramen Restaurant,Café,Sandwich Place,Restaurant,Grocery Store,Indonesian Restaurant,Electronics Store,Bank
0,Willowdale / Newtonbrook,Home Service,Yoga Studio,Discount Store,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Distribution Center,Curling Ice
0,Woburn,Coffee Shop,Korean Restaurant,Insurance Office,Distribution Center,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Discount Store,Dog Run
0,Woodbine Heights,Skating Rink,Dance Studio,Park,Beer Store,Video Store,Pharmacy,Cosmetics Shop,Curling Ice,Diner,Dim Sum Restaurant
0,York Mills / Silver Hills,Cafeteria,Martial Arts Dojo,Yoga Studio,Discount Store,Deli / Bodega,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Distribution Center
2,York Mills West,Park,Bank,Convenience Store,Discount Store,Department Store,Dessert Shop,Dim Sum Restaurant,Diner,Distribution Center,Dance Studio
"""

data = io.StringIO(data_string)
df = pd.read_csv(data, sep=",")

df.head()

df.dtypes

data_string2 = """Postal code,Borough,Neighborhood,Latitude,Longitude
M3A,North York,Parkwoods,43.7532586,-79.3296565
M4A,North York,Victoria Village,43.725882299999995,-79.31557159999998
M5A,Downtown Toronto,Regent Park / Harbourfront,43.6542599,-79.3606359
M6A,North York,Lawrence Manor / Lawrence Heights,43.718517999999996,-79.46476329999999
M7A,Downtown Toronto,Queen's Park / Ontario Provincial Government,43.6623015,-79.3894938
M9A,Etobicoke,Islington Avenue,43.6678556,-79.53224240000002
M1B,Scarborough,Malvern / Rouge,43.806686299999996,-79.19435340000001
M3B,North York,Don Mills,43.745905799999996,-79.352188
M4B,East York,Parkview Hill / Woodbine Gardens,43.7063972,-79.309937
M5B,Downtown Toronto,"Garden District, Ryerson",43.6571618,-79.37893709999999
M6B,North York,Glencairn,43.709577,-79.44507259999999
M9B,Etobicoke,West Deane Park / Princess Gardens / Martin Grove / Islington / Cloverdale,43.6509432,-79.55472440000001
M1C,Scarborough,Rouge Hill / Port Union / Highland Creek,43.7845351,-79.16049709999999
M3C,North York,Don Mills,43.72589970000001,-79.340923
M4C,East York,Woodbine Heights,43.695343900000005,-79.3183887
M5C,Downtown Toronto,St. James Town,43.6514939,-79.3754179
M6C,York,Humewood-Cedarvale,43.6937813,-79.42819140000002
M9C,Etobicoke,Eringate / Bloordale Gardens / Old Burnhamthorpe / Markland Wood,43.6435152,-79.57720079999999
M1E,Scarborough,Guildwood / Morningside / West Hill,43.7635726,-79.1887115
M4E,East Toronto,The Beaches,43.67635739999999,-79.2930312
M5E,Downtown Toronto,Berczy Park,43.644770799999996,-79.3733064
M6E,York,Caledonia-Fairbanks,43.6890256,-79.453512
M1G,Scarborough,Woburn,43.7709921,-79.21691740000001
M4G,East York,Leaside,43.7090604,-79.3634517
M5G,Downtown Toronto,Central Bay Street,43.6579524,-79.3873826
M6G,Downtown Toronto,Christie,43.669542,-79.4225637
M1H,Scarborough,Cedarbrae,43.773136,-79.23947609999999
M2H,North York,Hillcrest Village,43.8037622,-79.3634517
M3H,North York,Bathurst Manor / Wilson Heights / Downsview North,43.7543283,-79.4422593
M4H,East York,Thorncliffe Park,43.7053689,-79.34937190000001
M5H,Downtown Toronto,Richmond / Adelaide / King,43.65057120000001,-79.3845675
M6H,West Toronto,Dufferin / Dovercourt Village,43.66900510000001,-79.4422593
M1J,Scarborough,Scarborough Village,43.7447342,-79.23947609999999
M2J,North York,Fairview / Henry Farm / Oriole,43.7785175,-79.3465557
M3J,North York,Northwood Park / York University,43.7679803,-79.48726190000001
M4J,East York,East Toronto,43.685347,-79.3381065
M5J,Downtown Toronto,Harbourfront East / Union Station / Toronto Islands,43.6408157,-79.38175229999999
M6J,West Toronto,Little Portugal / Trinity,43.647926700000006,-79.4197497
M1K,Scarborough,Kennedy Park / Ionview / East Birchmount Park,43.7279292,-79.26202940000002
M2K,North York,Bayview Village,43.7869473,-79.385975
M3K,North York,Downsview,43.737473200000004,-79.46476329999999
M4K,East Toronto,The Danforth West / Riverdale,43.6795571,-79.352188
M5K,Downtown Toronto,Toronto Dominion Centre / Design Exchange,43.6471768,-79.38157640000001
M6K,West Toronto,Brockton / Parkdale Village / Exhibition Place,43.6368472,-79.42819140000002
M1L,Scarborough,Golden Mile / Clairlea / Oakridge,43.711111700000004,-79.2845772
M2L,North York,York Mills / Silver Hills,43.7574902,-79.37471409999999
M3L,North York,Downsview,43.7390146,-79.5069436
M4L,East Toronto,India Bazaar / The Beaches West,43.6689985,-79.31557159999998
M5L,Downtown Toronto,Commerce Court / Victoria Hotel,43.6481985,-79.37981690000001
M6L,North York,North Park / Maple Leaf Park / Upwood Park,43.713756200000006,-79.4900738
M9L,North York,Humber Summit,43.7563033,-79.56596329999999
M1M,Scarborough,Cliffside / Cliffcrest / Scarborough Village West,43.716316,-79.23947609999999
M2M,North York,Willowdale / Newtonbrook,43.789053,-79.40849279999999
M3M,North York,Downsview,43.7284964,-79.49569740000001
M4M,East Toronto,Studio District,43.6595255,-79.340923
M5M,North York,Bedford Park / Lawrence Manor East,43.7332825,-79.4197497
M6M,York,Del Ray / Mount Dennis / Keelsdale and Silverthorn,43.6911158,-79.47601329999999
M9M,North York,Humberlea / Emery,43.7247659,-79.53224240000002
M1N,Scarborough,Birch Cliff / Cliffside West,43.692657000000004,-79.2648481
M2N,North York,Willowdale,43.7701199,-79.40849279999999
M3N,North York,Downsview,43.7616313,-79.52099940000001
M4N,Central Toronto,Lawrence Park,43.7280205,-79.3887901
M5N,Central Toronto,Roselawn,43.7116948,-79.41693559999999
M6N,York,Runnymede / The Junction North,43.67318529999999,-79.48726190000001
M9N,York,Weston,43.706876,-79.51818840000001
M1P,Scarborough,Dorset Park / Wexford Heights / Scarborough Town Centre,43.7574096,-79.27330400000001
M2P,North York,York Mills West,43.752758299999996,-79.4000493
M4P,Central Toronto,Davisville North,43.7127511,-79.3901975
M5P,Central Toronto,Forest Hill North & West,43.6969476,-79.41130720000001
M6P,West Toronto,High Park / The Junction South,43.6616083,-79.46476329999999
M9P,Etobicoke,Westmount,43.696319,-79.53224240000002
M1R,Scarborough,Wexford / Maryvale,43.750071500000004,-79.2958491
M2R,North York,Willowdale,43.7827364,-79.4422593
M4R,Central Toronto,North Toronto West,43.7153834,-79.40567840000001
M5R,Central Toronto,The Annex / North Midtown / Yorkville,43.6727097,-79.40567840000001
M6R,West Toronto,Parkdale / Roncesvalles,43.6489597,-79.456325
M7R,Mississauga,Canada Post Gateway Processing Centre,43.6369656,-79.61581899999999
M9R,Etobicoke,Kingsview Village / St. Phillips / Martin Grove Gardens / Richview Gardens,43.6889054,-79.55472440000001
M1S,Scarborough,Agincourt,43.7942003,-79.26202940000002
M4S,Central Toronto,Davisville,43.7043244,-79.3887901
M5S,Downtown Toronto,University of Toronto / Harbord,43.6626956,-79.4000493
M6S,West Toronto,Runnymede / Swansea,43.6515706,-79.4844499
M1T,Scarborough,Clarks Corners / Tam O'Shanter / Sullivan,43.7816375,-79.3043021
M4T,Central Toronto,Moore Park / Summerhill East,43.6895743,-79.38315990000001
M5T,Downtown Toronto,Kensington Market / Chinatown / Grange Park,43.6532057,-79.4000493
M1V,Scarborough,Milliken / Agincourt North / Steeles East / L'Amoreaux East,43.8152522,-79.2845772
M4V,Central Toronto,Summerhill West / Rathnelly / South Hill / Forest Hill SE / Deer Park,43.68641229999999,-79.4000493
M5V,Downtown Toronto,CN Tower / King and Spadina / Railway Lands / Harbourfront West / Bathurst Quay / South Niagara / Island airport,43.6289467,-79.3944199
M8V,Etobicoke,New Toronto / Mimico South / Humber Bay Shores,43.6056466,-79.50132070000001
M9V,Etobicoke,South Steeles / Silverstone / Humbergate / Jamestown / Mount Olive / Beaumond Heights / Thistletown / Albion Gardens,43.739416399999996,-79.5884369
M1W,Scarborough,Steeles West / L'Amoreaux West,43.799525200000005,-79.3183887
M4W,Downtown Toronto,Rosedale,43.6795626,-79.37752940000001
M5W,Downtown Toronto,Stn A PO Boxes,43.6464352,-79.37484599999999
M8W,Etobicoke,Alderwood / Long Branch,43.60241370000001,-79.54348409999999
M9W,Etobicoke,Northwest,43.706748299999994,-79.5940544
M1X,Scarborough,Upper Rouge,43.836124700000006,-79.20563609999999
M4X,Downtown Toronto,St. James Town / Cabbagetown,43.667967,-79.3676753
M5X,Downtown Toronto,First Canadian Place / Underground city,43.6484292,-79.3822802
M8X,Etobicoke,The Kingsway / Montgomery Road / Old Mill North,43.653653600000005,-79.5069436
M4Y,Downtown Toronto,Church and Wellesley,43.6658599,-79.38315990000001
M7Y,East Toronto,Business reply mail Processing CentrE,43.6627439,-79.321558
M8Y,Etobicoke,Old Mill South / King's Mill Park / Sunnylea / Humber Bay / Mimico NE / The Queensway East / Royal York South East / Kingsway Park South East,43.6362579,-79.49850909999999
M8Z,Etobicoke,Mimico NW / The Queensway West / South of Bloor / Kingsway Park South West / Royal York South West,43.6288408,-79.52099940000001
"""

data2 = io.StringIO(data_string2)
df2 = pd.read_csv(data2, sep=",")
df2.head()

df2.dtypes

df2 = df2.join(df.set_index('Neighborhood'), on='Neighborhood')
#df2 = df2.merge(df,how = 'left', on='Neighborhood')

df2.head()

df2.dtypes

