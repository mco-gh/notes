WebPPL - probabilistic programming for the web

### [WebPPL](http://webppl.org/)

File:

​x

// Class attendance model.
var  attendance  =  function(i_pl, i_stats, busy) {
 var  attendance  =  function (interest, busy) {
 if (interest) {
 return  busy  ?  flip(0.3) : flip(0.8);
} else {
 return  flip(0.1);
}
}
 var  a_4110  =  attendance(i_pl, busy);
 var  a_4780  =  attendance(i_stats, busy);
 var  a_4242  =  attendance(i_pl  &&  i_stats, busy);
​
 return {cs4110: a_4110, cs4780: a_4780, cs4242: a_4242};
}
​
// Relevance of our three papers.
var  relevance  =  function(i_pl, i_stats) {
 var  rel1  =  i_pl  &&  i_stats;
 var  rel2  =  i_pl;
 var  rel3  =  i_stats;
​
 return {paper1: rel1, paper2: rel2, paper3: rel3};
}
​
// A combined model.
var  model  =  function() {
 // Some even random priors for our "student profile."
 var  i_pl  =  flip(0.5);
 var  i_stats  =  flip(0.5);
 var  busy  =  flip(0.5);
​
 return [relevance(i_pl, i_stats), attendance(i_pl, i_stats, busy)];
}
​
// A model query that describes my class attendance.
var  rec  =  function() {
 var  i_pl  =  flip(0.5);
 var  i_stats  =  flip(0.5);
 var  busy  =  flip(0.5);
​
 // Require my conference attendance.
 var  att  =  attendance(i_pl, i_stats, busy);
 if (att.cs4242  &&  att.cs4110  &&  !att.cs4780) {
 factor(-Infinity);
};
​
 return  relevance(i_pl, i_stats);
}
​
var  dist  =  Enumerate(rec);
viz.auto(dist);