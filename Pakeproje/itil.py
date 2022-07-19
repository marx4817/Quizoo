import os
import pickle
  
def kreyeQuiz(nonQuiz, nonbKesyon):
    rep_favorab =[]
    lis_kesyon ={}
    lis_Quiz ={}

    if isinstance(nonbKesyon, int):
        for i in range(nonbKesyon):
            kesyon =input("Antre kesyon an: ")
            print("Antre 4 repons pou kesyon ou an, antre bon repons lan avan...")
            a =1
            while a<=4:
                repons =input(f"Antre {a}e repons lan: ")
                rep_favorab.append(repons)
                a +=1
            lis_kesyon[kesyon] = rep_favorab

        #poun anrejistre quiz moun lan nan yon fichye...
        if os.path.exists("question"):
            listt_quiz=open("question","rb")
            li_quiz=pickle.load(listt_quiz)
            listt_quiz.close()

            lis_Quiz[nonQuiz] = lis_kesyon

            listt_quiz=open("question","wb")
            pickle.dump(lis_Quiz, listt_quiz)
            listt_quiz.close()
        else:
            lis_Quiz[nonQuiz] = lis_kesyon
            listt_quiz=open("question","wb")
            pickle.dump(lis_Quiz, listt_quiz)
            listt_quiz.close()
    else:
        raise valueError("saw antre a pa on antye")
        print("antre on nonb nan enteval 0 a 9")

def jweQuiz():
    listt_quiz=open("question","rb")
    lis_quiz=pickle.load(listt_quiz)
    listt_quiz.close()
    jedi=0
    for v in lis_quiz:
        jedi +=1
        print(f"{jedi}-{v}")

def meni():#fonksyon ki afiche meni pou itilizate an 
    print("1-Kreye quiz  \n2-Jwe quiz  \n3-Afiche sko itilizate  \n4-Kite")

    chwa =input("Fe yon chwa: ")

    if chwa=='1':
        nonQuiz= input("Antre non quiz: ")
        nonbKesyon= int(input("Antre kantite kesyon an: "))
        kreyeQuiz(nonQuiz, nonbKesyon)
    elif chwa=='2':
        jweQuiz()
        pass
    elif chwa =='3':
        pass
    elif chwa =='4':
        exit()
