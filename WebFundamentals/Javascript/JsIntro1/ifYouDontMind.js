/**
 * Created by jonat_000 on 1/27/2017.
 */
var HOUR = 8;
var MINUTE = 50;
var PERIOD = "AM";

if (MINUTE > 30 && HOUR > 7 && PERIOD === "AM") {
    console.log("It's almost " + 9 + " in the morning");
} else {
    console.log("It's just after " + 7 + " in the evening");
}