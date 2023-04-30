// creating class (class name should start with capital letter) and the class is created using function.
function bellBoy(name, age, isWorking, language)
{
    this.name = name;
    this.age = age;
    this.isWorking = isWorking;
    this.language = language;
}

// creating objects and objects is created using new keyword followed by class name
var bellboy1 = new bellBoy("timmy", 26, true, ['English' , 'tamil']);
var bellboy2 = new bellBoy("Sanjana", 20, true, ['tamil']);

// class variables can be accessed by using obj.attribute
console.log(bellboy1.language[1]);
console.log(bellboy2);
