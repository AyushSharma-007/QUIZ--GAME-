questions = ["What is the capital of Finland?","What is the name of Bridget Jones' baby in the third Bridget Jones film?",
             "Which five colours make up the Olympic rings?","In which decade was Madonna born?",
             "What is the most sold flavour of Walker's crisps?"]
options = [['Oulu','Helsinki','Kuopio',4
            'Jeonsu'],
           ["William","Armstrong","Stuart","Jinski"],
           ["Black, green, blue, white and red","Blue, green, orange, yellow and safforn","Black, green, blue, yellow and red","Black, grey, blue, yellow and pink"],
           ["The 1940s (1949)","The 1960s (1965)","The 1970s (1978)","The 1950s (1958)"],
           ["Cheese and Onion" ,"Cheese and pasta","tomato and Onion","Cheese and garlic"]]
correct = ['Helsinki','William','Black, green, blue, yellow and red','The 1950s (1958)','Cheese and Onion']
print("-----------WELCOME TO THE QUIZ----------")
count = 0;
p1 = (input("Enter the players name:"))
print("----------QUIZ BEGINS------")
for i in range(0,len(questions)):
    print()
    print("Questions",i+1)
    print(i+1,questions[i])
    print("Options:")
    for j in range(0,4):
        print('\t',j+1,options[i][j])
    right = int(input("Enter the correct options number :\n"))
    # print('i---->', i)
    # print('option i---->', options[i])
    if options[i][right-1] == correct[i]:
        print("Hence your option is correct\n")
        count += 10
    else:
        print("Incorrect")
        count -= 5

print("Hence you total score is :")
print(count)
