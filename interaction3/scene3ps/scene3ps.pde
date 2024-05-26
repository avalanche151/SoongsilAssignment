

class Scene3 {
    float x = 0;
    float y = 0;
    int resPower = 0;
    int power = 0;
    float arrowX = 0;
    float arrowY = 0;
    boolean isArrowLaunched = false;
    float dy = 0;
    float dz = 0;
    float g = 1.00002f;
    float snakeX = 600;
    float snakeY = 800;
    boolean isArrived = false;
    int snakeColor;
    float resarrowY = 0;
    boolean canfire=true;
    PImage snakeupward;
    boolean ishit;
    float moveparallel=400;
    int gameFinished=0;
    int hitcount=0;
  
    void setup() {
        size(1200, 800);
        snakeupward=loadImage("file.png"); 
    }

    void draw() {
        background(125);

        snake();
        target();
        arrow();
        gauge();
        if(ishit){
        textSize(48);
        text("hit!",1000,200);
        }
        snakeY-=0.6;
        if(snakeY<0){
        gameFinished=2;
        }
        if(hitcount>5){
          gameFinished=1;
        }
        if(gameFinished==1||gameFinished==2){
        noLoop();
        }
    }

    void target() {
        x = lerp(x, mouseX, 0.01f);
        y = lerp(y, mouseY, 0.01f);
        pushStyle();
        fill(0, 0, 0, 0);
        strokeWeight(1);
        ellipse(x, y, 80, 80);
        line(x - 60, y, x - 20, y);
        line(x + 60, y, x + 20, y);
        line(x, y - 60, x, y - 20);
        line(x, y + 60, x, y + 20);
        popStyle();
    }

    void gauge() {
        pushStyle();
        rectMode(CENTER);
        fill(255);
        rect(width / 2, height - 40, 500, 20);
        popStyle();
    }
    void mousePressed(){
      pushStyle();
      rectMode(CENTER);
      fill(255, 0, 0);
      if(mousePressed){
      rect(width / 2, height - 40, (power % 100) * 5, 20);
      power += 1;
      ishit=false;
      }
      popStyle();
    }
    
    void mouseReleased(){
      if(canfire){
        resPower = power % 100;
        power = 0;
        arrowX = x;
        arrowY = y;
        isArrowLaunched = true;
        dy = 0;
        dz = 0;
        canfire=false;
    }
    }

    void arrow() {
        if (isArrowLaunched) {
            dy = dy * g + 5 - 0.05f * resPower;
            dz = dz * g + 0.1f + 0.002f * resPower;
            resarrowY = arrowY + dy;
            pushStyle();
            fill(255);
            rectMode(CENTER);
            rect(arrowX, arrowY + dy, 5 / dz, 80 / dz);
            rect(arrowX, arrowY + dy, 80 / dz, 5 / dz);
            fill(139, 69, 19); // brown color
            ellipse(arrowX, arrowY + dy, 30 / dz, 30 / dz);
            popStyle();
            if (25 / dz < 2) {
                canfire=true;
                isArrived = true;
                isArrowLaunched = false;
                
            }
        }
    }

    void snake() {
        pushStyle();
        rectMode(CENTER);
        imageMode(CENTER);
        fill(snakeColor);
        if (frameCount % 120 == 0){
        moveparallel=random(snakeX - 200,snakeX + 200);
        }
        snakeX = lerp(snakeX,moveparallel, 0.01);
        
        if(snakeX<0){
          snakeX=0;
        }
        if(snakeX>width){
          snakeX=height;
        }
        
        pushMatrix();
        fill(snakeColor);
        image(snakeupward,snakeX, snakeY);
        popMatrix();
        if (isArrived) {
            if (arrowX < snakeX + 70 && arrowX > snakeX - 70 && resarrowY > snakeY - 135 && resarrowY < snakeY + 135) {
              ishit=true;
              hitcount++;
              isArrived = false;
            }
            else{
              ishit=false;
              isArrived=false;
            }
        }
        popStyle();
    }
}
Scene3 scene=new Scene3();
void setup(){
  scene.setup();

}

void draw(){
  scene.draw();
  scene.mousePressed();
}
void mouseReleased(){
  scene.mouseReleased();
}
