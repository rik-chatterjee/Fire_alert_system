# Fire_alert_system
## Desciption
Fire accidents are happening a lot these days. Fire-related accidents have, on average, killed 35 people every day in the five years between 2016 and 2020, according to a report by Accidental Deaths and Suicides in India (ADSI), maintained by the National Crime Records Bureau. A large amount of these fire accidents happens in apartments or office buildings which results in loss of property and sometimes life. We can prevent this by stopping the spread of fire as early as possible. To do this I have created this device. 
### How this device solves the problem ?
- It notes the room temperature and as soon as the temperature crosses a particular critical temperature it rings an alarm.
- If there is no one in the room then it also sends an email and a message to the owners phone number with time.
- If message is send successfully then a led is lit on.
- If message is not able to send then led will not glow, which signifies that due to some error message and email was not able to send.
- The alarm and led will only be switched off by the clicking 'off' button on app.

## Schematics
<img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/07/image-6-1024x568.png">

## Product image and App image
<img src="https://projectsubmission.boltiot.com/wp-content/uploads/2022/07/IMG_20220708_1125001-487x1024.jpg" width="324" height="500"><img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiZmFx9G0iP4HarE6KdnOgyH7KxatXCDYUDNwz0vudMvC7Btn--bulJxyq1a2GssvouVEBcv7SEtqVJ5XlItK8jJ1SnA30Oddu3BrNFUzKEvpcTXdVayn_kTTJLXqNuk7W0k7OmrLtpaSIYIR7ZTjYQ8jZnB9T-F7dcwXGKC5-fL5MF723SKlXu0xrB7A/s320/IMG_20220707_213625.jpg">

## Components Used
### Hardware
Bolt Wifi Module
- LM35 Temperature sensor
- Buzzer
- Assorted Wires 
- Breadboard
- LED
- 10 kohm resistor
### Software
- Bolt Iot-Bolt Cloud
- Twilio - A third party messaging software for sending messages.
- Mailgun - A third party mailing software for sending mails.
- VMware - For running Ubuntu OS.
