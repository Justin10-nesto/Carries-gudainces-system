
                if not re.search(special_sign_text1, password):
                    flag = -1
                    messages.info(request, "Weak password must contain a atleast 1 special character")

                if not re.search('0123456789', password):
                    flag = -1
                    messages.info(request, "Weak password must contain a atleast 1 digits")
