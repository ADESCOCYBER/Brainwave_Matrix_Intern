.#Phishing URLDetector

#List of Known Phishing URLs

phishing_urls = ["revil.ru", "conti.ru", "nso.il", "doubledragon.cn", "ryuk.ru", "spam.com"]
# Prompt the user to enter the URL 
url = input("Enter the URL: ")

#Extract the domain from the URL 
domain = url.spilt ("//")[-1].spilt("/")[0]

#check the conditions

if domain in phishing_urls:
    print('Beware! This URL is known phishing URL.')
else:
    print('This URL does not apper to be a phishing URL. ')