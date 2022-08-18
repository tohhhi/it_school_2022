from welcome_email import send_welcome_email


for i in []:
    try:
        send_welcome_email("11c.tohaneanu@gmail.com", "Tohaneanu Marian")
    except Exception as err:
        print(err)