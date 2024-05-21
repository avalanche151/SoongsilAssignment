

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
    float snakeX = 0;
    float snakeY = 0;
    boolean isArrived = false;
    int snakeColor;
    float resarrowY = 0;


    void setup() {
        size(1200, 800);
        snakeX = width / 2;
        snakeY = height / 2;
        snakeColor = color(255); // initial snake color is white
    }

    void draw() {
        background(125);

        snake();
        target();
        arrow();
        gauge();

        fill(0);
        text(resPower % 100, 300, 100);
    }

    void target() {
        x = lerp(x, mouseX, 0.01f);
        y = lerp(y, mouseY, 0.01f);
        pushMatrix();
        fill(0, 0, 0, 0);
        strokeWeight(1);
        ellipse(x, y, 80, 80);
        line(x - 60, y, x - 20, y);
        line(x + 60, y, x + 20, y);
        line(x, y - 60, x, y - 20);
        line(x, y + 60, x, y + 20);
        popMatrix();
    }

    void gauge() {
        pushMatrix();
        rectMode(CENTER);
        fill(255);
        rect(width / 2, height - 40, 500, 20);
        if (mousePressed) {
            fill(255, 0, 0);
            rect(width / 2, height - 40, (power % 100) * 5, 20);
            power += 1;
        }
        popMatrix();
    }

    void mouseReleased() {
        resPower = power % 100;
        power = 0;
        arrowX = x;
        arrowY = y;
        isArrowLaunched = true;
        dy = 0;
        dz = 0;
    }

    void arrow() {
        if (isArrowLaunched) {
            dy = dy * g + 5 - 0.05f * resPower;
            dz = dz * g + 0.1f + 0.002f * resPower;
            resarrowY = arrowY + dy;
            pushMatrix();
            fill(255);
            rectMode(CENTER);
            rect(arrowX, arrowY + dy, 5 / dz, 80 / dz);
            rect(arrowX, arrowY + dy, 80 / dz, 5 / dz);
            fill(139, 69, 19); // brown color
            ellipse(arrowX, arrowY + dy, 30 / dz, 30 / dz);
            popMatrix();
            if (15 / dz < 2) {
                isArrowLaunched = false;
                isArrived = true;
            }
        }
    }

    void snake() {
        pushMatrix();
        rectMode(CENTER);
        fill(snakeColor);
        snakeX = lerp(snakeX, random(snakeX - 300, snakeX + 300), 0.01f);
        snakeY = lerp(snakeY, random(snakeY - 300, snakeY + 300), 0.01f);
        rect(snakeX, snakeY, 100, 100);
        if (isArrived) {
            if (arrowX < snakeX + 50 && arrowX > snakeX - 50 && resarrowY > snakeY - 50 && resarrowY < snakeY + 50) {
                snakeColor = color(255, 0, 0); // red color
                isArrived = false;
            } else {
                snakeColor = color(255); // white color
                isArrived = false;
            }
        }
        popMatrix();
    }
}
Scene3 scene=new Scene3();
void setup(){
  scene.setup();

}

void draw(){
  scene.draw();
}
void mouseReleased(){
  scene.mouseReleased();
}
