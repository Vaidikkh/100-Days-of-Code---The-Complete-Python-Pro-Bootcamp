capital = {
    "France" :"Paris",
    "Germany" : "Berlin"

}
#travel_log = {
#    "France": ["Paris", "Lille", "Dijon"],
#    "Germany": ["Stuttgart", "Berlin"],
#}

#print(travel_log["France"][1])


nested_list = ["A","B", ["C","D"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "cities_visited" :["Paris", "Lille", "Dijon"],
        "no_of_times" : 3
    },
    "Germany":{
        "cities_visited" :["Stuttgart", "Berlin"],
        "no_of_times" : 3
    }
}

print(travel_log["Germany"]["cities_visited"][1], travel_log["France"]["cities_visited"])