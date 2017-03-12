function Brick(pos_x, pos_y, width, height){
    this.x = pos_x;
    this.y = pos_y;
    this.h = height;
    this.w = width;
    this.is_alive = true;

    this.kill = function(){this.is_alive = false;}
}
