global task1
def task1():
    intext_1 = int(input('Select a GSU Position:\n1. President\n2. GSU Officer\n3. Math Faculty Officer\n4. Science Faculty Officer\n5. Computing Faculty Officer\n6. Art Faculty Officer\n'))

    positions = ['President', 'GSU Officer', 'Math Faculty Officer', 'Science Faculty Officer', 'Computing Faculty Officer',
                 'Art Faculty Office']

    index_1 = 0
    for _ in positions:
        if positions[intext_1] == _:
            break
        index_1 += 1

    intext = input('Please input a candidates first name and last name')

    intext_2 = input('Please write your comment')

    candidates_1 = open('GSUCandidates.txt', 'r')
    comments = open('cnd_comments.txt', 'a')
    print(positions[index_1-1] +" "+ intext)
    for _ in candidates_1:
        if positions[index_1-1] +" "+ intext in _:
            comments.write(positions[index_1-1] +" "+ intext + " " + "'"+ intext_2 +"'"+ "\n")
            print("Your comment has been added")
            break
    else:
        print('That candidate does not exist or their name has been inputted incorrectly, Please check their name and selected position are correct')
