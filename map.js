// This script counts the number of tweets published by one person

function map() {

  // find all instances of the username in the JSON text
  var user = this.user.name.match(/\w+/g);

  if(user == null) {
    return;
  }

  for(var i = 0; i < user.length; ++i) {
    emit(this.user[i], {count:1});
  }

}
