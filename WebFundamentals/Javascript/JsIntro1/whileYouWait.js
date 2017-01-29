/**
 * Created by jonat_000 on 1/27/2017.
 */
var daysUntilMyBirthday = 364;
while (daysUntilMyBirthday > 0) {
    if (daysUntilMyBirthday > 60) {
        console.log(daysUntilMyBirthday + " days until my birthday. Such a long time.");
    } else if (daysUntilMyBirthday >= 30) {
        console.log(daysUntilMyBirthday + " days until my birthday. It's getting closer.");
    } else if (daysUntilMyBirthday < 30 && daysUntilMyBirthday > 5) {
        console.log(daysUntilMyBirthday + " days until my birthday. It's right around the corner");
    } else if (daysUntilMyBirthday <= 5 && daysUntilMyBirthday > 0) {
        console.log(daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY!");
    } else {
        console.log("HAPPY BIRTHDAY");
    }
    daysUntilMyBirthday -= 1;
}