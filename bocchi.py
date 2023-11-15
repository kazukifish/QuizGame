import random
# Class
class Band:
    # Constructor
    def __init__(self, guitar="後藤ひとり", dram="伊地知虹夏", base ="山田リョウ", vocal="喜多郁代"):
        self.guitar = guitar
        self.dram = dram
        self.base = base
        self.vocal = vocal
    # Method1   
    def memberProduce(self):
        print(f"結束バンドのギターは{self.guitar}です。")
        print(f"結束バンドのドラムは{self.dram}です。")
        print(f"結束バンドのベースは{self.base}です。")
        print(f"結束バンドのボーカルは{self.vocal}です。")
    # Method2
    @staticmethod
    def quiz(pointHistory = []):
        point = 0
        print("問題数は四問です。回答したら、エンターキーを押してください。")
        quiz_list = ["結束バンドのロゴTは誰がデザインした？",
                     "後藤家が飼っている犬の名前は？",
                     "ぼっちというあだ名は誰がつけた？",
                     "喜多ちゃんの陽キャオーラの擬音語は？",
                     "虹夏ちゃんの姉の名前は？",
                     "喜多ちゃんは結束バンドの何大臣？"]
        
        answer_list = [["伊地知", "伊地知虹夏", "虹夏", "虹夏ちゃん"],
                       ["ジミヘン", "じみへん"],
                       ["山田リョウ", "リョウさん", "リョウ", "山田","山田りょう", "りょう"],
                       ["きたーん", "キターン", "ｷﾀｰﾝ"],
                       ["星歌", "伊地知星歌"],
                       ["イソスタ", "ｲｿｽﾀ"]]
        
        id = []
        for i in range(len(quiz_list)):
            id.append(i)
        random.shuffle(id)

        # First quiz
        try:
            print("【第一問】")
            quiz_1 = input(quiz_list[id[0]])
            if quiz_1 in answer_list[id[0]]:
                print("正解！")
                point += 25
            else:
                print("残念！")
        except:
            print("errorが発生したようです。")
        else:
            print("次の問題に行きましょう！")   
            
        try:
            print("【第二問】")
            quiz_2 = input(quiz_list[id[1]])
            if quiz_2 in answer_list[id[1]]:
                print("正解！")
                point += 25
            else:
                print("残念！")
        except:
            print("errorが発生したようです。")
        else:
            print("次の問題に行きましょう！")   
        
        try:
            print("【第三問】")
            quiz_3 = input(quiz_list[id[2]])
            if quiz_3 in answer_list[id[2]]:
                print("正解！")
                point += 25
            else:
                print("残念！")
        except:
            print("errorが発生したようです。")
        else:
            print("次の問題に行きましょう！")   
        
        # Lazt quiz
        try:
            print("【第四問】")
            quiz_4 = input(quiz_list[id[3]])
            if quiz_4 in answer_list[id[3]]:
                print(f"正解！")
                point += 25
            else:
                print("残念！")
        except:
            print("errorが発生したようです。")
        else:
            print("お疲れ様でした！") 
        finally:
            print(f"あなたの正解率は{point}パーセントでした！")
            
        pointHistory.append(point)
        #  Return Value 
        return pointHistory 
    
    def quizStart(self):
        try:
            challenger = int(input("挑戦者の人数を入力してください。"))
            for _ in range(challenger):
                print(Band.quiz()) # print()関数をつけないとReturnが反映されない
        except ValueError as ve:
            print(ve, "数字以外が入力されました。")
        else:
            print("楽しめましたか？？")

# Test Code
if __name__ == '__main__':
    band = Band()
    band.quizStart()

        

    
