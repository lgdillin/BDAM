// This function counts all counts and sums the number of tweets by a single person

function reduce(key, values) {
  var total = 0;
  for(var i = 0; i < values.length; ++i) {
    total += values[i].count;
  }
  //return total;
  return {count: total};
}
