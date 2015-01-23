// http://wesleytodd.com/2013/4/drag-n-drop-in-raphael-js.html
Raphael.st.draggable = function() {
//Element.prototype.draggable = function() {
  var me = this,
      lx = 0,
      ly = 0,
      ox = 0,
      oy = 0,
      moveFnc = function(dx, dy) {
          lx = dx + ox;
          ly = dy + oy;
          me.transform('t' + lx + ',' + ly);
      },
      startFnc = function() {},
      endFnc = function() {
          ox = lx;
          oy = ly;
      };
  
  this.drag(moveFnc, startFnc, endFnc);
};

var num = 1;

var markups = [];

function gen_markup (paper, x, y, r) {
    var circle = paper.circle(x, y, r);
    // Sets the fill attribute of the circle to red (#f00)
    circle.attr("fill", "#f00");
    // Sets the stroke attribute of the circle to white
    circle.attr("stroke", "#fff");
    // circle.draggable();

    text = paper.text(x, y, num.toString()).attr({fill: '#fff'})

    var mySet = paper.set();

    mySet.push(circle);

    mySet.push(text);

    mySet.draggable();
    
    num++;

    return mySet;
}

$(document).ready(function () {
				// Creates canvas 320 × 200 at 10, 50
				var paper = Raphael(10, 50, 800, 600);
				// Creates circle at x = 50, y = 40, with radius 10
        var canvas = $('svg');
        canvas.on('click', function (event) {
          var posX = event.pageX;
            posY = event.pageY;
          console.log(posX + ", " + posY);
          var markup = gen_markup(paper, posX - $(this).position().left, posY - $(this).position().top, 20);
          markups.push(markup);
        });
				

			});

