var capture;

function setup() {
  createCanvas(390, 240);
  capture = createCapture(VIDEO);
  console.log(VIDEO);
  capture.size(320, 240);
  //capture.hide();
}

function draw() {
  background(255);
  image(capture, 0, 0, 320, 240);
  filter('INVERT');
}

// var capture;

//   function setup() {
//     canvas = createCanvas(640, 480);
//     capture = createCapture(VIDEO);
//     // capture.size(320, 240);
//     capture.hide();
//   };

//   function draw() {
//     image(capture, 0, 0);
//     filter('gray');
//     //console.log(get(80,90));
//   };

/*
var captura;
var d = function(p){
  p.setup = function() {
    //captura = p.createCapture(p.VIDEO);
    // captura.hide();
  };

  p.draw = function() {
    p.background(255);
    p.image(capture, 0, 0);    
    p.filter('gray');
    // console.log(p.get(80,90));
  };
};

var myp6 = new p5(d, 'div2');
*/

// function setup() {           // **change** void setup() to function setup()
//   createCanvas(640, 360);    // **change** size() to createCanvas()
//   stroke(255);               // stroke() is the same
//   noFill();                  // noFill() is the same
// }

// function draw() {                         // **change** void draw() to function draw()
//   background(0);                          // background() is the same
//   for (var i = 0; i < 200; i += 20) {     // **change** int i to var i
//     bezier(mouseX-(i/2.0), 40+i, 410, 20, 440, 300, 240-(i/16.0), 300+(i/8.0)); // bezier() is the same
//   }
// }
