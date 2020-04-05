from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

global num,count
num = [1,2,3,4,5,6,7,8,9]
count = []
switchPlayer1 = True
switchPlayer2 = False
winner = False
draw = False

#初期化の関数
def init():
    global winner,draw,switchPlayer1,switchPlayer2
    winner = False
    draw = False
    count.clear()
    for i in range(0,9):
        num[i] = int(i+1)
    switchPlayer1 = True
    switchPlayer2 = False
    return()

#ゲームの勝敗の判定関数
def game_judge():
    global winner,draw
    #横のビンゴ
    if (num[0] == num[1]  and num[1] == num[2]) or (num[3] == num[4]  and num[4] == num[5]) or (num[6] == num[7]  and num[7] == num[8]):
        winner = True
    #縦のビンゴ
    elif (num[0] == num[3]  and num[3] == num[6]) or (num[1] == num[4]  and num[4] == num[7]) or (num[2] == num[5]  and num[5] == num[8]):
        winner = True
    #斜めのビンゴ
    elif (num[0] == num[4]  and num[4] == num[8]) or (num[2] == num[4]  and num[4] == num[6]):
        winner = True
    #引き分けスイッチ
    elif winner == False and len(count) == 9:
        draw = True
    #その他
    else:
        winner == False
    return()

#初期化のルーチン
@app.route('/init',methods=['GET'])
def retry():
    init()
    return redirect(url_for('main'))

#ゲームのスタート画面＆最初の画面
@app.route('/main')
def main():
    game_judge()
    return render_template('main.html', title='Flask GET request', num = num, switchPlayer1 = switchPlayer1, switchPlayer2 = switchPlayer2, winner = winner, draw = draw )

#場所の選択に対して、'○''×'の記入をするルーチン
@app.route('/edit/<i>',methods=['GET'])
def edit(i):
    global switchPlayer1
    global switchPlayer2

    
    if switchPlayer1 == True:
        num[int(i)-1] = '○'
        switchPlayer1 = False
        switchPlayer2 = True
    elif switchPlayer2 == True:
        num[int(i)-1] = '×'
        switchPlayer1 = True
        switchPlayer2 = False
    return redirect(url_for('counting'))

#引き分けのためのカウントを増やすルーチン
@app.route('/counting',methods=['GET'])
def counting():
    count.append(1)
    return redirect(url_for('main'))

#記号をクリックしてしまったときのルーチン
@app.route('/edit/○',methods=['GET'])
def pass1():
    return redirect(url_for('main'))

@app.route('/edit/×',methods=['GET'])
def pass2():
    return redirect(url_for('main'))


if __name__ == '__main__':
    app.run(debug=True)
