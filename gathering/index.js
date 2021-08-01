let wBol = { xpos: 300, ypos: 300, xwid: 350, ywid: 350, r: 0, g: 0, b: 0};
let bBol = { xpos: 900, ypos: 300, xwid: 350, ywid: 350, r: 0, g: 0, b: 0};

function setup(){
  createCanvas(1200, 600);
}

function draw() {
  background(51);
  fill(wBol.r, wBol.g, wBol.b);
  ellipse(wBol.xpos, wBol.ypos, wBol.xwid, wBol.ywid);
  fill(bBol.r, bBol.g, bBol.b);
  ellipse(bBol.xpos, bBol.ypos, bBol.xwid, bBol.ywid);
  textSize(64);
  fill(255);
  text('text', 250, 320);
  fill(0);
  text('text', 850, 320);
}
function mousePressed(){
  var d1 = dist(300, 300, mouseX, mouseY);
  var d2 = dist(900, 300, mouseX, mouseY);
  if(d1 <= 350/2){
    //White text clicked
    console.log(Math.round(wBol.r), Math.round(wBol.g), Math.round(wBol.b), 1, 0);
    wBol.r = bBol.r = random(0,255);
    wBol.g = bBol.g = random(0,255);
    wBol.b = bBol.b = random(0,255);
  }
  if(d2 <= 350/2){
    //Black text clicked
    console.log(Math.round(bBol.r), Math.round(bBol.g), Math.round(bBol.b), 0, 1);
    wBol.r = bBol.r = random(0,255);
    wBol.g = bBol.g = random(0,255);
    wBol.b = bBol.b = random(0,255);
  }
}