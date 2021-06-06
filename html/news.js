var newsData=[
    
   
    {
        
        "description": "휘문중·고 농구부 출신 후배들도 중앙일보에 &quot;휘문중·고등학교 시절 현주엽은 모두의 롤모델일 정도로 일거수일투족이 공유됐기 때문에 그런 <b>이슈</b>가 있었다면 모를 수가 없었다&quot;며 현주엽을 둘러싼 논란에 선을 그었다.",
        "link": "<a href=\"https://www.sedaily.com/NewsView/22KXDXX4BL\">링크</a>",
        "title": "&quot;그는 현산군이었다&quot; 학폭 의혹 법적 대응한 현주엽, '고소인 조사' 경찰 출석"
    },
    {
        
        "description": "■ 기능성 침구류도 인기미세먼지 등 환경 <b>이슈</b>로 위생적인 실내 환경을 만들고자 집 안의 침구류를... 롯데백화점 관계자는 “최근 미세먼지 등 환경 <b>이슈</b>로 쾌적한 실내 환경을 만들려는 소비자가 늘었다”며 “집... ",
        "link": "<a href=\"http://www.kookje.co.kr/news2011/asp/newsbody.asp?code=0200&key=20210402.22013000420\">링크</a>",
        "title": "역대급 황사 기습에…공기청정기·기능성 침구 판매 ‘쑥쑥’"
    },
    {
        
        "description": "가덕신공항이 청년 일자리를 만든다 해도 승자독식과 각자도생이 만연한 사회가 그대로라면 문제는 해결되지 않는다.최근 한국토지주택공사(LH) 직원들의 부동산 투기 의혹이 <b>이슈</b>다. 부산시장 보궐선거 후보를 둘러싼... ",
        "link": "<a href=\"http://www.kookje.co.kr/news2011/asp/newsbody.asp?code=0300&key=20210402.22006000419\">링크</a>",
        "title": "김지현의 청년 관점 &lt;1&gt; 부산청년유권자행동의 도전"
    },
    {
        "description": "이번 보선 최대 <b>이슈</b>로 ‘지역경제 활성화’를 꼽은 응답자가 29.9%로 가장 많았고, ‘LH 땅투기 의혹(19.7... 리서치뷰 측은 “박형준 후보를 향한 여당의 검증 공세에도 불구하고 LH 사태가 부동산·불공정 <b>이슈</b>와... ",
        "link": "<a href=\"http://www.kookje.co.kr/news2011/asp/newsbody.asp?code=0100&key=20210402.33001000486\">링크</a>",
        "title": "김영춘 32% 박형준 57%…격차 더 벌어졌다"
    },
    {
        
        "description": "이찬복 입소스 본부장은 SBS에 &quot;최근 LH 직원 투기 의혹에 이어서 여권 인사의 임대료 인상 논란이 <b>이슈</b>화됐다&quot;며 &quot;지금 정부·여당에 느끼는 실망감이 표현된 것으로 보인다&quot;고 분석했다. 종합편성채널 JTBC가... ",
        "link":"<a href=\"https://www.dailian.co.kr/news/view/978363/?sc=Naver\">링크가기</a>",
        "title": "[4·7 재보선] 오세훈 50.5% 박영선 28.2%…지상파3사 여론조사"
    }


]

   buildTable(newsData)

            function buildTable(data){
              var table = document.getElementById('tablenews-body')

                for(var i= 0; i<data.length; i++){
                  var row =`<tr>
                                
                                <td>${data[i].title}</td>
                                <td>${data[i].description}</td>
                                 <td>${data[i].link}</td>
                            </tr>`
                            table.innerHTML +=row
                }
            }