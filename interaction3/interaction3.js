var x=0,y=0,resPower=0,power=0,arrowX,arrowY,isArrowLaunched=false,dy=0,dz=0,g=1.00002,snakeX,snakeY,isArrived=false,snakecolor="white",resarrowY;

function setup() {
  createCanvas(1200,800);
  snakeX=width/2;
  snakeY=height/2;
}


function draw() {
  background(125);
  
  snake();
  
  target();
  
  arrow();
  
  gauge();
  
  
  text(resPower%100,300,100);
}

function target(){
  x=lerp(x,mouseX,0.01);
  y=lerp(y,mouseY,0.01);
  push();
  fill(0,0,0,0);
  strokeWeight(1);
  circle(x,y,80,80);
  line(x-60,y,x-20,y);
  line(x+60,y,x+20,y);
  line(x,y-60,x,y-20);
  line(x,y+60,x,y+20);
  console.log(frameRate);
  pop();
}

function gauge(){
  push();
  rectMode(CENTER);
  fill(255);
  rect(width/2,height-40,500,20);
  if(mouseIsPressed){
    fill(255,0,0);
    rect(width/2,height-40,power%100*5,20);
    power+=1;
  }
  pop();
}
function mouseReleased(){
    resPower=power%100;
    power=0;
    arrowX=x
    arrowY=y
    isArrowLaunched=true;
    dy=0;
    dz=0;
  }
function arrow(){
  if(isArrowLaunched){
  dy=dy*g+5-(0.05*resPower);
  dz=dz*g+0.1+(0.002*resPower);
  resarrowY=arrowY+dy
  push();
  circle(arrowX,arrowY+dy,50/dz);
  pop();
  if(50/dz<2){
   isArrowLaunched=false;
   isArrived=true;
   }
  }
}
function snake(){
  push();
  rectMode(CENTER);
  fill(snakecolor);
  snakeX=lerp(snakeX,random(snakeX-300,snakeX+300),0.01);
  snakeY=lerp(snakeY,random(snakeY-300,snakeY+300),0.01);
  rect(snakeX,snakeY,100,100);
  if(isArrived){
    if(arrowX<snakeX+50&&arrowX>snakeX-50&&resarrowY>snakeY-50&&resarrowY<snakeY+50){
    snakecolor="red"
    isArrived=false;
    }
    else{
    snakecolor="white"
    isArrived=false;
    }
  }
  
  pop();
}
