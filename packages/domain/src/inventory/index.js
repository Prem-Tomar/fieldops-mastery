import validateQuantity from "./validateQuantity.js";

import calculateReservationValue from "./calculateReservationValue.js";

// Example ValidateQuantity
console.log("_______________________________________");
console.log("Example:  ValidateQuantity");
console.log("_______________________________________");
console.log(validateQuantity(1), "testcase");
console.log(validateQuantity(Number.MAX_SAFE_INTEGER), "testcase");
console.log(validateQuantity(-1), "testcase");
console.log(validateQuantity({}), "testcase");
console.log(validateQuantity([]), "testcase");
console.log(validateQuantity(true), "testcase");
console.log(validateQuantity(undefined), "testcase");
console.log(validateQuantity(null), "testcase");
console.log(validateQuantity(Number.MAX_SAFE_INTEGER + 1), "testcase");
console.log(validateQuantity(2.5));
console.log(validateQuantity(0.1));
console.log(validateQuantity(Number.MIN_VALUE));

// Example calculateReservationValue
console.log("_______________________________________");
console.log("Example:  CalculateReservationValue");
console.log("_______________________________________");

console.log(calculateReservationValue(199, 3));
console.log(calculateReservationValue(199, 3, 10));
console.log(calculateReservationValue(199, 3, 100));
console.log(calculateReservationValue("199", 3));
console.log(calculateReservationValue(199, "3"));
console.log(calculateReservationValue(199, 3, null));
console.log(calculateReservationValue(Number.MAX_SAFE_INTEGER, 2));
