# we are going to build the gui for the cookbook
# we are going to add the recipes
# we will display them on our screen
# try to use online recipes for the same
# once the user presses search, it pops up a new screen with relevant results or results with the same tag
# there is another button below the search button which has written on it "make recipe"
# the make recipe function brings up a new screen which says "make your own recipe"
# below the make your own recipe there will be and option for tags, name, main recipe, enter button
# this will make a new file in our sys which has the title as same as the tags
# the filename will be a number which will be a var which will have all the tags in it in a list
# if one of the tags is the same as the user searched, it will give us the options.
# fix the bug in the search engine to make it work
# make the search engine run by the titles of the files that are made by the make recipe button
# we are going to put the files as labels on the screen and show it to the user
# make the search bar work properly
# make the buttons bigger and add some decor to the program
# add the login system to this to make it an end to end application
# make the "make screen function work"
# once the user presses search, open another window whcih has all the search results in it
# we are done!....YAAY


import os
from tkinter import *
from PIL import ImageTk, Image

screen = Tk()
screen.title("Anitas cookbook")
screen.geometry("985x650")


def save():
    global title1
    global recipe1
    title1 = raw_title.get()
    recipe1 = raw_recipe.get()
    data = open(title1, "w")
    data.write(recipe1)
    data.close()

bg_small = PhotoImage(file='food.png')

def make_screen():
    global recipe1
    global raw_recipe
    global raw_title
    raw_title = StringVar()
    raw_recipe = StringVar()
    screen2 = Toplevel(screen)

    my_label1 = Label(screen2, image=bg_small)
    my_label1.place(x=0, y=0, relwidth=1, relheight=1)
    Label(screen2, text = "Title").pack()
    title1 = Entry(screen2, textvariable = raw_title,borderwidth=5).pack()
    Label(screen2, text="").pack()
    Label(screen2, text = "recipe").pack()
    recipe1 = Entry(screen2, textvariable = raw_recipe, borderwidth=5).pack()
    Button(screen2, text = "Enter", command = save, width=7, height=2).pack()


def save2():
    title1.append(recipe_list)
    print("working!")


def search():
    global index
    global recipe_list
    global search_list
    recpe_list_raw = os.listdir('/Users/puneet/PycharmProjects/cookbook')
    recipe_list = recpe_list_raw
    index = 0
    search_list = []
    search1 = raw_search.get()
    split_search = search1.split(" ")
    global result
    for recpies in recipe_list:
        index = index + 1
        split = recpies.split(" ")
        for keyword1 in split_search:
            for keyword2 in split:
                if keyword1.lower() == keyword2.lower():
                    search_list.append(index)
    print(len(search_list), "results found")
    for index in search_list:
        print(recipe_list[index - 1])
    result = recipe_list[index - 1]

def make_new_screen():
    screen3 = Toplevel(screen)
    real_result = open(result, "r")
    rr = real_result.read()
    print(rr)
    rf = (len(search_list), "results found")
    Label(screen3, text = rr).pack()


bg = PhotoImage(file="food_bg_img.png")

# create a label
my_label = Label(screen, image=bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)

raw_search = StringVar()
s = Entry(screen, width=75, textvariable=raw_search, borderwidth=10).pack()
Label(screen, text="Welcome to your cookbook Anita!", font = ("American Typewriter", 20)).pack()
Label(screen,
text="Here, you can login and write your own recipies, these recipies can be used by you again or can be used "
"by other users in this system", font = ("American Typewriter", 15)).pack()
Label(screen, text = "").pack()
my_pic0 = Image.open("create.png")
resized0=my_pic0.resize((215, 115), Image.ANTIALIAS)
new_pic0=ImageTk.PhotoImage(resized0)
make_recipe_button = Button(screen, image=new_pic0, command=make_screen, height=115, width=215).pack()
Label(screen, text = "").pack()
Label(screen, text = "").pack()
my_pic = Image.open("search.png")
resized=my_pic.resize((200, 100), Image.ANTIALIAS)
new_pic=ImageTk.PhotoImage(resized)
my_button = Button(screen, image=new_pic, command=search, height=100, width = 200, borderwidth=10).pack()
Label(screen, text = "").pack()
Label(screen, text="").pack()
my_pic1 = Image.open("show.png")
resized1=my_pic1.resize((200, 100), Image.ANTIALIAS)
new_pic1=ImageTk.PhotoImage(resized1)
Button(screen, image = new_pic1, command = make_new_screen, height=100, width = 200).pack()

# Program variables
text = "what"

def make_search_screen():
    screen1 = Toplevel(screen)

screen.mainloop()