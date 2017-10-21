// for each key value owner, it returns an emit
// emit is saying this.owner
// for each owner, emit the title
function map() { emit (this.owner, this.title); }

// for all the values in the value array, join them as a string
function reduce(key, value) { return value.join(); }

db.test.mapReduct(map, reduce, {out: { inline: 1}});



function map() { emit(this._id, this.created_at, this.name, this.text); }
function reduct(key, value) { return value.size(); }
db.MONGODB(map, reduce, {out: {inline:1} });








/*

def map():
    map = Code("function () {"
    " this.tags.forEach(function(z) {
    "    emit(z, 1);"
    " });"
    "}")

    */
