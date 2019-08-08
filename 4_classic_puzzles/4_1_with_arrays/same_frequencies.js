/*
Puzzle Wording
==============
Write a function called 'same' which accept two arrays.
The function should return true if every value in the first array has it's corresponding value squared in the second array, at the same frequency.

Example:
-------
same([1, 2, 3], [4, 1, 9]) --> true
same([1, 2, 3], [1, 9]) --> false
same([1, 2, 1], [4, 4, 1]) --> false (must be same frequency)
*/

function naiveSame(array1, array2) {
  if (array1.length !== array2.length) {
    return false;
  }

  for (let i = 0; i < array1.length; i++) {
    let correctIndex = array2.indexOf(array1[i] ** 2);
    // for and indexOf() are like a nested loop

    if (correctIndex === -1) {
      return false;
    }
    array2.splice(correctIndex, 1);
  }

  return true;
}
// Time complexity of 'naiveSame': O(n**2)

function refactoredSame(array1, array2) {
  if (array1.length !== array2.length) {
    return false;
  }

  let counter1 = {};
  let counter2 = {};
  for (let elt of array1) {
    counter1[elt] = (counter1[elt] || 0) + 1;
  }
  for (let elt of array2) {
    counter2[elt] = (counter2[elt] || 0) + 1;
  }

  for (let key in counter1) {
    if (!(key ** 2 in counter2)) {
      return false;
    }
    if (counter2[key ** 2] !== counter1[key]) {
      return false;
    }
  }
  // Successive loops are often better than a nested loop

  return true;
}
