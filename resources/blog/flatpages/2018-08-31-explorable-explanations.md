---
title: Explorable explanations
published: True
category: blog
scripts: [d3.v5.min.js, example-tools.js]
styles: [example-tools.css]
---

When learning a new concept, I learn best when I can play around with the idea
for a while. For some fields this takes the form of debate and discussion with
others. For some other fields however, this often takes the form of more
literally playing with the idea. Doodling and sketching have been very useful
when working out an algorithm.

Since having started this blog, I have often wanted to write a post about a
concept I've learned, only to find it difficult to get my point across by text
alone.

I've developed a solution that should fix most of that problem. Writing these
blog posts in Markdown, I can include arbitrary HTML tags in the posts. This
means I can even include `<script>` tags, and then use `d3.js` to create
widgets to illustrate what I am writing about, and embed it directly in the
text as I write it.

<figure class="demo" id="example1"></figure>
<script>
// set up demo
exampleTools.createDemo("example1", "An example animation");

// select element
var svg = d3.select("#example1-svg");

// get svg bounds
var h = svg.node().getBoundingClientRect().height;
var w = svg.node().getBoundingClientRect().width;

function animation() {
	var circle = svg.append("circle")
		.attr("cx", 0 + 0.25 * h)
		.attr("cy", "50%")
		.attr("r", h * 0.125)
		.attr("fill", "#00CCFF");

	repeat();

	function repeat() {
		circle
			.attr("cx", 0 + 0.25 * h)
			.attr("fill", "#00CCFF")
			.transition()
			.duration(2000)

			.attr("cx", w - 0.25 * h)
			.attr("fill", "#00FF99")
			.transition()
			.duration(2000)

			.attr("cx", 0 + 0.25 * h)
			.attr("fill", "#00CCFF")

			.on("end", repeat);
	}
};

animation();
</script>

So I've created a little JavaScript library that will attach to a `<figure>`
tag and set up an image and controls as needed. Then all I have to do is write
the visualization and it's done, just like that. With the ease of use, I look
forward to writing about all kinds of topics in the future.
