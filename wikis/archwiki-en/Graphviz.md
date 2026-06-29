# Graphviz

From Wikipedia:

:"Graphviz (short for Graph Visualization Software)  is a package of open-source tools for drawing graphs specified in DOT language scripts."

## Installation
Install the  package.

Viewers:
*
*

## Font
You need to install a font to include strings in the graph. For information how to install fonts, see Fonts.

To see what fonts are available:

 $ fc-list

To see what fonts dot is using:

 $ dot example.gv -Tpng -o foo.png -v 2>&1 | grep font

## Example
Here is a dot file example.

{{hc|1=example.gv|2=
digraph graph_name {
  graph [
    charset = "UTF-8";
    label = "sample graph",
    labelloc = "t",
    labeljust = "c",
    bgcolor = "#343434",
    fontcolor = white,
    fontsize = 18,
    style = "filled",
    rankdir = TB,
    margin = 0.2,
    splines = spline,
    ranksep = 1.0,
    nodesep = 0.9
  ;

  node [
    colorscheme = "rdylgn11"
    style = "solid,filled",
    fontsize = 16,
    fontcolor = 6,
    fontname = "Migu 1M",
    color = 7,
    fillcolor = 11,
    fixedsize = true,
    height = 0.6,
    width = 1.2
  ];

  edge [
    style = solid,
    fontsize = 14,
    fontcolor = white,
    fontname = "Migu 1M",
    color = white,
    labelfloat = true,
    labeldistance = 2.5,
    labelangle = 70
  ];

  // node define
  alpha = box;
  beta = box;
  gamma = Msquare;
  delta = box;
  epsilon = trapezium;
  zeta = Msquare;
  eta;
  theta = doublecircle;

  // edge define
  alpha -> beta = "a-b", arrowhead = normal;
  alpha -> gamma = "a-g";
  beta -> delta = "b-d";
  beta -> epsilon = "b-e", arrowhead = tee;
  gamma -> zeta = "g-z";
  gamma -> eta = "g-e", style = dotted;
  delta -> theta = crow;
  zeta -> theta = crow;
}
}}

To generate a png image from this file:

 $ dot -Tpng example.gv -o example.png
