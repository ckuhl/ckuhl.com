function Brick(pos_x, pos_y, width, height){
    this.x = pos_x;
    this.y = pos_y;
    this.height = height;
    this.width = width;
    this.alive = true;

    this.is_alive = function(){return this.alive;};
    this.kill = function(){this.is_alive = false;};
}
