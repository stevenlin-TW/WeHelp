- 要求三 
  + 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。
  ![螢幕快照 2022-10-20 01 00 42](https://user-images.githubusercontent.com/112813698/197306261-95a2f118-82d7-4a5b-afe5-069e054123d0.png)
  ![螢幕快照 2022-10-20 01 03 04](https://user-images.githubusercontent.com/112813698/197306302-14f7dd7e-adaa-4a1a-91b7-04c808166c67.png)
  ![螢幕快照 2022-10-22 08 03 04](https://user-images.githubusercontent.com/112813698/197306670-764e9aed-1ccb-4738-b40c-a431768603c3.png)
  ![螢幕快照 2022-10-22 08 02 54](https://user-images.githubusercontent.com/112813698/197306672-f380db22-67e6-4d39-a6ec-b02a85de834c.png)

  + 使用 SELECT 指令取得所有在 member 資料表中的會員資料。
  ![螢幕快照 2022-10-22 08 02 37](https://user-images.githubusercontent.com/112813698/197306696-00d80a7b-b324-4986-93cf-9ed102cd976c.png)

  + 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。
  ![螢幕快照 2022-10-22 08 05 40](https://user-images.githubusercontent.com/112813698/197306829-c37ebbf4-4a6a-4b64-b8fa-a5766607749a.png)

  + 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
  ![螢幕快照 2022-10-22 08 08 17](https://user-images.githubusercontent.com/112813698/197306968-c115802f-4ad9-430d-8486-005900e991af.png)

  + 使用 SELECT 指令取得欄位 username 是 test 的會員資料。
  ![螢幕快照 2022-10-22 08 10 04](https://user-images.githubusercontent.com/112813698/197307063-6a2495da-f6a2-48ca-8a7f-5a04edaed1af.png)

  + 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。
  ![螢幕快照 2022-10-22 08 10 56](https://user-images.githubusercontent.com/112813698/197307102-bc1082f2-caed-43a8-bcc9-e159cf24806e.png)

  + 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。
  ![螢幕快照 2022-10-20 19 30 20](https://user-images.githubusercontent.com/112813698/197307164-c335b85a-ebd1-41a0-99dd-7342d1a961a2.png)

- 要求四
  + 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。
  ![螢幕快照 2022-10-22 08 15 22](https://user-images.githubusercontent.com/112813698/197307334-91cbf93e-d35c-47a3-8348-40f3017197ee.png)

  + 取得 member 資料表中，所有會員 follower_count 欄位的總和。
  ![螢幕快照 2022-10-22 08 16 20](https://user-images.githubusercontent.com/112813698/197307375-1d1838a5-ae4b-4203-b02f-8030b0a06024.png)

  + 取得 member 資料表中，所有會員 follower_count 欄位的平均數。
  ![螢幕快照 2022-10-22 08 17 12](https://user-images.githubusercontent.com/112813698/197307422-3b82df27-0dcb-48a4-bef6-093eb9867de3.png)

- 要求五
  + 新增資料表 message
  ![螢幕快照 2022-10-22 00 28 01](https://user-images.githubusercontent.com/112813698/197307470-5e1d0f04-71c1-4cb0-b5d9-592a834f7c3c.png)

  + 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名。
  ![螢幕快照 2022-10-22 08 23 12](https://user-images.githubusercontent.com/112813698/197307889-3b640554-411f-4b32-b972-0887c491725e.png)
  
  + 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名。
  ![螢幕快照 2022-10-22 08 24 22](https://user-images.githubusercontent.com/112813698/197307957-04d0d7f0-6df5-42bd-979c-b7a040cc66de.png)

  + 使用 SELECT、SQL Aggregate Functions 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言平均按讚數。
  ![螢幕快照 2022-10-22 08 27 04](https://user-images.githubusercontent.com/112813698/197308082-f727dccf-63a2-46ca-aee4-f8f1c91a9272.png)







