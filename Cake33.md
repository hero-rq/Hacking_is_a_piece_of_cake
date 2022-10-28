심심풀이 삼아 Tryhackme anonymous를 풀어봅시당 
![어나니머스 00](https://user-images.githubusercontent.com/80503808/198506277-5a97da4b-d434-4cb5-bda7-70c0d90a282c.png)

일단 교양있게 포트 조사 부터 해줍니당 
139, 445 가 수상하니 더욱 파고들어도 좋습니당 
![어나니머스 01](https://user-images.githubusercontent.com/80503808/198506292-9185ee84-9cc5-4f1e-b49b-1d9f2722632c.png)

ftp를 이용해서 그쪽을 더 파고듭니당 

![어나니머스 02](https://user-images.githubusercontent.com/80503808/198506313-870f57ec-8d4f-43dd-9508-948467d8d1c2.png)

clean.sh에다가 python 리버스 쉘을 담아줍니당 그리고 그걸 ftp에서 put으로 다시 되돌려줍니당

 ![어나니머스 03](https://user-images.githubusercontent.com/80503808/198506327-0fb4658d-b36a-4c74-8a94-a5cab5cc5e28.png)

 ![어나니머스 04](https://user-images.githubusercontent.com/80503808/198506340-f291200a-23c9-4d56-ab30-8bec86d02171.png)

gtfobins에서 env를 찾아 그거에 알맞은 exploit을 파악한 뒤 root 권한을 획득합니당 
쉽습니당 
