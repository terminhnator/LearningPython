# import another_module
# print(another_module.another_variable)
#


# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("coral")
# timmy.fd(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()


from prettytable import PrettyTable

table = PrettyTable() ## Create new object
table.field_names = ["Pokemon Name", "Type"] ## Changing attributes
table.add_rows(                              ## Calling methods
    [
        ["Pikachu", "Electric"],
        ["Squirtle", "Water"],
        ["Charmander", "Fire"]
    ]
)

table.align = "l" ## Changing Attributes

print(table)
