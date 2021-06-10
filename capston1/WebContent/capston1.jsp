<%@ page contentType="text/html; charset=utf-8"%>
<%@ page import = "java.util.*" %> 
<!DOCTYPE html>
<html>
<head>
	
	<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.6.2/jquery.min.js"> </script>
	<meta charset="UTF-8">
	<title>Insert title here</title>
	<link rel="stylesheet" href="css/bootstrap.css">
	<script type="text/javascript" src="js/bootstrap.js"></script>
	
	<script>

    $(function() {


   	var people = [];

   		$.getJSON('3)실시간_per_news.json', function(data) {
       		$.each(data, function(i, f) {
          		var Data = "<tr>" + "<th>"+ (i+1) + "</th>" + "<td>" + "<a href = " + "https://search.naver.com/search.naver?query=" + f.title + ">" + f.title + "</a>" + "</td>"  + "</tr>"
           		$(Data).appendTo("#userLank tbody");
	        if(i==20){
	        	return false;
	        }
          			
     		});

   		});

	});
	
	$(function() {


	   	var people = [];

	   		$.getJSON('1)실시간_naver_news.json', function(data) {
	       		$.each(data, function(i, f) {
	          		var Data = "<tr>" + "<th>"+ i + "</th>" + "<td>" + "<a href = " + f.link + ">" + f.title + "</a>" + "</td>"  + "</tr>"
	           		$(Data).appendTo("#userdata tbody");
		        if(i==10){
		        	return false;
		        }
	          			
	     	});

	   	});

	});
	
	
</script>
	
</head>
<body>
	<jsp:include page = "menu.jsp"/>
	
	<div class = "container">
		<div class = "row justify-content-md-center">
		
			<div class = "col col-sm-auto">
				<form method=get action="https://www.google.co.kr/search" target="_blank" >
					<table bgcolor="#FFFFFF">     
						<tr>       
							<td>           
								<input type=text name=q size=25 maxlength=255 value="" /> 
								<!-- 구글 검색 입력 창 -->          
								<input type=submit name=btnG value="Google 검색" /> 
								<!-- 검색 버튼 -->      
							</td>     
						</tr>   
					</table> 
				</form>
			</div>
		</div>
	</div>
	<div class = "container">
		<div class = "row">
			<div class = "col-3">
			
				<table class="table" id= "userLank">
				  <thead>
				    <tr>
				      <th scope="col">검색어 순위</th>
				      <th scope="col">검색어</th>
				    </tr>
				  </thead>
				  
				  <tbody>
				  </tbody>
				</table>
			
			</div>
			
			<div class = "col-1">
			</div>
			
			<div class = "col-8">
				
				<table class="table" id= "userdata">
				  <thead>
				    <tr>
				      <th scope="col">#</th>
				      <th scope="col">title</th>
				    </tr>
				  </thead>
				  
				  <tbody>
				  </tbody>
				</table>
				
			</div>
		</div>
	</div>
	<%--
	<div class="container">
      <!-- Example row of columns -->
      <div class="row">
        <div class="my-box">
          <div class="left">
           <h1 id="title">검색어 순위</h1>
           <table class="table table-bordered">
             <thead>
               <tr class="bg-info">
                 <th>rank</th>
                 <th>title</th>
                 <th>counts</th>
               </tr>
             </thead>
             <tbody id="table-body"></tbody>
           </table>
            
          <script src="issue.js"></script>
            
          </div>
          <div class="right">
              <div class="my-box2">
              <h1 id="title">뉴스</h1>
                 <table class="table table-bordered">
             		<thead>
		               <tr class="bg-info">
		                 <th>뉴스기사</th>
		                 <th>내용</th>
		                 <th>링크</th>
		                 
		               </tr>
             		</thead>
             		<tbody id="tablenews-body"></tbody>
          		 </table>
              </div>

          </div>
        </div>
      </div>
     </div>
     --%>
	<%--
	<script>
	$(document).ready(function() { 
		$.getJSON('/2)이슈_search_news.json', function(data) { 
   		var html = []; 
    
    		$.each(data, function(i, item) { 
    			html.push('<div >'); 
    			html.push('<h3 >' + item.counts + '</h3>'); 
    			html.push('<div >' + item.title + '</div>');
    
    			html.push('</div>'); html.push('</div>'); 
    			//html.push('<li id="' + key + '">' + val + '</li>'); 
    		}); 

		console.log(html); 
		$('#target').html(html.join('')); 
		}); 
	}); 
	 

		
	</script>
	--%>
</body>
</html>