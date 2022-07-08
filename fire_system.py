import email_conf
import math,statistics
import time,json

from boltiot import Email,Bolt,Sms

maximum_limit = 25

mybolt = Bolt(email_conf.API_KEY, email_conf.DEVICE_ID)
mailer = Email(email_conf.MAILGUN_API_KEY,email_conf.SANDBOX_URL, email_conf.SENDER_EMAIL, email_conf.RECIPIENT_EMAIL)
sms = Sms(email_conf.SID, email_conf.AUTH_TOKEN, email_conf.TO_NUMBER, email_conf.FROM_NUMBER)
history_data = []
curr_time_seconds = time.time()
curr_time = time.ctime(curr_time_seconds)

while True: 

    response = mybolt.analogRead('A0')
    data = json.loads(response)
    if data['success'] != 1:
        print("There was an error while retriving the data.")
        print("This is the error:"+data['value'])
        time.sleep(10)
        continue

    print ("This is the value "+str(100*int(data['value'])/1024))
    sensor_value=0
    try:
        sensor_value = (100*int(data['value']))/1024
    except e:
        print("There was an error while parsing the response: ",e)
        continue


    try:
        if(sensor_value > maximum_limit):
             print("Indicator On")
             mybolt.digitalWrite('1','HIGH')

             print("Making request to mailgun to send an email")
             response = mailer.send_email("Alert","The room is on fire and temperature is "+str(sensor_value)+ " at time "+str(curr_time))
             response_text = json.loads(response.text)
             print("Response received from mailgun is:",str(response_text))
             print("Making request to twilio to send message")
             response = sms.send_sms("The room is on fire.The temperature is"+str(sensor_value)+"at time"+str(curr_time))
             print("Response received from twilio: "+str(response))
             print("Status of SMS at twilio is:"+str(response.status))


             print("Alarm On")
             mybolt.digitalWrite('0','HIGH')
    except Exception as e:
          print("Error occured below are details:")
          print(e)
          mybolt.digitalWrite('1','LOW')

    time.sleep(10) 