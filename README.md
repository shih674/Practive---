# Practice--- 圖形版終極密碼 Ultimate Code with Graphic UI

總共劃分為三個主要畫面，分別是歡迎頁面、遊戲頁面、遊戲結束。
※注意；img資料夾和bgm資料夾要和執行檔放在同一層，否則會出現讀取錯誤!!!

There are three main frames in this program. WelcomePage, GamePage and Gameset.<br />
※Warning! Folder 'img' and 'bgm' must be placed in the same folder with "Ultimate Code.ipynb/Ultimate Code.py", and same level.To avoid loading error!!!
<br />
# [歡迎頁面 WelcomePage]遊戲的選單 Menu of the game 
    
![image](https://github.com/shih674/Practive---/blob/master/img/welcomeBG.jpg)

功能說明: 具有"開始遊戲"、"離開"兩個按鈕。  <br /> 
    開始遊戲 > 以滑鼠左鍵點擊後進入[遊戲頁面]  <br /> 
    離開 > 以滑鼠左鍵點擊後關閉視窗  <br /> 
    <br />
Describe: There are two buttons."開始遊戲"、"離開" <br />
    開始遊戲 > START GAME. After click the button, leading to [Game Page]  <br /> 
    離開 > EXIT. Use mouse to click, and exit window  <br />     

# [遊戲頁面 Game Page]遊戲進行的畫面 Frame while game on

![image](https://github.com/shih674/Practive---/blob/master/img/gameBG.jpg)

功能說明： <br />
    一、最上方為功能欄位，具有"重新開始"、"離開"兩個按鈕。<br />
        重新開始 > 以滑鼠左鍵點擊後遊戲重新開始，重置終極密碼<br />
        離開 > 以滑鼠左鍵點擊後關閉視窗<br />
    二、垂直中間為顯示部分，左、右圓形處顯示終極密碼的範圍，起始值為 0 ~ 100，左側為最小值、右側為最大值。<br />
        左右圓形中間的方形則為玩家輸入區，會顯示玩家輸入的值，玩家將使用下方的數字按鈕進行操控。<br />
    三、垂直下方為玩家操作區塊，玩家使用滑鼠左鍵選擇輸入的數字，再用"送出"送出結果，輸入錯誤則可以使用"退格"消去輸入中的最後一位數字，若輸入的數字超出範圍則沒有反應，反之則會根據玩家輸入的數字更新範圍(最大/最小值)。<br />
        0 到 9 > 輸入數字 0 到 9<br />
        退格 > 移除輸入的最後一位數字<br />
        送出 > 送出輸入的數字<br />
        <br />
Describe : <br />
    A. There are two button in fuctionial band."重新開始" and "離開"<br />
       重新開始 > Restart. After click this button,game restart and ultimate code will be reset.<br />
       離開 > EXIT. Use mouse to click, and exit window <br />
    B. It's show section in the middle of window. <br />
       In left circle, shows minimum of the range of ultimate code.<br />
       In right circle, shows maxmum of the range of ultimate code.<br />
       Rectangle is input from player.Player can insert number by number button below.<br />
    C. 0 to 9 : insert number 0 to 9<br />
       退格 > BACKSPACE. Remove rightest number in the input.<br />
       送出 > SEND. Send the number. If the number is in the range of ultimate code, range will update. But it's will be nothing happend if the number is out of range. <br />
       <br />
# [遊戲結束 Gameset]遊戲結束 Tell player the game is over

![image](https://github.com/shih674/Practive---/blob/master/img/bg.png)

功能說明:<br />
    按下"確定"之後，返回[歡迎畫面]。<br />
    火焰中將顯示引爆的終極密碼。<br /><br />
Describe:<br />
    After click "確定", return to [Welcome Page].<br />
    Ultimate number will show in fire.<br />
