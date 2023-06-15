# Blockchain
區塊鏈技術期末專案<br>
以下網址為執行UI介面時，所進行的交易內容<br>
https://mumbai.polygonscan.com/address/0xcc4769A4F0367d884177b041A7cd4E3bEF5Afa21

以下為 Remix IDE 智能合約的程式說明<br>
pragma solidity 0.5.17                  //使用Solidity編譯器版本為0.5.17 <br>
contract RewardsCalculator              //宣告合約名稱為「RewardsCalculator」<br>
// 分別宣告兩行類別為'address'及'uint'的public變數<br>
    address public Server               //Server用於儲存伺服器位址<br>
    address public Costomer             //Costomer用於儲存客戶位址<br>
    uint public Bonus                   //Bonus用於儲存獎金數量<br>
    uint public TotalRewards            //TotalRewards用於儲存總獎勵數量<br>                       
constructor(address costomer) public    //一個建構函式，在建立合約時會被呼叫。接受'costomer address'作為參數<br>
    Server = msg.sender                 // 'msg.sender'設為伺服器位址<br>
    Costomer = costomer                 // 'costomer'設為客戶位址<br>
    TotalRewards = 0                    // 'TotalRewards'初始化為0<br>
function AddBonus(uint cost) public     //一個公開函式，用於新增獎金<br>
    Bonus = cost                        //接受一個'cost'，將其賦值給'Bonus'<br>
    ComputeTotalRewards()               //呼叫'ComputeTotalRewards()'計算總獎勵<br>
function ComputeTotalRewards() private  //這是一個私有函式，用於計算總獎勵<br>
    TotalRewards += Bonus               //將'Bonus'的值加到'TotalRewards'中<br>
    
