from selenium import webdriver
import time

def make_file():
    print("It seems that you haven't created the 'login_info.py' file or maybe haven't added your number in it.")
    print("Let me help you with that!")
    number = input("Enter your phone number (without the country code): ")
    f = open("login_info.py","w")
    f.write("phone_number = " + number)
    f.close()

try:
    from login_info import phone_number
    if phone_number == "":
        make_file()
except Exception:
    make_file()
    from login_info import phone_number

class Bot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com') #Add website here
        time.sleep(2)

        try:
            login_with_phone = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')
        except Exception:
            time.sleep(2)
            login_with_phone = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/div[1]/button')
        login_with_phone.click()

        try:
            mobile_num_input = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')
        except Exception:
            time.sleep(2)
            mobile_num_input = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/div[2]/div/input')

        mobile_num_input.send_keys(phone_number)
        login_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        login_button.click()
        otp = input("Enter OTP Recieved: ")
        for i in range(len(otp)):
            temp = self.driver.find_element_by_xpath(f'//*[@id="modal-manager"]/div/div/div[2]/div[3]/input[{i+1}]')
            temp.send_keys(otp[i])
        continue_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button')
        continue_button.click()
        time.sleep(5)

        popup1 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        popup1.click()

        time.sleep(1)
        popup2 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        popup2.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[3]')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/button[1]')
        dislike_btn.click()

    def out_of_likes(self):
        out_of_likes = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]')
        print("You're out of Likes for today, try again in 12 hours.")

    def auto_swipe(self):
        while True:
            time.sleep(0.5)
            try:
                self.like()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    try:
                        self.close_match()
                    except Exception:
                        self.out_of_likes()

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = Bot()
bot.login()
bot.auto_swipe()
