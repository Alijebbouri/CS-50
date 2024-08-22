# def linear_search(number):
#     arr = [20,50,100,30,10,1,25,40,49]
#     for i in range(len(arr)):
#         if arr[i] == number:
#             return "found at index",i
#     return 'not found'
# n = int(input('type 1.. 100 : '))
# print(linear_search(n))


def get_phone(nom):
    persons = [
        {'name': 'John', 'phone': '12345678'},
        {'name': 'Jane', 'phone': '2345678'},
        {'name': 'Alice', 'phone': '345678'},
        {'name': 'Bob', 'phone': '45678'},
        {'name': 'Charlie', 'phone': '5678'},
        {'name': 'David', 'phone': '678'},
        {'name': 'Eva', 'phone': '7222228'},
        {'name': 'Fred', 'phone': '122228'},
    ]
    for i in range(len(persons)):
        if(persons[i]["name"] == nom):
            return f"The phone number is: {persons[i]['phone']}"
    return 'not found'
search_name = input('type a name : ')
print(get_phone(search_name))