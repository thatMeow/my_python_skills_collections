import webbrowser

query = input("Please enter your keywords: ")
url = "https://www.google.com/?gws_rd=cr,ssl&ei=NCZFWIOJN8yMsgHCyLV4&fg=1#q={}".format(query)
webbrowser.open_new(url)
