Probabilistic Programming

	// A model query that describes my class attendance.

	var rec = function() {   var i_pl = flip(0.5);   var i_stats = flip(0.5);   var busy = flip(0.5);
	  // Require my conference attendance.
	  var att = attendance(i_pl, i_stats, busy);   require(att.cs4242 && att.cs4110 && !att.cs4780);
	  return relevance(i_pl, i_stats); }