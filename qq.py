import webbrowser
tabs = []
accounts = {}
user = input('Open Browse(yes/no): ')
#Test youtube link: https://www.youtube.com/watch?v=e3U1TKgwoxE or https://www.youtube.com/watch?v=xm2qGEEDsLw
#Test twitch link: https://www.twitch.tv/kaicenat
if user == 'yes':
    user = input('Open tab or close tab(close/open): ')
else:
    print('bye!')
while True:
    if user == 'open':
        user = input('which tab should open(youtube, twitch, odnoklassniki): ')
        tabs.append(user)
    elif user == 'close':
        user = input(f'Which tab should close tabs list:{tabs}(or u alredy close tab, write: open): ')
        tabs.remove(user)
    elif user == 'youtube':
        while True:
            register_or_login = input('register or login: ')
            if register_or_login == 'login':
                login = input('enter your username:')
                check = (accounts[login])
                password = input('enter your password: ')
                if check == password:
                        video = input('Insert the link to the video: ')
                        webbrowser.open_new_tab(video)
                        break
            else: 
                register_login = input('vvedite login: ')
                register_password = input('vvedite parol: ')

                accounts[register_login] = register_password
        
    elif user == 'twitch':
        stream = input('Insert the link to the stream: ')
        webbrowser.open_new_tab(stream)
        break
    elif user == 'odnoklassniki':
        profile = input('Insert the link to the profile: ')
        webbrowser.open_new_tab(profile)
        break
        
 




