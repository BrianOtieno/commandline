action = input("Enter Action: ")

comments = [
    
]

data = {
    'user' : {'username' : 'Ian',
                    'password' : '1234',
                    'user_id' : 1
                    }
}

if action =="3":
    username = input("Enter username: ")
    for username in data['user']:
        comment = input("Enter Comment: ")

        comment_data = {
            'id' : len(comments)+1,
            'comment' : comment,
            'username' : data['user']['username']
        }
        comments.append(comment_data)

        print(comments)
        break
    
    


