programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over  and over again.",
    # 123: "hi , this is numeric value"
}
#print(programming_dictionary["Bug"])
#print(programming_dictionary[123])
#to add some info iin dict
programming_dictionary["array"] = "Array where we define something"

#print(programming_dictionary)

empty_dict = {}

#wipe an existing dict

#programming_dictionary = {}
#print(programming_dictionary)

#edit the dict
programming_dictionary["Bug"] = "a moth of computer"

#print(programming_dictionary)
#LOOP through a dict
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key] )
