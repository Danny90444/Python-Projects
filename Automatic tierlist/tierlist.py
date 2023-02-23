
#create dictionary to store shows as keys and rankings as values


show_dict = {"Avatar": [100,200,300]}
print(show_dict.values())

#prompt user for rankings based on show

''' nick_shows  = {}
for i in range(3):
    show = input("What show? ")
    rating = input ("what is the rating")

    nick_shows[show] = rating
print (nick_shows ) '''

nick_toons = ["avatar", "space Jam", "matrix"]
shows_nick = {}
for i in nick_toons:
    rating = int(input("What do you rate this show on a scale of 1 - 5 with 1 being didn't watch/don't know and 5 being it is a perfect show? {}:  ".format(i)))
    shows_nick[i] = rating

print (shows_nick)


#find average for votes 


#sort the dictionary by ranking values 



#display dictionary as table/import into tierlist maker 



'''


my_dict = {"foo": 100, "bar": 0, "baz": 200}
filtered_vals = [v for _, v in my_dict.items() if v != 0]
average = sum(filtered_vals) / len(filtered_vals)
print(average)

def solve(scores):
   avg_scores = dict()
   for name in scores:
      avg_scores[name] = sum(scores[name])/len(scores[name])
   return list(avg_scores.items())

scores = {'Amal' : [25,36,4000000007,45],'Bimal' : [85,74,69,47],'Tarun' : [65,35,87,14],'Akash' : [74,12,36,75]}
print(solve(scores))


# Define the dictionary
dict1 = {}
 
# Insert data into dictionary
dict1 = {1: ["Samuel", 21, 'Data Structures'],
         2: ["Richie", 20, 'Machine Learning'],
         3: ["Lauren", 21, 'OOPS with java'],
         }
 
# Print the names of the columns.
print("{:<10} {:<10} {:<10}".format('NAME', 'AGE', 'COURSE'))
 
# print each data item.
for key, value in dict1.items():
    name, age, course = value
    print("{:<10} {:<10} {:<10}".format(name, age, course)) '''