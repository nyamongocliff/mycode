#! /usr/bin/env python3
import html



trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }
print()
question = trivia.get("question")
correct =  html.unescape(trivia.get("correct_answer"))
incorect = trivia.get("incorrect_answers")
incorect1 = html.unescape(incorect[0])
incorect2 = html.unescape(incorect[1])
incorect3 = html.unescape(incorect[-1])

print(f"{question:}")
print(f"Answers  ")
print(f"1 {correct}  ")
print(f"2 {incorect1}  ")
print(f"3 {incorect2}  ")
print(f"4 {incorect3}  ")



#print(question)
#print(correct)
#print(incorect2)


