ft_list = ["Hello", "tata!"]
#a list is an ordered and mutable(can be modified after creation) collection of elements, 
#you can add remove and modify elements of list

ft_tuple = ("Hello", "toto!")
#a tuple is an ordered and immutable collection of elements
#like list but cannot change elements once created

ft_set = {"Hello", "tutu!"}
#a set is an unordered and mutuable collection of unique elements
#sets auto remove dup elements
#you can perform set op like union inter difference

ft_dict = {"Hello" : "titi!"}
#a dictionary is an unordered and mutuable collection of key_value pair
#allows you to associate values with keys and quickly look them up

#modify the string of each data object
ft_list[1] = "world"
ft_tuple = tuple(list(ft_tuple[:1]) + ["morocco!"])
# : allows you to extract a portion  of a sequence exclusively
ft_set = {"hello", "khouribga"}
ft_dict["Hello"] = "1337kh"



print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)