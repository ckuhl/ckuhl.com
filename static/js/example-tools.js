"use strict";

// create library and load it into the window
((window) => {
    const exampleTools = () => {
        let _libraryObject = {};

        // Create the demo setup given a div ID
        _libraryObject.createDemo = (demoId, caption) => {
            // get root element
            let root = d3.select("figure#" + demoId)
                .classed("figure", true);

            // remove noscript styling
            root.classed("noscript", false);

            // add graphics container
            root.insert("div")
                .attr("class", "graphics")
                .insert("svg")
                .classed("figure-img img-fluid rounded", true)
                .attr("id", demoId + "-svg")
                .attr("width", "100%")
                .attr("height", "100%");

            // add the caption
            root.insert("figcaption")
                .text(caption)
                .classed("figure-caption", true);

            return root;
        };

        // Add controls to demo object and return demo object
        _libraryObject.addControls = (divId) => {
            let root = d3.select("div#" + divId);
            root.insert("div")
                .classed("controls", true)
                .html(`\n<button type="button" class="btn btn-outline-primary" aria-label="Skip to start"><span class="fa fa-fast-backward"></span></button>\n<button type="button" class="btn btn-outline-primary" aria-label="Step backward"><span class="fa fa-backward"></span></button>\n<button type="button" class="btn btn-outline-primary" aria-label="Toggle pause / play"><span class="fa fa-play"></button>\n<button type="button" class="btn btn-outline-primary" aria-label="Step forward"><span class="fa fa-forward"></span></button>\n<button type="button" class="btn btn-outline-primary" aria-label="Skip to end"><span class="fa fa-fast-forward"></span></button>\n`);
            return root;
        };

        return _libraryObject;
    };


    // to make the library globally accessible, save to the window
    if (typeof(window.exampleTools) === 'undefined') {
        window.exampleTools = exampleTools();
    }

})(window);
