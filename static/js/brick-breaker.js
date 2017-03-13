/**
 * A brick object to destroy in Brick Breaker.
 * @param pos_x Number - position of top left corner
 * @param pos_y Number - position of top right corner
 * @param width Number - width of the brick
 * @param height Number - height of the brick
 * @constructor
 */
function Brick(pos_x, pos_y, width, height){
    this.x = pos_x;
    this.y = pos_y;
    this.height = height;
    this.width = width;
    this.alive = true;

    this.is_alive = function(){return this.alive;};
    this.kill = function(){this.is_alive = false;};
}
