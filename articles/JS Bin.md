JS Bin

let  audioRunning  =  false;
// create Oscillator node
let  oscillator;
const  canvas  =  document.querySelector('#timer');
const  W  =  canvas.width  =  window.innerWidth;
const  H  =  canvas.height;
const  ctx  =  canvas.getContext('2d');
const  freqPresets  = [0,1,2,3,4,5,10,20,30,40,50,100,200,440,600,800, 900]
​
const  slider  =  document.querySelector('input[type=range]');
slider.oninput  = () => {
 const  c  =  ui.freq  =  parseInt(slider.value, 10);
 if (audioRunning) {
 oscillator.frequency.value  =  c;
}
};
const  ui  = { freq: parseInt(slider.value, 10) };
​
const  RATE  =  60;
​
ctx.lineWidth  =  1;
ctx.lineCap  =  'round';
ctx.lineJoin  =  'round';
ctx.font  =  '24px monospace'
if (!ctx.setLineDash) {
 ctx.setLineDash  =  function () {}
}
​
​
const  generateSample  = (sampleNumber, method  =  'sin') => {
 const  sampleTime  =  sampleNumber  /  RATE;
 const  sampleAngle  =  sampleTime  *  2  *  Math.PI  *  ui.freq;
 return  Math[method](sampleAngle);
};
​
var  last  =  null;
var  degree  =  10;
var  H2  =  H/2;
var  half  =  H2  *  .9; // amplitude
var  padLeft  =  H;
var  lastTime  =  Date.now();
​
function  draw() {
 requestAnimationFrame(draw);
​
 // avoid drawing if you don't need to
 if (last  ===  ui.freq) {
// return;
}
​
 last  =  ui.freq;
​
​
 ctx.strokeStyle  =  '#000';
 ctx.fillStyle  =  '#00BCD4';
 ctx.save();
​
 ctx.clearRect(0, 0, W, H);
​