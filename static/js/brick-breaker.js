function Brick(pos_x, pos_y, width, height){
    this.x = pos_x;
    this.y = pos_y;
    this.height = height;
    this.width = width;
    this.alive = true;

    this.is_alive = function() {return this.alive;};
    this.kill = function() {this.is_alive = false;};
}


function InfoBar(canvas) {
    this.canvas = canvas;
    this.height = this.canvas.height / 16;
    this.width = this.canvas.width;
    this.score = 0;
    this.lives = 3;

    this.updateScore = function(brick, level){
        this.score += (brick * level);
    };

    this.loseLife = function() {
        this.lives -= 1;
    };

    this.livesString = function() {
        var return_string = "";
        for ( var i = 0; i < this.lives; i++ ){
            return_string += "❤";
        }
        return return_string;
    };

    this.draw = function(context, canvas) {
        context.font = "x-large Arial";
        context.fillStyle = "#003333";
        context.fillRect(0, 0, this.width, this.height);
        context.fillStyle = "#FFFFFF";
        context.fillText(this.livesString(), canvas.width / 32, canvas.height / 64 * 3);
        context.fillText(this.score.toString(), (canvas.width / 8) * 7, canvas.height / 64 * 3);
    };
}


function PlayField(canvas, infoBar){
    if ( canvas.width / canvas.height > 1 ) {
        this.x = canvas.width / 4;
        this.y = infoBar.height;
        this.width = canvas.width / 2;
        this.height = canvas.height - infoBar.height;
    } else {
        this.x = 0;
        this.y = infoBar.height;
        this.width = canvas.width;
        this.height = canvas.height - infoBar.height;
    }

    this.draw = function(context) {
        context.fillStyle = "#FFE3AA";
        context.fillRect(this.x, this.y, this.width, this.height);
    }
}


function BrickArray(){
    // TODO: Eventually import level layouts from JSON array (LevelFactory?)
    this.bricks =[];
    this.b_cols = 4;
    this.b_rows = 3;

    this.init = function(playField) {
        for (var x = 0; x < this.b_cols; x++) {
            this.bricks[x] = [];
            for (var y = 0; y < this.b_rows; y++) {
                var b_width = playField.width / (this.b_cols * 2 + 1);
                var pad = b_width;
                // TODO: Fix the brick placement calculation (see: LevelFactory)
                this.bricks[x][y] = new Brick(
                    Math.round(playField.x + pad + (b_width + pad) * x),
                    Math.round(playField.y + pad + (b_width + pad) * y),
                    Math.round(b_width),
                    Math.round(b_width / 2));
            }
        }
    };

    this.draw = function(context) {
        for (var i = 0; i < this.b_cols; i++) {
            for (var j = 0; j < this.b_rows; j++) {
                var b = this.bricks[i][j];
                if ( b.is_alive ) {
                    context.fillStyle = "#AA8439";
                    context.fillRect(b.x, b.y, b.width, b.height);
                }
            }
        }
    };

    // TODO: Fix collision detection algorithm
    this.collision = function(ball, infoBar) {
        for (var i = 0; i < this.b_cols; i++) {
            for (var j = 0; j < this.b_rows; j++) {
                var b = this.bricks[i][j];

                // check that the ball is (slightly) within the box
                if (b.is_alive
                        && (ball.x + ball.r / 3 * 2 > b.x)
                        && (ball.x - ball.r / 3 * 2 < (b.x + b.width))
                        && (ball.y + ball.r / 3 * 2 > b.y)
                        && (ball.y - ball.r / 3 * 2 < (b.y + b.height))) {

                    // differences between centre of box and ball x/y coord
                    var xDiff = ball.x - (b.x + b.width / 2);
                    var yDiff = ball.y - (b.y + b.height / 2);

                    // ratio is to stretch 45deg. angles to fit box shape
                    var bRatio = b.width / b.height;

                    // reflections
                    if (Math.abs(xDiff) > Math.abs(bRatio * yDiff)){
                        ball.dx *= -1;
                    }else{
                        ball.dy *= -1;
                    }
                    b.kill();
                    infoBar.updateScore(1, 1);  // TODO: Replace with level & brick score eventually
                }
            }
        }
    }
}


function Ball(canvas) {
    this.default_x = canvas.width / 2;
    this.default_y = canvas.height / 8 * 5;
    this.x = this.default_x;
    this.y = this.default_y;
    this.r = 10;
    this.dx = 1;
    this.dy = 1;

    this.draw = function(context) {
        context.beginPath();
        context.fillStyle = "#407F7F";
        context.arc(this.x, this.y, this.r, 0, Math.PI*2);
        context.fill();
        context.closePath();
    };

    this.update = function() {
        this.x += this.dx;
        this.y += this.dy;
    };

    this.reset = function() {
        this.x = this.default_x;
        this.y = this.default_y;
        this.dx = 1;
        this.dy = 1;
    };

    this.stop = function() {
        this.dx = 0;
        this.dy = 0;
    }
}


function Paddle(canvas) {
    this.width = 60;
    this.height = 18;
    this.x = (canvas.width - this.width) / 2;
    this.y = canvas.height * (7/8);

    this.draw = function(context) {
        context.fillStyle = "#003333";
        context.fillRect(this.x, this.y, this.width, this.height);
        // left curve
        context.beginPath();
        context.arc(this.x,
                this.y + this.height / 2,
                this.height / 2,
                Math.PI / 2,
                Math.PI / 2 * 3);
        context.fill();
        context.closePath();

        // right curve
        context.beginPath();
        context.arc(this.x + this.width,
                this.y + this.height / 2,
                this.height / 2,
                Math.PI / 2 * 3,
                Math.PI / 2 );
        context.fill();
        context.closePath();
    };

    this.update = function() {
    };
}


var BrickBreaker = function(document, location) {
    // set the context for the game
    this.canvas = (function() {
        var cvs = document.getElementById("brick-breaker");
        cvs.width = window.innerWidth;
        cvs.height = window.innerHeight;
        return cvs;
    })();
    this.context = this.canvas.getContext("2d");

    this.infoBar = new InfoBar(this.canvas);
    this.playField = new PlayField(this.canvas, this.infoBar);
    this.paddle = new Paddle(this.canvas);
    this.ball = new Ball(this.canvas);
    this.brickArray = new BrickArray(this.canvas, this.playField, this.ball);

    this.isPaused = false;

    // bind this to _this in order to get it into the listeners
    var game = this;
    function mouseMoveListener(e) {
        game.paddle.x = e.clientX;
        //game.paddle.y = e.clientY;
        e.preventDefault();
    }
    function touchMoveListener(e) {
        game.paddle.x = e.touches[0].clientX;
        //game.paddle.y = e.touches[0].clientY;
        e.preventDefault();
    }

    this.init = function() {
        document.addEventListener("mousemove", mouseMoveListener, false);
        document.addEventListener("touchmove", touchMoveListener, false);
        game.brickArray.init(game.playField);
    };

    this.draw = function() {
        // clear the screen
        if (game.isPaused === false) {
            game.context.clearRect(0, 0,
                game.canvas.width,
                game.canvas.height);

            // draw everything
            game.playField.draw(game.context);
            game.ball.draw(game.context);
            game.paddle.draw(game.context);
            game.brickArray.draw(game.context);
            game.infoBar.draw(game.context, game.canvas);
        } else {
            // border (i.e. slightly larger rect)
            game.context.fillStyle = "#552700";
            game.context.fillRect(game.playField.x + game.playField.width * (1/8),
                game.playField.y + game.playField.height * (3/8),
                game.playField.width * (6/8),
                game.playField.height * (1/8));
            // inner rect.
            game.context.fillStyle = "#FFD1AA";
            game.context.fillRect(game.playField.x + game.playField.width * (1/8) + 2,
                game.playField.y + game.playField.height * (3/8) + 2,
                game.playField.width * (6/8) - 4,
                (game.playField.height * (1/8)) - 4);

            game.context.font = "x-large Arial";
            game.context.fillStyle = "#FFFFFF";
            game.context.fillText("Click or tap to start",
                game.playField.x + game.playField.width * (1.5/8),
                game.playField.y + game.playField.height * (3.5/8));
        }
    };

    this.wait_for_start = function() {
        game.isPaused = true;
        game.ball.stop();

        var startX = -1;
        var startY = -1;

        function mouseDownListener(e) {
            startX = e.clientX;
            startY = e.clientY;
        }

        function touchStartListener(e) {
            startX = e.touches[0].clientX;
            startY = e.touches[0].clientY;
        }

        game.canvas.addEventListener("click", mouseDownListener, false);
        game.canvas.addEventListener("touchstart", touchStartListener, false);

        function wait_for_start() {
            if (startX > (game.playField.x + game.playField.width * (1/8)) &&
                    startY > (game.playField.y + game.playField.height * (3/8)) &&
                    startX < game.playField.x + game.playField.width * (7/8) &&
                    startY < game.playField.y + game.playField.height * (4/8)) {
                clearInterval(wait_interval);
                game.ball.reset();
                game.canvas.removeEventListener("click", mouseDownListener, false);
                game.canvas.removeEventListener("touchstart", touchStartListener, false);
                game.isPaused = false;
            }
        }

        var wait_interval = setInterval(wait_for_start, 10);
    };

    this.update = function() {
        if (game.isPaused === false) {
            game.collision_check();
            game.ball.update();
            game.paddle.update();
        }
    };

    this.collision_check = function() {
        // Walls
        if ( (game.ball.x - game.ball.r) < game.playField.x
                || (game.ball.x + game.ball.r) > game.playField.width + game.playField.x) {
            game.ball.dx *= -1
        }
        if ( (game.ball.y - game.ball.r) < game.playField.y) {
            game.ball.dy *= -1
        }
        if ((game.ball.y + game.ball.r) > game.playField.height + game.playField.y){
            game.infoBar.loseLife();
            game.ball.reset();
            game.wait_for_start();

            // TODO: Implement a better gamestate handler
            if ( game.infoBar.lives === 0 ) {
                window.alert("Game Over!");
                location.reload();
            }
        }

        if ( (game.ball.x + (game.ball.r / 2) > game.paddle.x)
                && (game.ball.x - (game.ball.r / 2) < (game.paddle.x + game.paddle.width))
                && (game.ball.y + (game.ball.r / 2) > game.paddle.y)
                && (game.ball.y - (game.ball.r / 2) < (game.paddle.y + game.paddle.height))) {
            // delta = x dist. from centre of the paddle scaled by 3
            var delta = Math.abs((game.paddle.x + (game.paddle.width / 2) - game.ball.x) / game.paddle.width / 3);
            console.log(delta);
            var c_s = Math.pow(game.ball.dy, 2) + Math.pow(game.ball.dx, 2)

            game.ball.dy *= (-1 * (1 + delta));
            game.ball.dx = Math.sqrt(c_s - Math.pow(game.ball.dy, 2));
        }

        game.brickArray.collision(game.ball, game.infoBar);
    };

    this.run = function() {
        game.init();

        game.draw();
        game.wait_for_start();

        setInterval(game.draw, 10);
        setInterval(game.update, 10);
    };
};
