# Practical-Traffic-Analysis-Attacks-on-Secure-Messaging-Applications

In this github repository we have concluded the article https://www.ndss-symposium.org/ndss-paper/practical-traffic-analysis-attacks-on-secure-messaging-applications/
in the Article Summary.docx.
Following the article, we carried out a study that examines the main idea of ​​the article

Introduction-

Instant Messaging IM applications such as Telegram, Signal, and WhatsApp have become extremely popular in recent years. IM services allow users to create social, private, and public groups and send messages of various types, including text messages, images, videos, and audio files.
In order to protect their customers, IM services deploy state-of-the-art encryption mechanisms (end-to-end or end-to-middle encryption) to secure user communications.
However, IM providers do not deploy mechanisms to obfuscate traffic characteristics (eg, timing and packet sizes).

event extraction-
Each event (e.g. a picture sent) produces a burst of packets in the encrypted traffic at very close time intervals. Other things such as notifications, handshakes, updates, etc. are scattered packets (not close in time) in small sizes. Therefore, we can detect events by looking at the packet bursts as described above, even though the information itself is encrypted.

We conducted our research in the Telegram app and wished to answer the following questions:
1. What are the differences between the sizes of the different packages when we send a regular text message, voice message, image, video, file, location and contact?
2. Is there a difference in the size of the packets between sending messages from the phone and sending messages from the laptop? 
3. When recording from computer A, is there a difference in the size of the packets between the messages sent from phone A (which is used by the recorder) and phone B?
4. Is there a difference between a forwarded message and a normal sent message?
5. Is there a difference between sending a white/black/color photo?
6. Is there a difference between "quiet" and "loud" recording?
7. Is there a difference in packet size between sending messages in a channel and a group?
8. 8. When recording from two computers and only one of them is in the target group and the other is not, will we be able to distinguish who is in the target group by sending inductive messages?
9. What are the differences in packet sizes between the traffic that goes through WhatsApp and Telegram?
10. Can we distinguish transmitted content even when there is constant background "noise"?

enjoy reading!

Instructions for running the plots:

  • Clone this repo
  
  • Change the argument in the display function to your desire csv file in plot_csv.py
  
  ![image](https://github.com/yeelacitron/Practical-Traffic-Analysis-Attacks-on-Secure-Messaging-Applications/assets/99408144/e0f00566-7ffd-41f6-8e9c-305c224cdbe1)
  
  make sure that if the csv is not in the same file as plot_csv.py to include the right path 
  
  • Run plot_csv.py to show the graphs

