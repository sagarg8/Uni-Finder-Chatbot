import random
print("Hello, I am University Decider ChatBot.")
intro = ["hi", "name", "who", "hey" , "hello", "help"] 
answer_intro = [" I am here to help you with the college application process and to answer any questions you may have about college.",
            " I have a lot of experience with the college application process, and I am familiar with the admissions process at many different colleges and universities.",
            " I am here to help you every step of the way, from choosing the right colleges to apply to, to writing your essays, to filling out your applications.",
            " I want to help you get into the college of your dreams, and I will do everything I can to help you reach your goals"]

why = ["why", "country"]
answer_why = ["You should do your degree in a different country because universities in other country will provide world-class education. The _____ has the better quality of education especially in ____course_____. Universities in the ____ focus more on practical knowledge than theoretical knowledge. Hence, you will be able to build a solid foundation and it will prepare you for the real world.",
        " You will be able to experience a new and unique culture. This will help you to gain a global perspective and it will give you a chance to meet people from all over the world.", 
        "You will complete my education in a more competitive and international atmosphere. Also a degree from the ______ is recognised and respected all over the world and it will help you to get into my dream job.", 
        "You have chosen the UK over other countries because the cost of living and education fees in other countries such as USA and Canada are higher. Also, UK is one of the safest and affordable country for students."]

which = ["which", "university"]
answer_which = ["My advice will be that you should do a lot of research about different universities, while researching your main focus should be on the quality of education and campus.Then you should short-listed 3 universities that you are interested in.",
        " You should like the course modules because they are up-to-date and contain actually what is needed in today’s world industry.",
        " The university has a student union known as CUSU, it is the center of student social life, with regular entertainment and social events such as club nights and live performances events throughout the academic year. They also have around 150 societies for students to join that cover everything from academic support to campaigning, language, gaming, charity, and much more. ",
        "You should short-listed 3 universities that you are interested in. Also it has a dedicated team of staff for exercise classes and gym.   "]

research = ["about", "research", "know", "importance"]
answer_research = ["So you should researched about their course modules, student life, accommodation and facilities they provide.",
                   " After comparing you should come to the conclusion that which university is meeting all the criteria that you are looking for and hence you should decide to go to that University for your degree. "
                   "So you should researched about their course modules, student life, accommodation and facilities they provide.",
                   " After comparing you should come to the conclusion that which university is meeting all the criteria that you are looking for and hence you should decide to go to that University for your degree. "]

after_course = ["after" ,"completion"]
answer_after_course =  ["After completion of the course you should return back to your home country  and should join the best Multinational companies in your home country.",
                        " Apply for different degree Or Look for jobs",
                        "After completion of the course you should return back to your home country  and should join the best Multinational companies in your home country.",
                        "Apply for different degree Or Look for jobs"]

accommodation = ["accommodation", "stay", "live"]
answer_accommodation = ["If the university accomodation is available then you should be using university accommodation ",
                        " You should look for a private accomodation near university",
                        "If the university accomodation is available then you should be using university accommodation ",
                        " You should look for a private accomodation near university"]

part_time_work = ["job", "work", "part" , "time"]
answer_part_time_work = ["An international student, you should work up to 20 hours a week during term time. ",
                         " You should not be doing part time work because your full intention is to study there and you should have enough funds to finance your living expenses. ",
                         "An international student, you should work up to 20 hours a week during term time. ",
                         " You should not be doing part time work because your full intention is to study there and you should have enough funds to finance your living expenses. "]  

answer_again = ["Oh! It appears you wrote something I don't understand yet",
        "Do you mind trying to rephrase that?",
        "I'm terribly sorry, I didn't quite catch that.",
        "I can't answer that yet, please try asking something else."]

conversation_question= [intro,why,which,research,after_course,accommodation,part_time_work]
conversation_answer = [answer_intro,answer_why,answer_which,answer_research,answer_after_course,answer_accommodation,answer_part_time_work]
    
while True:
    user_input = input("You: ").lower()
    user_list= user_input.split()
    
    random_answer = random.randint(0,3)
    
    def match_word(question):
         for i in user_list:
            for j in conversation_question[question]:
                if i == j: 
                     return(i)
    
    if match_word(0) in intro:
        uniBot = answer_intro[random_answer]
        print(uniBot)
    elif match_word(1) in why:
        uniBot = answer_why[random_answer]
        print(uniBot)
    elif match_word(2) in which:
        uniBot = answer_which[random_answer]
        print(uniBot)
    elif match_word(3) in research:
        uniBot = answer_research[random_answer]
        print(uniBot)
    elif match_word(4) in after_course:
        uniBot = answer_after_course[random_answer]
        print(uniBot)
    elif match_word(5) in accommodation:
        uniBot = answer_accommodation[random_answer]
        print(uniBot)
    elif match_word(6) in part_time_work:
        uniBot = answer_part_time_work[random_answer]
        print(uniBot)
    else:
        uniBot = answer_again[random_answer]
        print(uniBot)
    if user_input == "thank you" or "bye":
        print("Your Welcome :)")
        break