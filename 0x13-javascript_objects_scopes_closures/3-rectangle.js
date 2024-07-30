#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if ((w > 0) && (h > 0)) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let y = 0; y < this.height; y++) {
      let p = '';
      for (let d = 0; d < this.width; d++) {
        p += 'X';
      }
      console.log(p);
    }
  }
}

module.exports = Rectangle;
