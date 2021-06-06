var tableData=[               
                     {
                         "counts": 82,
                         "title": "쿠팡",
                          "rank" :"1",
                     },
                     {
                         "counts": 34,
                         "title": "개최",
                          "rank" :"2",
                     },
                     {
                         "counts": 33,
                         "title": "출범",
                          "rank" :"3",
                     },
                     {
                         "counts": 25,
                         "title": "자회사",
                          "rank" :"4",
                     },
                     {
                         "counts": 24,
                         "title": "국민은행",
                          "rank" :"5",
                     },
                     {
                         "counts": 23,
                         "title": "업무",
                          "rank" :"6",
                     },
                     {
                         "counts": 22,
                         "title": "실시간",
                          "rank" :"7",
                     },
                     {
                         "counts": 22,
                         "title": "협약",
                          "rank" :"8",
                     },
                     {
                         "counts": 21,
                         "title": "온라인",
                          "rank" :"9",
                     },
                     {
                         "counts": 21,
                         "title": "아이돌",
                          "rank" :"10",
                     },
            ]

            buildTable(tableData)

            function buildTable(data){
              var table = document.getElementById('table-body')

                for(var i= 0; i<data.length; i++){
                  var row =`<tr>
                                <td>${data[i].rank}</td>
                                <td>${data[i].title}</td>
                                <td>${data[i].counts}</td>
                            </tr>`
                            table.innerHTML +=row
                }
            }