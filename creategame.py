from bs4 import BeautifulSoup

name=input("Game name?: ")
filedir = "play/" + name.lower().replace(' ', '-')+".html"
print(filedir)
cat = input("What category?: ")
url=input("Game URL: ")
thumb=input("Thumbnail url: ")


with open('directory.html', 'r') as file:
    html_content= file.read()

soup = BeautifulSoup(html_content, 'html.parser')

div = soup.find('div', class_='grid-container')

element_string=f'''
<div class="col-lg-4 col-md-6 grid-2">
						<a href="{filedir}">
							<div class="game-item">
								<div class="list-game">
									<div class="list-thumbnail"><img
											src="{thumb}"
											data-src="{thumb}"
											class="small-thumb img-rounded lazyload"></div>
									<div class="list-info">
										<div class="list-title">{name}</div>
										<div class="list-category"></div>

									</div>
								</div>
							</div>
						</a>
					</div>
'''

new_element = BeautifulSoup(element_string, 'html.parser')

div.insert(0, new_element)

with open('directory.html', 'w') as directory:
    directory.write(soup.prettify())

with open('category/'+cat+".html", "r") as catfile:
    html_content=catfile.read()

soup = BeautifulSoup(html_content, 'html.parser')

div = soup.find('div', class_='grid-container')

element_string=f'''
<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/{filedir}">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="{thumb}" data-src="{thumb}" class="lazyload" alt="{name}"></div>
    </div>
  </div>
  </a>
</div>
'''

new_element = BeautifulSoup(element_string, 'html.parser')

div.insert(0, new_element)

with open('category/'+cat+".html", "w") as catfile:
    catfile.write(soup.prettify())

with open(filedir, 'w') as game:
    game.write(f'''<!DOCTYPE html>
<html lang="en" dir="ltr">
	<head>

		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
		<title>{name}  - rusk-games.pages.dev</title>
    <meta name="robots" content="noindex,nofollow" />
		<meta name="description" content="{name} - rusk-games.pages.dev: on Chromebook delivers seamless, lag-free gaming with an optimized interface, ensuring an enjoyable and safe experience for players of all ages">
    <link rel="icon" href="../images/favicon.ico" sizes="32x32">


      <meta property="og:image:width" content="200 px" />
      <meta property="og:image:height" content="200 px" />
      <meta property="og:title" content="{name}" />
      <meta property="og:site_name" content="{name}" />
      <meta property="og:description" content="{name} - rusk-games.pages.dev: on Chromebook delivers seamless, lag-free gaming with an optimized interface, ensuring an enjoyable and safe experience for players of all ages" />
      <meta property="og:type" content="website" />
      <meta property="og:image" content="{thumb}">



  	<style type="text/css">
.report-modal {{
  display: none;
  position: fixed;
  z-index: 20;
  padding-top: 100px;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  overflow: auto;
  background-color: rgb(0,0,0);
  background-color: rgba(0,0,0,0.4);
}}
.report-modal-content {{
  background-color: #fefefe;
  color: #000;
  margin: auto;
  padding: 20px;
  border: 1px solid #888;
  max-width: 320px;
}}
.close {{
  color: #aaaaaa;
  float: right;
  font-size: 28px;
  font-weight: bold;
}}
.close:hover,.close:focus {{
  color: black;
  text-decoration: none;
  cursor: pointer;
}}
.report-label {{
  padding: 0 10px;
  margin-right: 5px;
  border-radius: 15px;
  display: inline-block;
  margin-bottom: 8px;
}}
</style>
		<link rel="stylesheet" type="text/css" href="../css/bootstrap.min.css" />
		<link rel="stylesheet" type="text/css" href="../css/jquery-comments.css" />
		<link rel="stylesheet" type="text/css" href="../css/user.css" />
		<link rel="stylesheet" type="text/css" href="../css/style.css" />
		<link rel="stylesheet" type="text/css" href="../css/custom.css" />
		<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.3/font/bootstrap-icons.css" />
		<!-- Font Awesome icons (free version)-->
		<link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
		<!-- Google fonts-->
		<link rel="preconnect" href="https://fonts.googleapis.com">
		<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
		<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap" rel="stylesheet">



<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-VZRYLR5KM1"></script>









</head>
	<body id="page-top" style="background: url('../images/background1.png'); background-size: cover;">


<!-- Navigation-->
		   <div id="nav-placeholder"></div>
<script src="https://ajax.aspnetcdn.com/ajax/jQuery/jquery-3.7.1.js"></script>
  <script type="text/javascript" src="../navbar.js"></script>
		









<div class="container game-wrapper">
<div style="padding-bottom: 20px">
     <!-- ads_ngang-->
   
</div>





  <div class="row">
      <div class="col-md-9">
          	<div class="game-container">
          		<div class="game-content" data-id="169">
          			<div id="allow_mobile_version"></div>			
               <!-- 
                <div id="mobile-play" style="display: none;">
          				<div class="mobile-thumb-play">
          					<img src="#">
          				</div>
          				<div id="mobile-play-btn">
          					<i class="bi bi-play-circle-fill"></i>
          				</div>
          			</div> -->



          			<div class="game-iframe-container" id="game-player">
          				<div id="mobile-back-button" draggable="true">
          					<i class="bi bi-x-circle-fill"></i>
          				</div>
          				<iframe class="game-iframe" id="game-area" src="{url}" width="480" height="800" scrolling="none" frameborder="0" allowfullscreen></iframe>
          			</div>
          		</div>


          		<div class="game-info">
          			<div class="header-left">
          				<h1 class="single-title">{name}</h1>


          			</div>
          			<div class="header-right">


          				<div class="b-action2">
          		
          					<a href="#" onclick="open_fullscreen()" class="btn btn-capsule"><i class="bi bi-arrows-fullscreen b-icon"></i>Fullscreen</a>
          				</div>
          			</div>
          		</div>
          	</div>

      </div><!-- end col-9 -->
      

      <div class="col-md-3">
        <div style="">
          <!-- ads_doc -->
    
        </div>
      </div>


  </div><!-- end row -->


</div> <!-- end row container game-wrapper-->







<div class="container">

            <div class="banner-ad-wrapper">
              <div class="banner-ad-content" style="padding: 20px 0; text-align: center;">




              </div>
            </div>





	<div class="content-wrapper">
		<div class="row">
			

			<div class="col-md-5">
				<div class="sidebar">
	











</div>			



</div>
</div>
</div>




	<div class="bottom-container">
		<h2 class="item-title">You might also Like</h2>
		<div class="row">

<!-- 

<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/age-of-war.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/age-of-war.png" data-src="https://htmlxm.github.io/thumb/age-of-war.png" class="lazyload" alt="{name}"></div>
      <div class="list-info">
        <div class="list-title">{name}</div>
      </div>
    </div>
  </div>
  </a>
</div>  

 -->






<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/city-car-driving-stunt-master.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/city-car-driving-stunt-master.png" data-src="https://htmlxm.github.io/thumb/city-car-driving-stunt-master.png" class="lazyload" alt="City Car Driving: Stunt Master"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/top-speed-3d.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/top-speed-3d.png" data-src="https://htmlxm.github.io/thumb/top-speed-3d.png" class="lazyload" alt="Top Speed 3d"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/subway-surfers-newyork.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/subway-surfers-newyork.png" data-src="https://htmlxm.github.io/thumb/subway-surfers-newyork.png" class="lazyload" alt="Subway Surfers Newyork"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/smash-karts.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/smash-karts.png" data-src="https://htmlxm.github.io/thumb/smash-karts.png" class="lazyload" alt="Smash Karts"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/drift-hunters.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/drift-hunters.png" data-src="https://htmlxm.github.io/thumb/drift-hunters.png" class="lazyload" alt="Drift Hunters"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/monster-tracks.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/monster-tracks.png" data-src="https://htmlxm.github.io/thumb/monster-tracks.png" class="lazyload" alt="Monster Tracks"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/rocket-soccer-derby.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/rocket-soccer-derby.png" data-src="https://htmlxm.github.io/thumb/rocket-soccer-derby.png" class="lazyload" alt="Rocket Soccer Derby"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/idle-digging-tycoon.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/idle-digging-tycoon.png" data-src="https://htmlxm.github.io/thumb/idle-digging-tycoon.png" class="lazyload" alt="Idle Digging Tycoon"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/moto-road-rash-3d.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/moto-road-rash-3d.png" data-src="https://htmlxm.github.io/thumb/moto-road-rash-3d.png" class="lazyload" alt="Moto Road Rash 3D"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/football-legends.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/football-legends.png" data-src="https://htmlxm.github.io/thumb/football-legends.png" class="lazyload" alt="Football Legends"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/top-speed-racing-3d.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/top-speed-racing-3d.png" data-src="https://htmlxm.github.io/thumb/top-speed-racing-3d.png" class="lazyload" alt="Top Speed Racing 3d"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/stick-defenders.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/stick-defenders.png" data-src="https://htmlxm.github.io/thumb/stick-defenders.png" class="lazyload" alt="Stick Defenders"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/battle-wheels.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/battle-wheels.png" data-src="https://htmlxm.github.io/thumb/battle-wheels.png" class="lazyload" alt="Battle Wheels"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/merge-cyber-racers.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/merge-cyber-racers.png" data-src="https://htmlxm.github.io/thumb/merge-cyber-racers.png" class="lazyload" alt="Merge Cyber Racers"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/penalty-shooters-2.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/penalty-shooters-2.png" data-src="https://htmlxm.github.io/thumb/penalty-shooters-2.png" class="lazyload" alt="Penalty Shooters 2"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/master-chess.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/master-chess.png" data-src="https://htmlxm.github.io/thumb/master-chess.png" class="lazyload" alt="Master Chess"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/blumgi-slime.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/blumgi-slime.png" data-src="https://htmlxm.github.io/thumb/blumgi-slime.png" class="lazyload" alt="Blumgi Slime"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/tunnel-rush.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/tunnel-rush.png" data-src="https://htmlxm.github.io/thumb/tunnel-rush.png" class="lazyload" alt="Tunnel Rush"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/red-ball-4.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/red-ball-4.png" data-src="https://htmlxm.github.io/thumb/red-ball-4.png" class="lazyload" alt="Red Ball 4"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/soccer-skills-world-cup.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/soccer-skills-world-cup.png" data-src="https://htmlxm.github.io/thumb/soccer-skills-world-cup.png" class="lazyload" alt="Soccer Skills World Cup"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/tag.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/tag.png" data-src="https://htmlxm.github.io/thumb/tag.png" class="lazyload" alt="Tag"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/the-impossible-quiz.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/the-impossible-quiz.png" data-src="https://htmlxm.github.io/thumb/the-impossible-quiz.png" class="lazyload" alt="The Impossible Quiz"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/football-masters.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/football-masters.png" data-src="https://htmlxm.github.io/thumb/football-masters.png" class="lazyload" alt="Football Masters"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/crazy-cars.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/crazy-cars.png" data-src="https://htmlxm.github.io/thumb/crazy-cars.png" class="lazyload" alt="Crazy Cars"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/stick-merge.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/stick-merge.png" data-src="https://htmlxm.github.io/thumb/stick-merge.png" class="lazyload" alt="Stick Merge"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/stickman-climb-2.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/stickman-climb-2.png" data-src="https://htmlxm.github.io/thumb/stickman-climb-2.png" class="lazyload" alt="Stickman Climb 2"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/stickman-bike.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/stickman-bike.png" data-src="https://htmlxm.github.io/thumb/stickman-bike.png" class="lazyload" alt="Stickman Bike"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/rooftop-snipers.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/rooftop-snipers.png" data-src="https://htmlxm.github.io/thumb/rooftop-snipers.png" class="lazyload" alt="Rooftop Snipers"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/escaping-the-prison.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/escaping-the-prison.png" data-src="https://htmlxm.github.io/thumb/escaping-the-prison.png" class="lazyload" alt="Escaping The Prison"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/blumgi-rocket.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/blumgi-rocket.png" data-src="https://htmlxm.github.io/thumb/blumgi-rocket.png" class="lazyload" alt="Blumgi Rocket"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/moto-x3m.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/moto-x3m.png" data-src="https://htmlxm.github.io/thumb/moto-x3m.png" class="lazyload" alt="Moto X3m"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/raft-wars.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/raft-wars.png" data-src="https://htmlxm.github.io/thumb/raft-wars.png" class="lazyload" alt="Raft Wars"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/moto-x3m-winter.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/moto-x3m-winter.png" data-src="https://htmlxm.github.io/thumb/moto-x3m-winter.png" class="lazyload" alt="Moto X3m Winter"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/brain-test-tricky-puzzles.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/brain-test-tricky-puzzles.png" data-src="https://htmlxm.github.io/thumb/brain-test-tricky-puzzles.png" class="lazyload" alt="Brain Test: Tricky Puzzles"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/swingo.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/swingo.png" data-src="https://htmlxm.github.io/thumb/swingo.png" class="lazyload" alt="Swingo"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/merge-round-racers.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/merge-round-racers.png" data-src="https://htmlxm.github.io/thumb/merge-round-racers.png" class="lazyload" alt="Merge Round Racers"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/chicken-merge.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/chicken-merge.png" data-src="https://htmlxm.github.io/thumb/chicken-merge.png" class="lazyload" alt="Chicken Merge"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/dreadhead-parkour.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/dreadhead-parkour.png" data-src="https://htmlxm.github.io/thumb/dreadhead-parkour.png" class="lazyload" alt="Dreadhead Parkour"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/we-become-what-we-behold.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/we-become-what-we-behold.png" data-src="https://htmlxm.github.io/thumb/we-become-what-we-behold.png" class="lazyload" alt="We Become What We Behold"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/stickman-hook.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/stickman-hook.png" data-src="https://htmlxm.github.io/thumb/stickman-hook.png" class="lazyload" alt="Stickman Hook"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/blumgi-ball.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/blumgi-ball.png" data-src="https://htmlxm.github.io/thumb/blumgi-ball.png" class="lazyload" alt="Blumgi Ball"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/stack-ball.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/stack-ball.png" data-src="https://htmlxm.github.io/thumb/stack-ball.png" class="lazyload" alt="Stack Ball"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/temple-of-boom.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/temple-of-boom.png" data-src="https://htmlxm.github.io/thumb/temple-of-boom.png" class="lazyload" alt="Temple Of Boom"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/who-is.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/who-is.png" data-src="https://htmlxm.github.io/thumb/who-is.png" class="lazyload" alt="Who Is"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/sausage-flip.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/sausage-flip.png" data-src="https://htmlxm.github.io/thumb/sausage-flip.png" class="lazyload" alt="Sausage Flip"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/murder.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/murder.png" data-src="https://htmlxm.github.io/thumb/murder.png" class="lazyload" alt="Murder"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/temple-run-2.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/temple-run-2.png" data-src="https://htmlxm.github.io/thumb/temple-run-2.png" class="lazyload" alt="Temple Run 2"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/soccer-skills-champions-league.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/soccer-skills-champions-league.png" data-src="https://htmlxm.github.io/thumb/soccer-skills-champions-league.png" class="lazyload" alt="Soccer Skills Champions League"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/idle-lumber-inc.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/idle-lumber-inc.png" data-src="https://htmlxm.github.io/thumb/idle-lumber-inc.png" class="lazyload" alt="Idle Lumber Inc"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/tiger-simulator-3d.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/tiger-simulator-3d.png" data-src="https://htmlxm.github.io/thumb/tiger-simulator-3d.png" class="lazyload" alt="Tiger Simulator 3d"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/gold-digger-frvr.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/gold-digger-frvr.png" data-src="https://htmlxm.github.io/thumb/gold-digger-frvr.png" class="lazyload" alt="Gold Digger Frvr"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/gobble.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/gobble.png" data-src="https://htmlxm.github.io/thumb/gobble.png" class="lazyload" alt="Gobble"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/drive-mad.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/drive-mad.png" data-src="https://htmlxm.github.io/thumb/drive-mad.png" class="lazyload" alt="Drive Mad"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/n-gon.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/n-gon.png" data-src="https://htmlxm.github.io/thumb/n-gon.png" class="lazyload" alt="N Gon"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/stack.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/stack.png" data-src="https://htmlxm.github.io/thumb/stack.png" class="lazyload" alt="Stack"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/water-color-sort.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/water-color-sort.png" data-src="https://htmlxm.github.io/thumb/water-color-sort.png" class="lazyload" alt="Water Color Sort"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/masked-forces.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/masked-forces.png" data-src="https://htmlxm.github.io/thumb/masked-forces.png" class="lazyload" alt="Masked Forces"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/eugenes-life.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/eugenes-life.png" data-src="https://htmlxm.github.io/thumb/eugenes-life.png" class="lazyload" alt="Eugenes Life"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/madalin-stunt-cars-2.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/madalin-stunt-cars-2.png" data-src="https://htmlxm.github.io/thumb/madalin-stunt-cars-2.png" class="lazyload" alt="Madalin Stunt Cars 2"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/jumping-shell.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/jumping-shell.png" data-src="https://htmlxm.github.io/thumb/jumping-shell.png" class="lazyload" alt="Jumping Shell"></div>
    </div>
  </div>
  </a>
</div>


<div class="col-lg-2 col-md-4 col-6 grid-3">
  <a href="/play/tiny-fishing.html">
  <div class="game-item">
    <div class="list-game">
      <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/tiny-fishing.png" data-src="https://htmlxm.github.io/thumb/tiny-fishing.png" class="lazyload" alt="Tiny Fishing"></div>
    </div>
  </div>
  </a>
</div>

















  </div> <!-- end row You might also Like -->
	








</div> <!-- end container -->





  <div class="banner-ad-wrapper">
    <div class="banner-ad-content" style="padding: 20px 0; text-align: center;">
      
      <!-- ads_ngang -->



    </div>
  </div>





  <!-- Popular games section -->
  <h3 class="section-title">Popular games</h3>
  <div class="row grid-container">
  




  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/slope.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/slope.png" data-src="https://htmlxm.github.io/thumb/slope.png" class="small-thumb img-rounded lazyload" alt="Slope"></div>
        <div class="list-info">
          <div class="list-title">Slope</div>
          <div class="list-category">Running</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/stack.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/stack.png" data-src="https://htmlxm.github.io/thumb/stack.png" class="small-thumb img-rounded lazyload" alt="Stack"></div>
        <div class="list-info">
          <div class="list-title">Stack</div>
          <div class="list-category">Skill</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/stack-ball.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/stack-ball.png" data-src="https://htmlxm.github.io/thumb/stack-ball.png" class="small-thumb img-rounded lazyload" alt="Stack Ball"></div>
        <div class="list-info">
          <div class="list-title">Stack Ball</div>
          <div class="list-category">Jumping</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/basketball-stars.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/basketball-stars.png" data-src="https://htmlxm.github.io/thumb/basketball-stars.png" class="small-thumb img-rounded lazyload" alt="Basketball Stars"></div>
        <div class="list-info">
          <div class="list-title">Basketball Stars</div>
          <div class="list-category">Sports</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/tiny-fishing.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/tiny-fishing.png" data-src="https://htmlxm.github.io/thumb/tiny-fishing.png" class="small-thumb img-rounded lazyload" alt="Tiny Fishing"></div>
        <div class="list-info">
          <div class="list-title">Tiny Fishing</div>
          <div class="list-category">Sports</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/smash-karts.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/smash-karts.png" data-src="https://htmlxm.github.io/thumb/smash-karts.png" class="small-thumb img-rounded lazyload" alt="Smash Karts"></div>
        <div class="list-info">
          <div class="list-title">Smash Karts</div>
          <div class="list-category">Action</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/moto-x3m.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/moto-x3m.png" data-src="https://htmlxm.github.io/thumb/moto-x3m.png" class="small-thumb img-rounded lazyload" alt="Moto X3m"></div>
        <div class="list-info">
          <div class="list-title">Moto X3m</div>
          <div class="list-category">Racing</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/moto-x3m-2.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/moto-x3m-2.png" data-src="https://htmlxm.github.io/thumb/moto-x3m-2.png" class="small-thumb img-rounded lazyload" alt="Moto X3m 2"></div>
        <div class="list-info">
          <div class="list-title">Moto X3m 2</div>
          <div class="list-category">Racing</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  





  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/getaway-shootout.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/getaway-shootout.png" data-src="https://htmlxm.github.io/thumb/getaway-shootout.png" class="small-thumb img-rounded lazyload" alt="Getaway Shootout"></div>
        <div class="list-info">
          <div class="list-title">Getaway Shootout</div>
          <div class="list-category">Action</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/the-impossible-quiz.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/the-impossible-quiz.png" data-src="https://htmlxm.github.io/thumb/the-impossible-quiz.png" class="small-thumb img-rounded lazyload" alt="The Impossible Quiz"></div>
        <div class="list-info">
          <div class="list-title">The Impossible Quiz</div>
          <div class="list-category">Thinking</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/rooftop-snipers.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/rooftop-snipers.png" data-src="https://htmlxm.github.io/thumb/rooftop-snipers.png" class="small-thumb img-rounded lazyload" alt="Rooftop Snipers"></div>
        <div class="list-info">
          <div class="list-title">Rooftop Snipers</div>
          <div class="list-category">Action</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/rooftop-snipers-2.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/rooftop-snipers-2.png" data-src="https://htmlxm.github.io/thumb/rooftop-snipers-2.png" class="small-thumb img-rounded lazyload" alt="Rooftop Snipers 2"></div>
        <div class="list-info">
          <div class="list-title">Rooftop Snipers 2</div>
          <div class="list-category">Action</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/we-become-what-we-behold.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/we-become-what-we-behold.png" data-src="https://htmlxm.github.io/thumb/we-become-what-we-behold.png" class="small-thumb img-rounded lazyload" alt="We Become What We Behold"></div>
        <div class="list-info">
          <div class="list-title">We Become What We Behold</div>
          <div class="list-category">Adventure</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/house-of-hazards.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/house-of-hazards.png" data-src="https://htmlxm.github.io/thumb/house-of-hazards.png" class="small-thumb img-rounded lazyload" alt="House Of Hazards"></div>
        <div class="list-info">
          <div class="list-title">House Of Hazards</div>
          <div class="list-category">Skill</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/master-chess.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/master-chess.png" data-src="https://htmlxm.github.io/thumb/master-chess.png" class="small-thumb img-rounded lazyload" alt="Master Chess"></div>
        <div class="list-info">
          <div class="list-title">Master Chess</div>
          <div class="list-category">Thinking</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/football-legends.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/football-legends.png" data-src="https://htmlxm.github.io/thumb/football-legends.png" class="small-thumb img-rounded lazyload" alt="Football Legends"></div>
        <div class="list-info">
          <div class="list-title">Football Legends</div>
          <div class="list-category">Sports</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/rocket-soccer-derby.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/rocket-soccer-derby.png" data-src="https://htmlxm.github.io/thumb/rocket-soccer-derby.png" class="small-thumb img-rounded lazyload" alt="Rocket Soccer Derby"></div>
        <div class="list-info">
          <div class="list-title">Rocket Soccer Derby</div>
          <div class="list-category">Sports</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  


  <div class="col-lg-4 col-md-6 grid-2">
    <a href="/play/big-shot-boxing.html">
    <div class="game-item">
      <div class="list-game">
        <div class="list-thumbnail"><img src="https://htmlxm.github.io/thumb/big-shot-boxing.png" data-src="https://htmlxm.github.io/thumb/big-shot-boxing.png" class="small-thumb img-rounded lazyload" alt="Big Shot Boxing"></div>
        <div class="list-info">
          <div class="list-title">Big Shot Boxing</div>
          <div class="list-category">Sports</div>
    

        </div>
      </div>
    </div>
    </a>
  </div>  














</div> <!-- end Poplular -->






<!--           <div class="post-item">
              <div class="post-media">
                <div class="post-thumb">
                  <img title="Play Now" src="{thumb}" alt="{name} ">
                </div>
                <div class="post-body">

                  <div class="post-intro">



                  </div>

                   

                </div>
              </div>
            </div> -->



</div> <!-- end container -->






	<div class="footer-copyright py-4">
		<div class="container">
			rusk-games.pages.dev 		<span class="dsb-panel">
				       <a href="/term.html">Term</a> - <a href="/dmca.html">DMCA</a> - <a href="/policy.html">Policy</a></span>

		</div>
	</div>



	<script type="text/javascript" src="../js/jquery-3.6.2.min.js"></script>
	<script type="text/javascript" src="../js/lazysizes.min.js"></script>
	<script type="text/javascript" src="../js/popper.min.js"></script>
	<script type="text/javascript" src="../js/bootstrap.min.js"></script>


	<script type="text/javascript" src="../js/script.js"></script>
	<script type="text/javascript" src="../js/custom.js"></script>





  </body>
</html>
''')

with open(f'embed/{filedir[5:]}', 'w') as game:
                    game.write(f'''
                               <!DOCTYPE html>
                                <html lang="en">
                                <head>
                                    <meta charset="UTF-8">
                                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                                    <title>{name}</title>
                                    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
                                </head>

                                <body style="padding: 0; margin: 0; background-color: white; overflow: hidden">
                                    <script src="embed.js"></script>
                                    <iframe src="https://rusk-games.pages.dev/{filedir}" frameborder="0" style="width: 100vw; height: 100vh" id="iframe"></iframe>
                                </body>
                                </html>
                                ''')
# soup = BeautifulSoup(html_content, 'html.parser')

# divs = soup.find_all('div', class_='col-lg-4')

# for i, div in enumerate(divs):
#     a_tag = div.find_next('a')
    
#     if a_tag and 'href' in a_tag.attrs:
#         href_dict[a_tag['href']] = a_tag.sourceline

# href_dict['hi']='hello'
# sorted_dict = {k: href_dict[k] for k in sorted(href_dict)}

# current_key = 'hi'
# keys=list(sorted_dict.keys())

# current_index = keys.index(current_key)
# if current_index < len(keys) - 1:
#     next_key = keys[current_index - 1]
#     print(next_key)  




