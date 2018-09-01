---
    title: Explorable explanations
    created: 2018-08-31 20:39 -7
    updated: 2018-08-31 20:39 -7
    published: False
    category: blog
    tags:
      - programming
    scripts:
      - "d3.v5.min.js"
...

When learning a new concept, I find I learn best when I have the ability to
play with the concept for a while. For some fields this takes the form of
debate, discussion, or even just thinking on it myself. For others however, I
benefit from having a physical example. When I don't have one, I often find
myself wishing I did in such cases. For example, when I was learning about the
Simplex algorithm, after finally understanding it, I had the feeling that if
only I had a better mental picture of what was happening, I could have figured
it out much quicker.

<div class="demo">
<svg id="example1"></svg>
<script>
//Select element
var svg = d3.select("svg#example1");

//Create rectangle element inside SVG
svg.append("circle")
	.attr("cx", 100)
	.attr("cy", 75)
	.attr("r", 35)
	.attr("fill", "green");
</script>
</div>

Always one to project, whenever I am explaining a concept to others, I try to
use models or concepts that can be played with. However when it came to my blog,
I struggled at first with how to present such concepts when my posts were
written in plain text.

The solution? Markdown! As it turns out, HTML can be included inside of
arbitrary Markdown. Including `<script>` tags! With those tools, I can create
small demonstrations inline with my documents.

<div class="demo">
<svg id="example2"></svg>
<script>
//Select element
var svg = d3.select("svg#example2");

//Create rectangle element inside SVG
svg.append("rect")
	.attr("x", 50)
	.attr("y", 50)
	.attr("width", 200)
	.attr("height", 100)
	.attr("fill", "red");
</script>
</div>

So I can write while I create my examples, a win-win!

