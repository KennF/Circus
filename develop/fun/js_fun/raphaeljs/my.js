// http://wesleytodd.com/2013/4/drag-n-drop-in-raphael-js.html
// Raphael.st.draggable = function() {
Element.prototype.draggable = function() {
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

$(document).ready(function () {
				// Creates canvas 320 × 200 at 10, 50
				var paper = Raphael(10, 50, 320, 200);
				// Creates circle at x = 50, y = 40, with radius 10
				var circle = paper.circle(50, 40, 10);
				// Sets the fill attribute of the circle to red (#f00)
				circle.attr("fill", "#f00");
				// Sets the stroke attribute of the circle to white
				circle.attr("stroke", "#fff");
				circle.draggable();

				// var mySet = paper.set();
  
  				// mySet.push(circle);

				// mySet.draggable();

				circle.draggable();
			});

