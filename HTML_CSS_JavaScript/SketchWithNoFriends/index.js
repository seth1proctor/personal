$("#gameCanvasSection").hide();
$("#width1").hide();
$("#eraser").hide();
$("#win").hide();
$("#restart").hide();
$("#lose").hide();

let userDrawing;
let userHasDrawn = false;
let gameStart = false;
let loseTheGame;
let timerIsGoing;


function startGame() {
  userDrawing = $("#drawing").val();

  botResp.push(userDrawing);

  $("#gameCanvasSection").show();
  $("#width1").show();
  $("#eraser").show();
  $("#label").hide();
  $("#submit").hide();
  $("#drawing").hide();
  gameStart = true;
  music.play();
  timerIsGoing = true;

  setTimeout(addBotResp, 3 * 1000); 
}

if (timerIsGoing == true) {
    setTimeout(loseGame, 10 * 1000);    
  }

const winSound = Sound.from('assets/WinSound.mp3');
  
function winGame() { 
  $("#title").hide(); 
  $("#win").show();
  winSound.play();
  winSound.loop = false;
  music.stop(); 
  
}

function loseGame() {
  music.stop(); 
  $("#title").hide();
  $("#lose").show();
  loseTheGame = true;
}


  const music = Sound.from('assets/music.mp3')
    music.loop = true;
    music.volume = .25;

const botResp = ["Apple", "Tree", "House", "Sun", "pencil", "Flower", "Ant", "Tank", "Stapler", "Desk", "Light", "Chair", "Notepad", "Pens", "Pencils", "Shoe", "Book",
"Chairs", "Chocolate",]


const botResponse = new Text("", { fontFamily: 'Helvetica', fontSize: 12 });

botResponse.x = 350;
botResponse.y = 0;

function addBotResp() {
   if (userHasDrawn == true) {
    const random = Math.floor(Math.random() * botResp.length);

    const botResponses = botResp[random];

    botResponse.text += `Bot Guessed: ${botResponses}
`;
  
 if (botResponses == userDrawing) {
    winGame();
    timerIsGoing = false;
    return;
  }
  if (loseTheGame == true) {
    loseGame();
    return;
  }
  }

  setTimeout(addBotResp, 3 * 1000);
}

const stage = createStage({ width: 500, height: 350 });
stage.backgroundColor = 'white'.rgb;

let color = 'black'.rgb;
let mousePrev = { x: 0, y: 0 };
let width = 4;
const controller = new Container()
   
  .step(() => {
  if (gameStart == true) {

  if (Mouse.isDown) {
    const graphics = new Graphics()
    .tags("stroke")
      .lineStyle(width, color)
      .moveTo(mousePrev.x, mousePrev.y)
      .lineTo(Mouse.x, Mouse.y);
    stage.add(graphics);
    userHasDrawn = true;
  }
 
  mousePrev = { x: Mouse.x, y: Mouse.y };
  }
});

  const line = new Graphics()
    .lineStyle(4, 'black'.rgb)
    .moveTo(345, 0)
    .lineTo(345,350)

  const erase = Sound.from('assets/erase.mp3');

  const eraser = Sprite.from('assets/eraser.png')
    .at(300, 10)
  
  eraser.scale.set(.15,.15)
  eraser.click(() => {
    eraseCanvas();
    erase.play();
  });

  function eraseCanvas() {
    getDisplayObjectsByTag("stroke").destroy();
  }

  const click = Sound.from('assets/click.mp3');

  function makeSquare(color) {
    const square = new Graphics()
      .beginFill(color)
      .drawRect(4,4,3,4)
      square.scale.set(7,7)

    stage.add(square);
	  return square;
  }

  makeSquare("black".rgb).at(-15,-15).click(() => { color = 'black'.rgb; click.play();});
  makeSquare("blue".rgb).at(15,-15).click(() => { color = 'blue'.rgb; click.play();});
  makeSquare("red".rgb).at(45,-15).click(() => { color = 'red'.rgb; click.play();});
  makeSquare("orange".rgb).at(75,-15).click(() => { color = 'orange'.rgb; click.play();});
  makeSquare("yellow".rgb).at(105,-15).click(() => { color = 'yellow'.rgb; click.play();});
  makeSquare("purple".rgb).at(135,-15).click(() => { color = 'purple'.rgb; click.play();});
  makeSquare("green".rgb).at(165,-15).click(() => { color = 'green'.rgb; click.play();});
  makeSquare("brown".rgb).at(195,-15).click(() => { color = 'brown'.rgb; click.play();});
  makeSquare("grey".rgb).at(225,-15).click(() => { color = 'grey'.rgb; click.play();});



const circle = Sprite.from('assets/Circle.png')
  .at(319, 75)
  .click(() => {width = 4; click.play();});
  circle.scale.set(.04,.05)
const circle2 = Sprite.from('assets/Circle.png')
  .at(315, 127)
  .click(() => {width = 8; click.play();});
  circle2.scale.set(.09,.1)
const circle3 = Sprite.from('assets/Circle.png')
  .at(311, 180)
  .click(() => {width = 16; click.play();});
  circle3.scale.set(.13,.15)


function widthOne() {
  width = 10; 
}

function widthTwo() {
  width = 15;
}

function widthTwo() {
  width = 20;
}


stage.add(controller, eraser, circle, circle2, circle3, botResponse, line);

$("#submit").click(startGame);

