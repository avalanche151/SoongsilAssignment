class Scene3 {
  constructor() {
    this.x = 0;
    this.y = 0;
    this.resPower = 0;
    this.power = 0;
    this.arrowX = 0;
    this.arrowY = 0;
    this.isArrowLaunched = false;
    this.dy = 0;
    this.dz = 0;
    this.g = 1.00002;
    this.snakeX = 0;
    this.snakeY = 0;
    this.isArrived = false;
    this.snakecolor = "white";
    this.resarrowY = 0;
  }

  setup() {
    createCanvas(1200, 800);
    this.snakeX = width / 2;
    this.snakeY = height / 2;
  }

  draw() {
    background(125);

    this.snake();
    this.target();
    this.arrow();
    this.gauge();

    text(this.resPower % 100, 300, 100);
  }

  target() {
    this.x = lerp(this.x, mouseX, 0.01);
    this.y = lerp(this.y, mouseY, 0.01);
    push();
    fill(0, 0, 0, 0);
    strokeWeight(1);
    circle(this.x, this.y, 80);
    line(this.x - 60, this.y, this.x - 20, this.y);
    line(this.x + 60, this.y, this.x + 20, this.y);
    line(this.x, this.y - 60, this.x, this.y - 20);
    line(this.x, this.y + 60, this.x, this.y + 20);
    console.log(frameRate);
    pop();
  }

  gauge() {
    push();
    rectMode(CENTER);
    fill(255);
    rect(width / 2, height - 40, 500, 20);
    if (mouseIsPressed) {
      fill(255, 0, 0);
      rect(width / 2, height - 40, (this.power % 100) * 5, 20);
      this.power += 1;
    }
    pop();
  }

  mouseReleased() {
    this.resPower = this.power % 100;
    this.power = 0;
    this.arrowX = this.x;
    this.arrowY = this.y;
    this.isArrowLaunched = true;
    this.dy = 0;
    this.dz = 0;
  }

  arrow() {
    if (this.isArrowLaunched) {
      this.dy = this.dy * this.g + 5 - 0.05 * this.resPower;
      this.dz = this.dz * this.g + 0.1 + 0.002 * this.resPower;
      this.resarrowY = this.arrowY + this.dy;
      push();
      fill("white");
      rectMode(CENTER);
      rect(this.arrowX, this.arrowY + this.dy, 5 / this.dz, 80 / this.dz);
      rect(this.arrowX, this.arrowY + this.dy, 80 / this.dz, 5 / this.dz);
      fill("brown");
      circle(this.arrowX, this.arrowY + this.dy, 30 / this.dz);
      pop();
      if (15 / this.dz < 2) {
        this.isArrowLaunched = false;
        this.isArrived = true;
      }
    }
  }

  snake() {
    push();
    rectMode(CENTER);
    fill(this.snakecolor);
    this.snakeX = lerp(this.snakeX, random(this.snakeX - 300, this.snakeX + 300), 0.01);
    this.snakeY = lerp(this.snakeY, random(this.snakeY - 300, this.snakeY + 300), 0.01);
    rect(this.snakeX, this.snakeY, 100, 100);
    if (this.isArrived) {
      if (this.arrowX < this.snakeX + 50 && this.arrowX > this.snakeX - 50 && this.resarrowY > this.snakeY - 50 && this.resarrowY < this.snakeY + 50) {
        this.snakecolor = "red";
        this.isArrived = false;
      } else {
        this.snakecolor = "white";
        this.isArrived = false;
      }
    }
    pop();
  }
}

let scene3 = new Scene3();

function setup() {
  scene3.setup();
}

function draw() {
  scene3.draw();
}

function mouseReleased() {
  scene3.mouseReleased();
}
